import requests 
import bs4 
import pandas as pd
import codecs

def get_soup(url):
    res = requests.get(url)
    res.raise_for_status() #エラーチェック

    soup = bs4.BeautifulSoup(res.text,"lxml")
    return soup

def rename_url(url):
    return 'https://websunday.net/' + url

url = 'https://websunday.net/conandb/comics-list/' 

soup = get_soup(url)

#print(soup)　#確認用

ul = soup.find("ul",attrs={"class","cover"})
volumes = ul.find_all("li")
print(volumes)
for volume in volumes:
    p = volume.find("p").get_text()
    print(p)
    url_volume = rename_url(volume.find("a").get("href"))
    text = get_soup(url_volume)
    print(f'p:{p}')
    case_list = text.find_all("tr")
    for case_tr in case_list:
        case = case_tr.find_all("td")
        case_number = case[0].get_text()
        case_url = rename_url(case[1].find("a").get("href"))
        print(f'case_number:{case_number}')
        case_detail = get_soup(case_url).find("div",attrs={"class","conanDb-main"})
        print(f'case_detail:{case_detail}')


#updatedetail = soup.find_all("div",attrs={"class","livedetail"})
