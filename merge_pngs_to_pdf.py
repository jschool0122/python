#!/usr/bin/env python
# coding: utf-8

#png 파일을 pdf로 변경
#2022.02.25

from PIL import Image
from pprint import pprint
import os

filename = os.path.basename(__file__)#확장자까지 정확하게 입력.주피터 노트북에서는 __file__이 안먹힌다. 주피터 노트북에서는 진짜 파일명을 '~~.py'로 써줄 것. 
print(filename)
path = os.path.dirname(os.path.realpath(filename))
ConvertedToPdfPath = os.path.dirname(os.path.realpath(filename))

file_list = os.listdir(path)
print(file_list)
file_list.remove(filename)
#pprint(file_list)
img_list = []
k = 0
for i in file_list:
    k += 1
    if k%100==0:
        print("진행상황 : "+str(k)+'/'+str(len(file_list)))
    img = Image.open(path+"\\"+str(i))
    img_1 = img.convert('RGB')
    img_list.append(img_1)
img_1.save(ConvertedToPdfPath+'\\ConvertedToPdf.pdf',save_all=True, append_images=img_list)
print("완료되었습니다.")

