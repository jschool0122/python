#!/usr/bin/env python
# coding: utf-8


#교원대 음악교육과 게시판 크롤링
#2022.02.26.
#selenium4로 업데이트 되면서 많은것이 바뀌었다. webdriver을 설정하는 부분이 Service를 사용해야 하는 등, 변화를 참고해서 개선하였음. 
#왜 갑자기 첨부파일을 다운받냐..

from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
from bs4 import BeautifulSoup
import time
import openpyxl
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

wb = openpyxl.Workbook()
ws = wb.active
ws.append(['제목', '날짜', '링크', '본문'])

s = Service('C:/dev_python/Webdriver/chromedriver.exe')
driver = webdriver.Chrome(service=s)

options = webdriver.ChromeOptions()
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko")


for num in range(1,2) :
    driver.get("http://music.knue.ac.kr/notice_02.brd/0"+str(num)+"..fc269d8/?shell=/index.shell:71")
    elems = driver.find_elements_by_css_selector('table.table4list > tbody > tr > td > a')
    link_list = list()
    for elem in elems:
        links = elem.get_attribute('href').strip("'")
        link_list.append(links)

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




