import os

os.system('chkdsk /f')  #재부팅 필요

#시스템 재시작 후 종료
os.system('shutdown -r -t 10') #10초 뒤 재부팅
print('10초 뒤 재부팅 됩니다.')