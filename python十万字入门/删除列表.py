# coding=gbk
"""
作者：川川
时间：2021/8/23
群：970353786
"""
mylist = ["川川一号", "川川二号", "川川三号","川川四号"]
mylist.remove('川川二号')
print(mylist)

mylist = ["川川一号", "川川二号", "川川三号","川川四号"]
mylist.pop(2)
print(mylist)

mylist = ["川川一号", "川川二号", "川川三号","川川四号"]
mylist.pop()
print(mylist)

mylist = ["川川一号", "川川二号", "川川三号","川川四号"]
del mylist[0]
print(mylist)

mylist = ["川川一号", "川川二号", "川川三号","川川四号"]
del mylist

mylist = ["川川一号", "川川二号", "川川三号","川川四号"]
mylist.clear()
print(mylist)