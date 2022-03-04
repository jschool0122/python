#!/usr/bin/env python
# coding: utf-8

# In[3]:


#exe 파일로 변환하는 setup.py
#exe 파일로 만들고자 하는 .py의 이름을 매번 변경해야 한다.
#2022.02.05

from cx_Freeze import setup, Executable
 
buildOptions = dict(packages=[], excludes = [])
 
exe = [Executable('서울시교육청 in 네이버뉴스.py')]
 
setup(
    name='testingName',
    version='0.0.1',
    author='me',
    description = 'description',
    options = dict(build_exe = buildOptions),
    executables = exe
)
 


# In[2]:


python setup.py build

