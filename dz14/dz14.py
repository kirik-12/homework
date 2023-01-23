import requests
from bs4 import BeautifulSoup as BS
import fake_useragent
import csv 


# с какого сайта считаем данные, делаем "анти бан пользователя", 
url =  'https://www.coingecko.com'
user_agent = fake_useragent.UserAgent().random
headers ={
    'User-Agent': user_agent
}
response = requests.get(url, headers=headers)   
  
html = BS(response.content,'html.parser')

# считаем данные с сайта
name = html.select('span[class="lg:tw-flex font-bold tw-items-center tw-justify-between"]')
price = html.select('td[class="td-price price text-right"]')
change_1_hour = html.select('td[class="td-change1h change1h stat-percent text-right col-market"]')
change_24_hours = html.select('td[class="td-change24h change24h stat-percent text-right col-market"]')
change_7_days = html.select('td[class="td-change7d change7d stat-percent text-right col-market"]')
volume_24_hors = html.select('td[class="td-liquidity_score lit text-right col-market"]')
mkt_cap = html.select('td[class="td-market_cap cap col-market cap-price text-right"]')

name_lst, price_lst, change_1_hour_lst, change_24_hours_lst, change_7_days_lst, volume_24_hors_lst, mkt_cap_lst = [],[],[],[],[],[],[]

for i in range(100):
    name_lst.append(name[i].text.strip())
    price_lst.append(price[i].text.strip().replace('$','').replace(',',''))
    change_1_hour_lst.append(change_1_hour[i].text.strip())
    change_24_hours_lst.append(change_24_hours[i].text.strip())
    change_7_days_lst.append(change_7_days[i].text.strip())
    volume_24_hors_lst.append(volume_24_hors[i].text.strip())
    mkt_cap_lst.append(mkt_cap[i].text.strip())

data = [name_lst, price_lst, change_1_hour_lst, change_24_hours_lst, change_7_days_lst, volume_24_hors_lst, mkt_cap_lst]


# создаём csv файл в который внесём полученные данные
with open('pars.csv','w') as csv_file:
    writer = csv.writer(csv_file, delimiter=';')
    writer.writerow(['name', 'price', 'change_1_hour', 'change_24_hours', 'change_7_days', 'volume_24_hors', 'mkt_cap'])
    for i in range(len(data[0])):
        writer.writerow([data[j][i] for j in range(7)])
