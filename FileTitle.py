# -*- coding: utf-8 -*-

import json
import pandas as pd

with open('ConanData.json',encoding='utf-8') as f:
    jsn = json.load(f)

datalist = []

#ここまで雛形
count=1
for case in jsn.values():
    #print(case)
    files=case["Files"]
    for f in files:
        datalist.append([count,f['Volume'],f['Index'],f['Title']])
        count+=1

df=pd.DataFrame(datalist,columns=["number","volume","index","title"])
df.to_csv('dataset_csv/Volume-Index-Title.csv',encoding='utf-8',index=None)        
