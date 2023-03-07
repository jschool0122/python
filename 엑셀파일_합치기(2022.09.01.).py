#!/usr/bin/env python
# coding: utf-8


#엑셀파일_합치기(2022.02.24.)
#2022.09.01. 통합 엑셀파일명에 날짜를 넣도록 업데이트

import os
import pandas as pd
import time

cwd = os.getcwd() #현재 파일이 속해있는 디렉토리의 경로.
print(cwd)
files = os.listdir(cwd)  
print(files)

df = pd.DataFrame()
for file in files:
    if file.endswith('.xlsx'):
        df = df.append(pd.read_excel(file, header = 1), ignore_index=True)  #df에 pd.read_excel 값을 추가한다. 단, 헤더는 위에서 2번째 행부터 시작하므로 header= 1로 설정. 인덱스 번호는 통합해서 센다.
        df.index = df.index + 1 #인덱스가 0부터 시작하니까 1부터 시작하도록 변경.
    elif file.endswith('xls'):
        df = df.append(pd.read_excel(file, header = 1), ignore_index=True)  #df에 pd.read_excel 값을 추가한다. 단, 헤더는 위에서 2번째 행부터 시작하므로 header= 1로 설정. 인덱스 번호는 통합해서 센다.
        df.index = df.index + 1 #인덱스가 0부터 시작하니까 1부터 시작하도록 변경.
    
df.head()

df.iloc[7:, 1:9]  #df.loc[행 범위, 열 범위]

print(df.iloc[7:, 1:9])

savedate = time.strftime('(%Y%m%d)')
save_file_name = '통합_엑셀파일'+savedate+'.xlsx'

df.to_excel(save_file_name)




