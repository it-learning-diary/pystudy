# coding=gbk
"""
���ߣ�����
ʱ�䣺2021/8/23
Ⱥ��970353786
"""
mylist = ["����һ��", "��������", "��������","�����ĺ�"]
mylist.remove('��������')
print(mylist)

mylist = ["����һ��", "��������", "��������","�����ĺ�"]
mylist.pop(2)
print(mylist)

mylist = ["����һ��", "��������", "��������","�����ĺ�"]
mylist.pop()
print(mylist)

mylist = ["����һ��", "��������", "��������","�����ĺ�"]
del mylist[0]
print(mylist)

mylist = ["����һ��", "��������", "��������","�����ĺ�"]
del mylist

mylist = ["����һ��", "��������", "��������","�����ĺ�"]
mylist.clear()
print(mylist)