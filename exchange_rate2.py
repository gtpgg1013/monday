import requests
from bs4 import BeautifulSoup
import pandas as pd

#내가 요청 보낸 시점과 브라우저의 시점이 다를 떄 (렌더링 시점 차이)
url = "https://finance.naver.com/marketindex/?tabSel=exchange#tab_section"

res = requests.get(url)

# print(res)

soup = BeautifulSoup(res.text, 'html.parser')
name = soup.select("body > div > table > tbody > tr > td.tit > a")
ratio = soup.select("body > div > table > tbody > tr > td.sale")
vsdollar = soup.select("body > div > table > tbody > tr > td:nth-child(7)")

print(name)

fulllist =[]

for i in range(0,len(name)):
    print(name[i].text, ratio[i].text, "미화대비",vsdollar[i].text)
    list = [name[i].text, ratio[i].text,vsdollar[i].text]
    fulllist.append(list)
    
df = pd.DataFrame(fulllist, columns = ['이름','비율','미화대비'])
print(df)