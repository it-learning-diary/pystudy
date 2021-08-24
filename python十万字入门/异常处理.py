# coding=gbk
"""
作者：川川
时间：2021/8/24
群：970353786
"""
try:
  print(x)
except:
  print("An exception occurred")

try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")


try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")

# x= -1
# if x < 0:
#   raise Exception("Sorry, no numbers below zero")

x = "hello"

if not type(x) is int:
  raise TypeError("Only integers are allowed")