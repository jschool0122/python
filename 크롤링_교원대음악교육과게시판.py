#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#교원대 음악교육과 게시판 크롤링
#2022.02.15.

from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import time
import openpyxl

wb = openpyxl.Workbook()
ws = wb.active
ws.append(['제목', '날짜', '링크', '본문'])

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko")

chromedriver = 'C:/dev_python/Webdriver/chromedriver.exe' # 윈도우 
driver = webdriver.Chrome(chromedriver, chrome_options=options)


for num in range(1,2) :
    driver.get("http://music.knue.ac.kr/notice_02.brd/0"+str(num)+"..fc269d8/?shell=/index.shell:71")
    elems = driver.find_elements_by_css_selector('table.table4list > tbody > tr > td:nth-child(3) > a')
    link_list = list()
    for elem in elems:
        links = elem.get_attribute('href').strip("'")
        link_list.append(links)

    #print(link_list)

    for i in link_list:
        driver.get(i)
        title = driver.find_element_by_css_selector('tbody > tr > td.l_topbg > div.read_title')
        contents = driver.find_element_by_css_selector('div.sl_context > div > div > div.post_context > div.context_view')
        date = driver.find_element_by_css_selector('div.info_view > div > div:nth-child(3)')
        print('='*100)
        print('제목: '+title.text+'\n'+'날짜: '+date.text+'\n'+'링크: '+i+'\n'+'본문: '+contents.text)
        #print(title.text, date.text, i, contents.text)
        ws.append([title.text, date.text, i, contents.text])
        time.sleep(3)
        
        
wb.save('크롤링_교원대음악교육과.xlsx')
wb.close()

driver.quit()    


# In[ ]:




