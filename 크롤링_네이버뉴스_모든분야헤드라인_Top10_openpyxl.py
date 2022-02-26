#!/usr/bin/env python
# coding: utf-8

# In[7]:


#네이버뉴스 모든 분야의 헤드라인을 10개씩 가져와서 엑셀파일에 저장. openpyxl은 pandas와 달리 열 너비를 설정하여 엑셀로 저장하는 것이 가능함.
#2022.2.26.

from bs4 import BeautifulSoup
import requests
import openpyxl
import os
import time
from tqdm import tqdm


wb = openpyxl.Workbook()
ws = wb.active
ws.append(['분야','제목','날짜','링크'])
ws.column_dimensions['B'].width = 70
ws.column_dimensions['C'].width = 30

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
        if a < 10 : 
            title = i.text
            link = i['href']
            #print(title, link)

                #headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'}
            res2 = requests.get(link, headers = headers)
            soup2 = BeautifulSoup(res2.content, 'html.parser')

            in_date = soup2.select_one('div.article_info > div > span.t11')

            print(part, title, in_date.text, link)
            ws.append([part, title, in_date.text, link])
            a = index + 1
        if a > 9 :
            break
        
savedate = time.strftime('(%Y%m%d-%H%M%S)')
wb.save('크롤링_네이버뉴스_모든분야_헤드라인Top10'+savedate+'.xlsx')

print('네이버 뉴스 모든분야(정치, 경제, 사회, 생활/문화, 세계, IT/과학 분야)의 헤드라인 Top10 뉴스를 엑셀파일에 저장했습니다.')
print('현재폴더에서 '+'크롤링_네이버뉴스_모든분야_헤드라인Top10'+savedate+'.xlsx 를 찾아보세요.')

os.system("pause")


# In[ ]:




