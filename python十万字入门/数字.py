# coding=gbk
"""
作者：川川
时间：2021/8/22
群：970353786
"""
#整形
x = 1    # int
y = 2.8  # float
z = 1j   # complex
print(type(x))
print(type(y))
print(type(z))


x = 1
y = 3562254887
z = -35522
print(type(x))
print(type(y))
print(type(z))

#浮点
x = 1.10
y = 1.0
z = -35.59
print(type(x))
print(type(y))
print(type(z))

x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))

#类型转换
x = 1    # int
y = 2.8  # float
z = 1j   # complex

a = float(x)

b = int(y)

c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

#随机数
import random
print(random.randrange(1, 11))