#!/usr/bin/env python
# coding: utf-8

# In[89]:


#엑셀파일_합치기(2022.02.24.)

import os
import pandas as pd
cwd = os.path.abspath('') 
files = os.listdir(cwd)  


df = pd.DataFrame()
for file in files:
    if file.endswith('.xlsx'):
        df = df.append(pd.read_excel(file, header = 2), ignore_index=True)  #df에 pd.read_excel 값을 추가한다. 단, 헤더는 위에서 3번째 행부터. 인덱스 번호는 통합해서 센다.
        columns = ['학번', '이름', '내용']
        df.index = df.index + 1
df.head()

df.iloc[0:20, 1:4]


df.to_excel('통합_엑셀파일.xlsx')

