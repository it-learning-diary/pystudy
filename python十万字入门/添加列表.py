# coding=gbk
"""
���ߣ�����
ʱ�䣺2021/8/23
Ⱥ��970353786
"""
mylist = ["����һ��", "��������", "��������","�����ĺ�"]
mylist.append("��������")
print(mylist)


mylist = ["����һ��", "��������", "��������","�����ĺ�"]
mylist.insert(2,'��������')
print(mylist)

mylist = ["����һ��", "��������", "��������","�����ĺ�"]
mylist1 = ["����һ��", "��������", "��������","�����ĺ�"]
mylist.extend(mylist1)
print(mylist)

mylist = ["����һ��", "��������", "��������","�����ĺ�"]
mylist2=("����","����")
mylist.extend(mylist2)
print(mylist)