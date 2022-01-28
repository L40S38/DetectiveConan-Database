# -*- coding: utf-8 -*-

import json
import pandas as pd

with open('ConanData.json',encoding='utf-8') as f:
    jsn = json.load(f)

datalist = []

#ここまで雛形

for case in jsn.values():
    #print(case)
    files=case["Files"]
    for f in files:
        datalist.append([f['Volume'],f['Index'],f['Title']])

df=pd.DataFrame(datalist,columns=["volume","index","title"])
df.to_csv('dataset_csv/Volume-Index-Title.csv',encoding='utf-8')        
