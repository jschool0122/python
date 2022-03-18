#!/usr/bin/env python
# coding: utf-8

# In[6]:


#네이버뉴스 모든 분야의 헤드라인을 10개씩 가져와서 pandas로 저장함.
#2022.2.26

from bs4 import BeautifulSoup
import requests
import openpyxl
import os
import pandas as pd
import time
from tqdm import tqdm

df = []

for news_num in tqdm(range(100, 106)) :
    if news_num == 100 :
        part='정치'
    elif news_num == 101 :
        part='경제'
    elif news_num == 102 :
        part='사회'
    elif news_num == 103 :
        part='생활/문화'
    elif news_num == 104 :  
        part='세계'
    elif news_num == 105 :    
        part='IT/과학'
        
    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'}
    url =  'https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1='+str(news_num)
    res = requests.get(url, headers = headers)

    soup = BeautifulSoup(res.content, 'html.parser')

    titles = soup.select('#main_content > div > div> div > div > div > ul > li > div.cluster_text > a')

    a = 0
    for index, i in enumerate(titles) : 
        if a <10 :
            title = i.text
            link = i['href']

            res2 = requests.get(link, headers = headers)
            soup2 = BeautifulSoup(res2.content, 'html.parser')

            in_date = soup2.select_one('div.article_info > div > span.t11')

            print(part, title, in_date.text, link)
            df.append([part, title, in_date.text, link])
            a = index + 1
        if a > 9 :
            break
        
data = pd.DataFrame(df, columns = ['분야', '제목', '날짜', '링크'])


savedate = time.strftime('(%Y%m%d-%H%M%S)')
save_file_name = '네이버뉴스_모든분야_헤드라인_Top10'+savedate+'.xlsx'

data.index = data.index + 1 #가장 왼쪽에 자동 생성되는 인덱스 번호가 0이 아닌 1부터 시작되도록.
data.to_excel(save_file_name)
#data.to_excel('noindex.xlsx', sheet_name='noindex', index=False) #만약 가장 왼쪽 칼럼에 출력되는 index를 없애고 싶다면 index=False로 할 것. 


print('네이버 뉴스 모든 분야(정치, 경제, 사회, 생활/문화, 세계, IT/과학)의 상위 10개 헤드라인 뉴스를 엑셀파일에 저장했습니다.')
print('저장된 파일: '+save_file_name)

os.system("pause")


