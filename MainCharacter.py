# -*- coding: utf-8 -*-

import json
import pandas as pd

with open('ConanData.json',encoding='utf-8') as f:
    jsn = json.load(f)

datalist = []

#ここまで雛形
number=0
for case in jsn.values():
    #print(case)
    title=case['Title']
    mchara=case["Main Characters"]
    for chara in mchara:
        if chara == "羽田秀":
            chara = "羽田秀𠮷"
        number+=1
        datalist.append([number,title,chara])

df=pd.DataFrame(datalist,columns=["number","case","mchara"])
df.to_csv('dataset_csv/Title-MainCharacter.csv',encoding='utf-8',index=None) 