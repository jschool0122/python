import os  # .path.join(), .listdir(), .chdir(), .getcwd() 등 사용

import win32com.client as win32  # 한/글 열 수 있는 모듈
import win32gui  # 창 숨기기 위한 모듈
from datetime import datetime as dt

start = dt.now()
nowfolder = os.getcwd()  # 예제 hwp파일이 있는 폴더로 이동

hwp = win32.gencache.EnsureDispatch('HWPFrame.HwpObject')  # 한/글 열기
hwnd = win32gui.FindWindow(None, '빈 문서 1 - 한글')  # 해당 윈도우의 핸들값 찾기

win32gui.ShowWindow(hwnd, 0)  # 한/글 창을 숨겨줘. 0은 숨기기, 5는 보이기, 3은 풀스크린 등
hwp.RegisterModule('FilePathCheckDLL', 'FilePathCheckerModule')  # 보안모듈 적용

BASE_DIR = nowfolder # 한/글은 파일 열거나 저장할 때 전체경로를 입력해야 하므로, os.path.join(BASE_DIR, i) 식으로 사용할 것

hwp_file_list = []
for i in os.listdir(nowfolder) :
    if i.endswith('hwp') :
        hwp_file_list.append(i)
    else :
        continue

print('현재 한글파일 목록: ', hwp_file_list)

for i in hwp_file_list:  # 현재폴더 안에 있는 모든 파일을
    hwp.Open(os.path.join(BASE_DIR, i))  # 한/글로 열어서
    hwp.HAction.GetDefault('FileSaveAsPdf', hwp.HParameterSet.HFileOpenSave.HSet)  # PDF로 저장할 건데, 설정값은 아래와 같이.
    hwp.HParameterSet.HFileOpenSave.filename = os.path.join(BASE_DIR, i.replace('.hwp', '.pdf'))  # 확장자는 .pdf로,
    hwp.HParameterSet.HFileOpenSave.Format = 'PDF'  # 포맷은 PDF로(소문자 "pdf" 입력하면 오류 발생)
    hwp.HAction.Execute('FileSaveAsPdf', hwp.HParameterSet.HFileOpenSave.HSet)  # 위 설정값으로 실행해줘.

win32gui.ShowWindow(hwnd, 5)  # 다시 숨겼던 한/글 창을 보여주고,
hwp.XHwpDocuments.Close(isDirty=False)  # 열려있는 문서가 있다면 닫아줘(저장할지 물어보지 말고)
hwp.Quit()  # 한/글 종료

end = dt.now()
working_time = end - start
print('소요시간: ', working_time)
print('HWP -> PDF 변환이 완료되었습니다.')
os.system("pause")