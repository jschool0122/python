#컴퓨터최적화(2022.02.25.)

import os
import time



os.system('sfc /scannow')

os.system('DISM.exe /Online /Cleanup-image /Restorehealth')

os.system('ipconfig/displaydns')
os.system('ipconfig/flushdns')

print('작업이 종료되었습니다.')
time.sleep(5)
os.system('pause')

#os.system('shutdown -s -f')



#도스창 열기

#최적화 명령어 입력
#ipconfig/displaydns
#ipconfig/flushdns
#DISM.exe /Online /Cleanup-image /Restorehealth
#sfc /scannow

#시스템 재시작 후 종료
os.system('shutdown -r -t 0') #10초 뒤 재부팅
