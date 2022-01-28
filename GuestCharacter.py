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
    gchara=case["Guest Characters"]
    for chara in gchara:
        number+=1
        datalist.append([number,title,chara])

df=pd.DataFrame(datalist,columns=["number","title","gchara"])
df.to_csv('dataset_csv/Title-GuestCharacter.csv',encoding='utf-8',index=None) 