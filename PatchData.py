# -*- coding: utf-8 -*-
# 編纂室のページそのものの誤りを、patches.json に従って ConanData.json 上で直す。
# ConanData.py の後、CSV を作る前（Case.py などの前）に実行する。何度実行しても結果は同じ。

import json
import codecs
import sys

#コンソールで表示できない字（簱・𠮷 など）があっても止まらないようにする
sys.stdout.reconfigure(errors='backslashreplace')

with open('ConanData.json',encoding='utf-8') as f:
    jsn = json.load(f)

with open('patches.json',encoding='utf-8') as f:
    patches = json.load(f)

def find_case(title):
    for case in jsn.values():
        if case['Title'] == title:
            return case
    return None

def remove_file(case, patch):
    #事件の話の一覧から、巻と巻内の話番号が一致する話を外す
    files = case['Files']
    kept = [f for f in files if not (f['Volume'] == patch['volume'] and f['Index'] == patch['index'])]
    if len(kept) == len(files):
        return False
    case['Files'] = kept
    return True

def add_chara(key):
    #人物を足す。after があればその人物の後ろ、before があればその人物の前、どちらも無ければ末尾に入れる
    def add(case, patch):
        charas = case[key]
        if patch['name'] in charas:
            return False
        after = patch.get('after')
        before = patch.get('before')
        if after in charas:
            charas.insert(charas.index(after) + 1, patch['name'])
        elif before in charas:
            charas.insert(charas.index(before), patch['name'])
        else:
            charas.append(patch['name'])
        return True
    return add

def rename_title(case, patch):
    #話タイトルの誤りを直す。巻と巻内の話番号が一致する話のタイトルが from のときだけ to にする
    for f in case['Files']:
        if f['Volume'] == patch['volume'] and f['Index'] == patch['index'] and f['Title'] == patch['from']:
            f['Title'] = patch['to']
            return True
    return False

def rename_chara(key):
    #同じ人物の呼び名を、編纂室がほかの事件で使っている名前にそろえる
    def rename(case, patch):
        charas = case[key]
        if patch['from'] not in charas:
            return False
        charas[charas.index(patch['from'])] = patch['to']
        return True
    return rename

ops = {
    'remove_file': remove_file,
    'rename_title': rename_title,
    'add_main': add_chara('Main Characters'),
    'add_guest': add_chara('Guest Characters'),
    'rename_guest': rename_chara('Guest Characters'),
}

for patch in patches:
    case = find_case(patch['case'])
    if case is None:
        print(f"{patch['id']}: 事件「{patch['case']}」が無い。事件名が変わっていないか確かめる")
        continue
    if ops[patch['op']](case, patch):
        print(f"{patch['id']}: 適用した（{patch['case']} {patch['op']}）")
    else:
        #もう直っている（適用済み、または編纂室側で直った）
        print(f"{patch['id']}: 直す対象が無い（適用済みか、編纂室側で直った）")
    if 'note' in patch:
        #消す時期などの注意書き（単行本の発売前の暫定パッチなど）
        print(f"    注意：{patch['note']}")

fw = codecs.open('ConanData.json', 'w','utf-8')
json.dump(jsn, fw, ensure_ascii=False, indent='\t')
fw.close()
print("**patch completed**")
