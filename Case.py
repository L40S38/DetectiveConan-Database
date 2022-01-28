# -*- coding: utf-8 -*-

import json
import pandas as pd

with open('ConanData.json',encoding='utf-8') as f:
    jsn = json.load(f)

datalist = []

#ここまで雛形

for case in jsn.values():
    #print(case)
    number=case['Number']
    title=case['Title']
    explain=case['Explain']
    datalist.append([number,title,explain])

df=pd.DataFrame(datalist,columns=["number","title","explain"])
df.to_csv('dataset_csv/Number-Title-Explain.csv',encoding='utf-8',index=None) 