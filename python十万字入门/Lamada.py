# coding=gbk
"""
���ߣ�����
ʱ�䣺2021/8/24
Ⱥ��970353786
"""
x = lambda a : a + 10
print(x(5))

x = lambda a, b : a * b
print(x(5, 6))

x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

def myfunc(n):
  return lambda a : a * n
mydoubler = myfunc(2)
print(mydoubler(11))

def myfunc(n):
  return lambda a : a * n
mytripler = myfunc(3)
print(mytripler(11))