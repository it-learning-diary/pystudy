# coding=gbk
"""
���ߣ�����
ʱ�䣺2021/8/22
Ⱥ��970353786
"""
#�ᱨ��
# age = 20
# txt ="�������� " + age
# print(txt)

age = 20
txt = "�������� {}"
print(txt.format(age))

quantity = 20
itemno = 3000
price = 49.95
myorder = "�������� {}�� ���˸���Ϊ�ֻ� {} ÿ���»��� {} Ԫ."
print(myorder.format(quantity, itemno, price))


quantity = 20
itemno = 3000
price = 49.95
myorder = "�������� {2}�� ���˸���Ϊ�ֻ� {0} ÿ���»��� {1} Ԫ."
print(myorder.format(quantity, itemno, price))