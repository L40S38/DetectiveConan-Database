# -*- coding: utf-8 -*-
from Mainfunc import * 
import json
import codecs

url = 'https://websunday.net/conandb/comics-list/' 

soup = get_soup(url)

#print(soup)　#確認用

ul = soup.find("ul",attrs={"class","cover"})
volumes = ul.find_all("li")
#print(volumes)
dataset = dict()
case_number=0
for volume in volumes:
    p = volume.find("p").get_text()
    #print(p)
    url_volume = rename_url(volume.find("a").get("href"))
    text = get_soup(url_volume)
    #print(f'p:{p}')
    case_list = text.find_all("tr")
    for case_tr in case_list:
        case = case_tr.find_all("td")
        if case_number == int(case[0].get_text()):
            continue
        case_number = int(case[0].get_text())
        case_url = rename_url(case[1].find("a").get("href"))
        print(f'case_number:{case_number}')
        case_detail = get_soup(case_url).find("div",attrs={"class","conanDb-main"})
        #print(f'case_detail:{case_detail}')
        case_title = get_title(case_detail)
        case_files = get_files(case_detail)
        case_mchara = get_mchara(case_detail)
        case_venue = get_venue(case_detail)
        case_gchara = get_gchara(case_detail)
        case_explain = get_explain(case_detail)
        

        data = {}
        data['Number'] = case_number
        data['Title'] = case_title
        data['Files'] = case_files
        data['Main Characters'] = case_mchara
        data['Place'] = case_venue
        data['Guest Characters'] = case_gchara
        data['Explain'] = case_explain
        dataset[case_number] = data
#updatedetail = soup.find_all("div",attrs={"class","livedetail"})
#print(dataset)
fw = codecs.open('ConanData.json', 'w','utf-8') 
json.dump(dataset, fw, ensure_ascii=False, indent='\t')
fw.close()
print("**output completed**")
