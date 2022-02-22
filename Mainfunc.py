import requests 
import bs4 

def get_soup(url):
    res = requests.get(url)
    res.raise_for_status() #エラーチェック

    soup = bs4.BeautifulSoup(res.text,"lxml")
    return soup

def rename_url(url):
    return 'https://websunday.net/' + url
"""
def remove_unneslet(s):
    replacements = {
        '\r\n'  :'',
        ' '     :'',
        '　'    :''
    }
    print('{}'.format(''.join(map(re.escape, replacements.keys()))))
    return re.sub('{}'.format(''.join(map(re.escape, replacements.keys()))), lambda m: replacements[m.group()], s)
"""
def remove_unneslet(s):
    #print(s)
    s = s.replace('\n\n','').replace('\r\n','').replace(' ','').replace('\n','').replace('\u7c31','').replace('\U00020bb7','').replace('\u2661','').replace('\U000e0100','').replace('\u3000','')
    return s

def get_title(case_detail):
    case_title = case_detail.find("h1").get_text()
    #print(f'case_title:{case_title}')    
    case_title = remove_unneslet(case_title)
    return case_title

def get_files(case_detail):
    case_files = case_detail.find("div",attrs={"class","file"}).find_all("li")
    rtu = []
    for file in case_files:
        #print(file.get_text())  
        f=remove_unneslet(file.get_text())
        file_idx = f.find('「')
        title = f[file_idx:]
        volume = f[1:f.find('巻')]
        index = f[f.find('File')+4:file_idx]
        rtu.append({'Volume':volume,'Index':index,'Title':title})
    return rtu 

def get_mchara(case_detail):
    case_mchara = case_detail.find("div",attrs={"class","mchara"}).find_all("li")
    rtu = []
    for chara in case_mchara:  
        c = remove_unneslet(chara.get_text())
        #print(list(c))
        rtu.append(c)  
    #print(rtu)    
    return rtu

def get_venue(case_detail):
    case_venue = case_detail.find("div",attrs={"class","venue"}).find("p").get_text()
    case_venue = remove_unneslet(case_venue)
    if '／' in case_venue:
        case_venue = case_venue.split('／')
    else:
        case_venue = [case_venue]    
    return case_venue  

def get_gchara(case_detail):
    case_gchara = case_detail.find("div",attrs={"class","gchara"}).find("p").get_text()
    case_gchara = remove_unneslet(case_gchara)
    #print(case_gchara.split('／'))  
    return case_gchara.split('／')

def get_explain(case_detail):
    case_explain = case_detail.find("div",attrs={"class","naiyo__item"}).find("p").get_text() 
    case_explain = remove_unneslet(case_explain)
    #print(case_explain)
    return case_explain
