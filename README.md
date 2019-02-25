# 오늘 한 것

- python 기초

- web craling
- github 사용법
- github를 이용한 개인 페이지 만들기

## 내용

Python 기초

```python
import os
from faker import Faker

fake = Faker("ko_KR")
print(fake.name())
for i in range(100):
    name = fake.name()
    cmd = f"touch {str(i)}_{name}.txt"
    os.system(cmd)

for a in list:
    print(a)
```

Faker 모듈을 이용해 더미 자료를 생성한 후, 수정하기

```python
import os

# 해당 폴더로 들어가기
os.chdir("/home/ubuntu/workspace/monday/student_list")
# 폴더 안에 모든 파일 돌면서
# 이름을 바꾼다.

# 현재 폴더의 존재하는 파일 이름들 리스트로 묶어줌
for filename in os.listdir("."):
    os.rename(filename, filename.replace("student","mc"))
    # 수정할 때에는!
```



Web Crawling

```python
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
```



advanced

```python
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
```



github 사용법

- 먼저 repository 생성

```bash
gtpgg1013:~/workspace $ cd monday
gtpgg1013:~/workspace/monday $ git init
$ git add .
$ git commit -m "first commit"
$ git remote add monday https://github.com/gtpgg1013/monday.git
$ git push -u monday master
```

push 다음 -u를 해놓으면 다음에 push 할때 monday에 알아서 commit 해줌



github를 이용한 개인 홈페이지 만들기

- 먼저 repository 생성 :  gtpgg1013.github.io

```bash
gtpgg1013:~/workspace $ cd githubio
gtpgg1013:~/workspace/githubio $ git init
$ git add .
$ git commit -m "first commit"
$ git remote add monday https://github.com/gtpgg1013/gtpgg1013.github.io
$ git push -u origin master
```

이 이후에 bootstrap에서 템플릿을 받은 후 내용을 긁어서 githubio안에 내용만 긁어서 복사!

