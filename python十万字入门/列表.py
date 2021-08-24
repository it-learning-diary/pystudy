# coding=gbk
"""
作者：川川
时间：2021/8/22
群：970353786
"""
#单个列表索引
mylist = ["川川一号", "川川二号", "川川三号"]
print(mylist)
print(mylist[0])


thislist = list(("apple", "banana", "cherry"))
print(thislist)
#遍历列表
for i in mylist:
    print(i)

#允许重复
thislist = ["川川一号", "川川二号", "川川三号","川川一号"]
print(thislist)

#长度计算
thislist = ["川川一号", "川川二号", "川川三号","川川一号"]
print(len(thislist))

#数据类型
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

print(list1)
print(list2)
print(list3)
