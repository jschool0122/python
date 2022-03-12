#알라딘 신간 1PAGE를 크롤링하는 크롤러.
#Beautiful Soup를 사용한 정적 크롤러이며, pandas로 엑셀 저장한다. 
#이후 for 문을 활용하여 페이지 수를 넓힐 수 있는 가능성이 있음.


#!/usr/bin/env python
# coding: utf-8



from bs4 import BeautifulSoup
import requests
import os
import pandas as pd
import time

df = []

url = 'https://www.aladin.co.kr/shop/common/wnew.aspx?BranchType=1'

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'}
res = requests.get(url, headers = headers)

soup = BeautifulSoup(res.content, 'html.parser')

items = soup.select('#Myform > div.ss_book_box')

for i in items:
    link_list = []
    link_list.append(i.select_one('td > div > ul > li > a')['href'])
    #date = i.select('tr> td > div > ul > li:nth-child(2)')
    #realdate = str(date).split('|')[2].strip().split('</li>]')[0]  

    for link in link_list : 
        res_2 = requests.get(link, headers = headers)

        soup_2 = BeautifulSoup(res_2.content, 'html.parser')
        title = soup_2.select_one('div.Ere_prod_topwrap > div.Ere_prod_titlewrap > div.left > div > ul > li > div > a.Ere_bo_title').text
        #date = soup_2.select_one('div.Ere_prod_topwrap > div.Ere_prod_titlewrap > div.left > div > ul > li.Ere_sub2_title > span.Ere_PR10').text
        date = i.select('tr> td > div > ul > li:nth-child(2)')
        writer = soup_2.select_one('div.Ere_prod_topwrap > div.Ere_prod_titlewrap > div.left > div > ul > li.Ere_sub2_title > a:nth-child(1)').text
        if i.select_one('tr > td > p') == None :
            info = ""
        else: 
            info = i.select_one('tr > td > p').text
        
        print(title, writer, info, link)
        df.append([title, writer, info, link])
        
data = pd.DataFrame(df, columns = ['제목', '저자', '정보', '링크'])
data.index = data.index + 1

savedate = time.strftime('(%Y%m%d-%H%M%S)')
save_file_name = '크롤링_알라딘_신간('+savedate+').xlsx'
data.to_excel(save_file_name)

print('알라딘 신간 책을 크롤링했습니다. 현재폴더에서 '+save_file_name+'을 찾아보세요')

os.system("pause")

