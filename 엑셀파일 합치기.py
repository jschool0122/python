#!/usr/bin/env python
# coding: utf-8

# In[9]:


#엑셀파일 합치기

import os
import pandas as pd
cwd = os.path.abspath('') 
files = os.listdir(cwd)  
print(files)

df = pd.DataFrame()
for file in files:
    if file.endswith('.xlsx'):
        df = df.append(pd.read_excel(file), ignore_index=true) 
df.head() 
df.to_excel('total_sales.xlsx')

