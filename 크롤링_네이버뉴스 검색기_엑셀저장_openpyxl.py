#!/usr/bin/env python
# coding: utf-8

# In[2]:


#네이버 뉴스에서 키워드를 입력하여 크롤링 한 뒤 엑셀파일에 저장.
#뷰티풀 수프를 활용한 정적 크롤링
#2022.02.07.

from bs4 import BeautifulSoup
import time
import requests
import datetime
import openpyxl
import os
from tqdm import tqdm

d = datetime.datetime.now()


headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'}
#res = requests.get('https://search.naver.com/search.naver?where=news&ie=utf8&sm=nws_hty&query=%EC%84%9C%EC%9A%B8%EC%8B%9C%EA%B5%90%EC%9C%A1%EC%B2%AD')
#soup = BeautifulSoup(res.content, 'html.parser')

search_key = input('검색어를 입력하세요: ')

wb = openpyxl.Workbook()
sheet = wb.active
sheet.append(['제목','언론사','날짜','링크'])
sheet.column_dimensions['A'].width = 70
sheet.column_dimensions['B'].width = 20
sheet.column_dimensions['C'].width = 15
sheet.column_dimensions['A'].width = 70

print('다음 키워드를 네이버 뉴스에서 검색합니다: '+search_key)
date = (str(d.year)+'년 '+str(d.month)+'월 '+str(d.day)+'일 '+str(d.hour)+'시 '+str(d.minute)+'분 '+str(d.second)+'초')
print(date)
print('=' * 50)

for page in tqdm(range(1, 10)):
    url = 'https://search.naver.com/search.naver?where=news&sm=tab_pge&query='+search_key+'&sort=0&photo=0&field=0&pd=0&ds=&de=&cluster_rank=162&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so:r,p:all,a:all&start='+str(page-1)+str(1)
    res = requests.get(url)
    soup = BeautifulSoup(res.content, 'html.parser')

    titles = soup.select('div.news_wrap.api_ani_send > div > a.news_tit')
    froms = soup.select('div.news_wrap.api_ani_send > div > div.news_info > div.info_group > a.info.press')
    links = soup.select('div.news_wrap.api_ani_send > div > a.news_tit')
    date = soup.select('div.news_wrap.api_ani_send > div > div.news_info > div.info_group > span')

    for index, i in enumerate(titles):  
        cont_title = i.text
        cont_from = froms[index].text
        cont_date = date[index].text
        cont_link = links[index]['href']
        #print(cont_title, cont_from, cont_date, cont_link)
        
        sheet.append([cont_title, cont_from, cont_date, cont_link])

daynum = date
savename = 'naver_news'+str(daynum)+'.xlsx'
wb.save(savename)
print('네이버 뉴스 검색 결과를 엑셀파일에 저장했습니다.')
os.system("pause")


# In[ ]:




