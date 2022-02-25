#네이버 뉴스에서 키워드를 입력하여 크롤링 한 뒤 엑셀파일에 저장.
#뷰티풀 수프를 활용한 정적 크롤링. pandas를 활용하여 엑셀파일 저장. 저장 파일명에 검색 키워드와 날짜가 붙음.
#2022.02.07.

from bs4 import BeautifulSoup
import time
import requests
import datetime

import os
from tqdm import tqdm
import pandas as pd
import time

d = datetime.datetime.now()

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'}

search_key = input('검색어를 입력하세요: ')

work_date = (str(d.year)+'년 '+str(d.month)+'월 '+str(d.day)+'일 '+str(d.hour)+'시 '+str(d.minute)+'분 '+str(d.second)+'초')

print(work_date, '다음 키워드를 네이버 뉴스에서 검색합니다: '+search_key)
print('=' * 50)

df = []

for page in tqdm(range(1, 10)):
    url = 'https://search.naver.com/search.naver?where=news&sm=tab_pge&query='+search_key+'&sort=0&photo=0&field=0&pd=0&ds=&de=&cluster_rank=162&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so:r,p:all,a:all&start='+str(page-1)+str(1)
    res = requests.get(url)
    soup = BeautifulSoup(res.content, 'html.parser')

    titles = soup.select('div.news_wrap.api_ani_send > div > a.news_tit')
    froms = soup.select('div.news_wrap.api_ani_send > div > div.news_info > div.info_group > a.info.press')
    links = soup.select('div.news_wrap.api_ani_send > div > a.news_tit')
    date = soup.select('div.news_wrap.api_ani_send > div > div.news_info > div.info_group > span')
    
    a = 0
    for i in titles:   
        cont_title = i.text
        cont_from = froms[int(a)].text
        cont_date = date[int(a)].text
        cont_link = links[int(a)]['href']
        #print(cont_title, cont_from, cont_date, cont_link)
        a = a+1
        df.append([cont_title, cont_from, cont_date, cont_link])

data = pd.DataFrame(df, columns = ['제목','출처','날짜','링크'])

data.index = data.index + 1

savedate = time.strftime('(%Y%m%d-%H%M%S)')
savename = '네이버뉴스검색_'+search_key+savedate+'.xlsx'
data.to_excel(savename)

print('네이버 뉴스 검색 결과를 엑셀파일에 저장했습니다.')
print('파일명: '+savename)

os.system("pause")