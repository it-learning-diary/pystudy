# coding=gbk
"""
作者：川川
时间：2021/8/22
群：970353786
"""
x = "川川"
print("帅哥是" + x)

x = "川川真"
y = "帅"
z = x + y
print(z)


x = 6
y = 10
print(x + y)

#会报错
# x = 5
# y = "川川"
# print(x + y)
#修改为：
x = 5
y = "川川"
print(str(x) + y)