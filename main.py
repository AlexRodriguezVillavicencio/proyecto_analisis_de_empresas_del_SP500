from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import pandas as pd

import yfinance as yf
from sqlalchemy import create_engine

############################
#web scraping
############################

site = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
header = {'User-Agent': 'Mozilla/5.0'}
req = Request(site,headers=header)
page = urlopen(req)
soup = BeautifulSoup(page, "lxml")
table = soup.find('table', id="constituents")

#column "TICKER"
tickers = []
for row in table.findAll('tr')[1:]:
    ticker = row.findAll('td')[0].get_text()
    tickers.append(ticker)

ticker = [n.replace('\n','').replace('.','-') for n in tickers]

#column "COMPANY"
company = []
for row in table.findAll('tr')[1:]:
    name = row.findAll('td')[1].get_text()
    company.append(name)

company = [n.replace('\n', '') for n in company]


############################
# connection MySQL
############################

create_connection = 'mysql+pymysql://root@localhost:3306/sp&500'

for tck in ticker:
    df = yf.download(tck, start='2000-01-01', end='2021-12-31')
    df.reset_index(inplace=True)
    name_tck = tck.lower()
    connection = create_engine(create_connection)
    try:
        df.to_sql(name=name_tck,con=connection, index=False)
    except:
        print(f'la tabla {tck} ya existe')


############################
# DataFrame
############################

df_SP = pd.DataFrame()
df_SP['TICKER'] = ticker
df_SP['COMPANY'] = company
connc = create_engine(create_connection)
df_SP.to_sql(name='sp500',con=connc, index=False)