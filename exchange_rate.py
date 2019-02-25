import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query=%ED%99%98%EC%9C%A8%EC%A0%95%EB%B3%B4"

res = requests.get(url)

# print(res)

soup = BeautifulSoup(res.text, 'html.parser')
name = soup.select("#_cs_foreigninfo > div > div.contents03_sub > div > div.c_rate > div.rate_table_bx._table > table > tbody > tr > th > a > span")
ratio = soup.select("#_cs_foreigninfo > div > div.contents03_sub > div > div.c_rate > div.rate_table_bx._table > table > tbody > tr > td:nth-child(2) > span")
comp = soup.select("#_cs_foreigninfo > div > div.contents03_sub > div > div.c_rate > div.rate_table_bx._table > table > tbody > tr > td.flu_nm > em")
updown = soup.select("#_cs_foreigninfo > div > div.contents03_sub > div > div.c_rate > div.rate_table_bx._table > table > tbody > tr > td.flu_pct > span")

fulllist =[]

for i in range(0,8):
    print(name[i].text, ratio[i].text, "전일대비:",comp[i].text, "등락률:", updown[i].text)
    list = [name[i].text, ratio[i].text,comp[i].text, updown[i].text]
    fulllist.append(list)
    
df = pd.DataFrame(fulllist, columns = ['이름','비율','전일대비','등락률'])
print(df)