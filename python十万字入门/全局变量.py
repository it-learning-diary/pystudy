# coding=gbk
"""
���ߣ�����
ʱ�䣺2021/8/22
Ⱥ��970353786
"""

# x = "����"
# def myfunc():
#   print("˧���� " + x)
# myfunc()


# x = "awesome"
#
# def myfunc():
#   x = "fantastic"
#   print("Python is " + x)
#
# myfunc()
#
# print("Python is " + x)


x = "˧��"

def myfunc():
  global x
  x = "����"

myfunc()

print("����" + x)