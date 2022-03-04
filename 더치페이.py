#!/usr/bin/env python
# coding: utf-8

# In[57]:


import math
from datetime import datetime

case = input('항목과 금액입력(스페이스바): ')
items = case.split(" ")

print(items)
casenum = len(items)

title = list()
price = list()

n = 1
for i in items[0::2] :
    title.append(i)
    
for i in items[1::2] :
    price.append(int(i))
    
item = title[:-1]
total = sum(price)
people = int(title[-1])
dutch_price = total / people

today = datetime.today()

print('[더치페이 계산내역]',today)
print('=' * 40)
print('항목: ', item)
print('금액: ', price)
print('계산: ', total, '/', people, '=', dutch_price,'\n')
print(str(round(dutch_price,-1))[:-2]+'원을 보내주세요(카카오페이 가능)')


#print('더치페이 값:', , '/', title[-1])
    
    

#햄버거 5000 오뎅 4000 피시방 50000 3


# In[ ]:




