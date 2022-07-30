import yfinance as yf
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

def get_data(tck, start ='2000-01-01', end='2021-12-31'):
    df = yf.download(tck, start=start, end=end)
    return df

def scraping_url(site:str, nameid="constituents"):    
    header = {'User-Agent': 'Mozilla/5.0'}
    req = Request(site,headers=header)
    page = urlopen(req)
    soup = BeautifulSoup(page, "lxml")
    table = soup.find('table', id=nameid)
    return table

def scraping_column(table, col:int) -> list:
    list_load = []
    for row in table.findAll('tr')[1:]:
        scr_col = row.findAll('td')[col].get_text()
        list_load.append(scr_col)
    scr_col = [n.replace('\n','').replace('.','-') for n in list_load]
    return scr_col

def get_table(table, scr_dict:dict) -> dict:
    scr_dict2 = {}
    for name,column in scr_dict.items():
        scr_col = scraping_column(table,column)
        scr_dict2[name] = scr_col
    return scr_dict2