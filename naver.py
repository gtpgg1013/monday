import requests
from bs4 import BeautifulSoup

url = "https://naver.com"

res = requests.get(url)
print(res)
soup = BeautifulSoup(res.text, 'html.parser')
list = []
silgum = soup.select("#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_list.PM_CL_realtimeKeyword_list_base > ul:nth-child(5) > li:nth-child(1) > a.ah_a > span.ah_k")

for i in range(1,11):
    a = soup.select_one('#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_list.PM_CL_realtimeKeyword_list_base > ul:nth-child(5) > li:nth-child('+str(i)+') > a.ah_a > span.ah_k')
    list.append(a.text)

silgum = soup.select('a.ah_a > span.ah_k')
print(list)
print(len(list))
print(silgum)