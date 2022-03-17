#!/usr/bin/env python
# coding: utf-8

# In[13]:


"""소수 중에서 각 자리의 숫자들을 순환시켜도 여전히 소수인 것을 원형 소수(circular prime)라고 합니다. 예를 들어 197은 971, 719가 모두 소수이므로 여기에 해당합니다.

이런 소수는 100 미만에 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97 처럼 13개가 있습니다.

그러면 1,000,000 미만에는 모두 몇 개나 있을까요?"""

#현재 1000000미만의 소수를 구하는 방법은 아래와 같음.

from numba import jit
import datetime

@jit(nopython=True)


def f_jit() :
    A=list()
    for n in range (2,1000000):
        DivisorNum=0
        for a in range (2,int(n**(1/2)+1)):
            if n%a==0:
                DivisorNum+=1
        if DivisorNum==0 :
            n=str(n)
            A.append(n)
    print(A)
    
start = datetime.datetime.now()
f_jit()
end = datetime.datetime.now()

print('총소요시간: ')
print(end-start)


# In[ ]:




