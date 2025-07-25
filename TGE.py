from bs4 import BeautifulSoup as bs
import requests as rq
import datetime
nazwapliku = str(datetime.datetime.now().strftime("%Y%m%d-%H%M%S"))
csvurl = 'https://tge.pl/energia-elektryczna-rdn'
page = rq.get(csvurl)
soup = bs(page.content, 'html.parser')
tabela = soup.find("div", class_="table-responsive wyniki-table-kontrakty-godzinowe")
strtabela = str(tabela)
with open(nazwapliku + '.xml' ,'a') as f:
    f.write(strtabela)

