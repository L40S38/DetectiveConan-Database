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
    number=case['Number']
    places=case['Place']
    title=case['Title']
    for p in places:
        number+=1
        datalist.append([number,title,p])

df=pd.DataFrame(datalist,columns=["number","title","Place"])
df.to_csv('dataset_csv/Title-Place.csv',encoding='utf-8',index=None) 