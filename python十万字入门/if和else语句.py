# coding=gbk
"""
作者：川川
时间：2021/8/24
群：970353786
"""
a = 33
b = 200
if b > a:
  print("b 大于 a")


a = 33
b = 33
if b > a:
  print("b 大于 a")
elif a == b:
  print("a 等于b")

a = 200
b = 33
if b > a:
  print("b 大于 a")
elif a == b:
  print("a 等于b")
else:
  print("a 小于 b")

a = 200
b = 33
if b > a:
  print("b 大于 a")
else:
  print("b 小于 a")

a = 200
b = 33
c = 500
if a > b and c > a:
  print("两种条件都满足")

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