# coding=gbk
"""
作者：川川
时间：2021/8/24
群：970353786
"""
tuple1 = ("川川菜鸟", "川川二号", "川川三号",'川川一号')
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)

tuple1 = ("川川菜鸟", "川川二号", "川川三号",'川川一号')
tuple4=tuple1*2
print(tuple4)

thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.count(5)
print(x)

thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.index(8)
print(x)