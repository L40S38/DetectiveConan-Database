# -*- coding: utf-8 -*-
from func import get_soup
from func import rename_url

import attr
import requests 
import bs4 
import pandas as pd
import codecs

url = 'https://websunday.net/conandb/comics-list/' 

soup = get_soup(url)

#print(soup)　#確認用

ul = soup.find("ul",attrs={"class","cover"})
volumes = ul.find_all("li")
print(volumes)
case_number=0
for volume in volumes:
    p = volume.find("p").get_text()
    print(p)
    url_volume = rename_url(volume.find("a").get("href"))
    text = get_soup(url_volume)
    print(f'p:{p}')
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
        case_title = case_detail.find("h1").get_text()
        print(f'case_title:{case_title}')
        case_files = case_detail.find_all("li")
        for file in case_files:
            print(file.get_text())
        case_mchara = case_detail.find("div",attrs={"class","mchara"}).find_all("li")
        for chara in case_mchara:
            print(chara.get_text())
        case_venue = case_detail.find("div",attrs={"class","venue"}).find_all("p")
        for venue in case_venue:
            print(venue.get_text())
        case_gchara = case_detail.find("div",attrs={"class","gchara"}).find("p").get_text()
        print(f'case_gchara:{case_gchara}')
        print(case_gchara.split('／'))
        case_explain = case_detail.find("div",attrs={"class","naiyo__item"}).find("p").get_text()
        print(case_explain)
#updatedetail = soup.find_all("div",attrs={"class","livedetail"})
