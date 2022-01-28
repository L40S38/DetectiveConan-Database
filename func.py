import requests 
import bs4 

def get_soup(url):
    res = requests.get(url)
    res.raise_for_status() #エラーチェック

    soup = bs4.BeautifulSoup(res.text,"lxml")
    return soup

def rename_url(url):
    return 'https://websunday.net/' + url