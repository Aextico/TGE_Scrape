from bs4 import BeautifulSoup as bs
import requests as rq
import datetime
nazwapliku = str(datetime.datetime.now().strftime("%Y%m%d-%H%M%S"))
csvurl = 'https://tge.pl/energia-elektryczna-rdn'
page = rq.get(csvurl)
soup = bs(page.content, 'html.parser')
datakontraktu = soup.find('small')
print(datakontraktu)
tabela = soup.find("div", class_="table-responsive wyniki-table-kontrakty-godzinowe")
strdopliku = '<html> \n' + str(datakontraktu) + '\n' + str(tabela) + '\n' + '</html>' 
with open(nazwapliku + '.xml' ,'a') as f:
    f.write(strdopliku)

