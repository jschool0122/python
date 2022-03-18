#복수의 pdf파일들을 하나의 pdf파일로 통합하는 파이썬
#.py 와 동일 폴더 내에 pdf 파일들을 갖다 놓으면 통합됨.

from PyPDF2 import PdfFileMerger
import os
import datetime

nowtime = datetime.datetime.now().strftime('%Y%m%d-%H%M%S')
print(nowtime)
pdflist = list()
files = os.listdir(os.getcwd())

for file in files:
    if file.endswith('.pdf') :
        pdflist.append(file)
    else:
        continue

for i in pdflist:
    print(i)

merger = PdfFileMerger()

for pdf in pdflist:
    merger.append(pdf)

merge_pdf_name = '통합PDF_'+nowtime+'.pdf'
merger.write(merge_pdf_name)
merger.close()

print('PDF 통합 작업이 완료되었습니다.')
os.system("pause")
