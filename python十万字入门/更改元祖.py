# coding=gbk
"""
作者：川川
时间：2021/8/23
群：970353786
"""
x = ("川川一号", "川川二号", "川川三号",'川川一号')
y = list(x)
y[1] = "帅哥"
x = tuple(y)
print(x)


thistuple = ("川川一号", "川川二号", "川川三号",'川川一号')
y = list(thistuple)
y.append("爱你")
thistuple = tuple(y)
print(thistuple)

thistuple = ("川川一号", "川川二号", "川川三号",'川川一号')
y = ("爱你",)
thistuple += y
print(thistuple)

thistuple = ("川川菜鸟", "川川二号", "川川三号",'川川一号')
y = list(thistuple)
y.remove("川川菜鸟")
thistuple = tuple(y)
print(thistuple)

this = ("川川菜鸟", "川川二号", "川川三号",'川川一号')
del this
print(this)