# coding=gbk
"""
作者：川川
时间：2021/8/23
群：970353786
"""
mylist = ["川川一号", "川川二号", "川川三号","川川四号"]
mylist.append("憨批川川")
print(mylist)


mylist = ["川川一号", "川川二号", "川川三号","川川四号"]
mylist.insert(2,'川川菜鸟')
print(mylist)

mylist = ["川川一号", "川川二号", "川川三号","川川四号"]
mylist1 = ["川川一号", "川川二号", "川川三号","川川四号"]
mylist.extend(mylist1)
print(mylist)

mylist = ["川川一号", "川川二号", "川川三号","川川四号"]
mylist2=("川川","菜鸟")
mylist.extend(mylist2)
print(mylist)