# coding=gbk
"""
���ߣ�����
ʱ�䣺2021/8/24
Ⱥ��970353786
"""
a = 33
b = 200
if b > a:
  print("b ���� a")


a = 33
b = 33
if b > a:
  print("b ���� a")
elif a == b:
  print("a ����b")

a = 200
b = 33
if b > a:
  print("b ���� a")
elif a == b:
  print("a ����b")
else:
  print("a С�� b")

a = 200
b = 33
if b > a:
  print("b ���� a")
else:
  print("b С�� a")

a = 200
b = 33
c = 500
if a > b and c > a:
  print("��������������")

a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")

x = 41
if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

a = 33
b = 200
if b > a:
  pass