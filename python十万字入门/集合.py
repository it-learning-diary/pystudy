# coding=gbk
"""
作者：川川
时间：2021/8/24
群：970353786
"""
myset = {"川川一号", "川川二号", "川川三号"}
print(myset)


myset = {"川川一号", "川川二号", "川川三号"}
for i in myset:
    print(i)

myset = {"川川一号", "川川二号", "川川三号"}
print('串串一号' in myset)

myset = {"川川一号", "川川二号", "川川三号"}
myset.add('川川菜鸟')
print(myset)

myset = {"川川一号", "川川二号", "川川三号"}
myset1 = {"川川一号", "川川二号", "川川三号",'川川菜鸟'}
myset.update(myset1)
print(myset)

myset1 = {"川川一号", "川川二号", "川川三号",'川川菜鸟'}
myset2=['菜鸟','川川']
myset.update(myset2)
print(myset)

myset4 = {"川川一号", "川川二号", "川川三号",'川川菜鸟'}
myset4.remove('川川菜鸟')
print(myset4)

myset4 = {"川川一号", "川川二号", "川川三号",'川川菜鸟'}
myset4.discard('川川菜鸟')
print(myset4)

myset4 = {"川川一号", "川川二号", "川川三号",'川川菜鸟'}
myset4.pop()
print(myset4)

myset4 = {"川川一号", "川川二号", "川川三号",'川川菜鸟'}
myset.clear()
print(myset4)

myset4 = {"川川一号", "川川二号", "川川三号",'川川菜鸟'}
del myset4

myset4 = {"川川一号", "川川二号", "川川三号",'川川菜鸟'}
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


myset4 = {"川川一号", "川川二号", "川川三号",'川川菜鸟'}
myset5 = {"川川一号", "川川五号", "川川三号",'川川菜鸟'}
myset4.intersection_update(myset5)
print(myset4)

myset4 = {"川川一号", "川川二号", "川川三号",'川川菜鸟'}
myset5 = {"川川一号", "川川五号", "川川三号",'川川菜鸟'}
myset4.intersection(myset5)
print(myset4)


myset4 = {"川川一号", "川川二号", "川川三号",'川川菜鸟'}
myset5 = {"川川一号", "川川五号", "川川三号",'川川菜鸟'}
myset4.symmetric_difference_update(myset5)
print(myset4)

myset4 = {"川川一号", "川川二号", "川川三号",'川川菜鸟'}
myset5 = {"川川一号", "川川五号", "川川三号",'川川菜鸟'}
myset4.symmetric_difference(myset5)
print(myset4)