# coding=gbk
"""
作者：川川
时间：2021/8/22
群：970353786
"""

# x = "川川"
# def myfunc():
#   print("帅哥是 " + x)
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


x = "帅哥"

def myfunc():
  global x
  x = "菜鸟"

myfunc()

print("川川" + x)