# coding=gbk
"""
���ߣ�����
ʱ�䣺2021/8/24
Ⱥ��970353786
"""
myset = {"����һ��", "��������", "��������"}
print(myset)


myset = {"����һ��", "��������", "��������"}
for i in myset:
    print(i)

myset = {"����һ��", "��������", "��������"}
print('����һ��' in myset)

myset = {"����һ��", "��������", "��������"}
myset.add('��������')
print(myset)

myset = {"����һ��", "��������", "��������"}
myset1 = {"����һ��", "��������", "��������",'��������'}
myset.update(myset1)
print(myset)

myset1 = {"����һ��", "��������", "��������",'��������'}
myset2=['����','����']
myset.update(myset2)
print(myset)

myset4 = {"����һ��", "��������", "��������",'��������'}
myset4.remove('��������')
print(myset4)

myset4 = {"����һ��", "��������", "��������",'��������'}
myset4.discard('��������')
print(myset4)

myset4 = {"����һ��", "��������", "��������",'��������'}
myset4.pop()
print(myset4)

myset4 = {"����һ��", "��������", "��������",'��������'}
myset.clear()
print(myset4)

myset4 = {"����һ��", "��������", "��������",'��������'}
del myset4

myset4 = {"����һ��", "��������", "��������",'��������'}
for i in myset4:
    print(i)


set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)


myset4 = {"����һ��", "��������", "��������",'��������'}
myset5 = {"����һ��", "�������", "��������",'��������'}
myset4.intersection_update(myset5)
print(myset4)

myset4 = {"����һ��", "��������", "��������",'��������'}
myset5 = {"����һ��", "�������", "��������",'��������'}
myset4.intersection(myset5)
print(myset4)


myset4 = {"����һ��", "��������", "��������",'��������'}
myset5 = {"����һ��", "�������", "��������",'��������'}
myset4.symmetric_difference_update(myset5)
print(myset4)

myset4 = {"����һ��", "��������", "��������",'��������'}
myset5 = {"����һ��", "�������", "��������",'��������'}
myset4.symmetric_difference(myset5)
print(myset4)