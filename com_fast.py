#컴퓨터최적화(2022.02.25.)

import os
import time



os.system('sfc /scannow')

os.system('DISM.exe /Online /Cleanup-image /Restorehealth')

os.system('ipconfig/displaydns')
os.system('ipconfig/flushdns')
os.system('DISM.exe /Online /Cleanup-image /Restorehealth')

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
#chkdsk /f 재시작 필요

#시스템 재시작 후 종료

