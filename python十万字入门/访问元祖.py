# coding=gbk
"""
���ߣ�����
ʱ�䣺2021/8/23
Ⱥ��970353786
"""
mytuple = ("����һ��", "��������", "��������")
print(mytuple[1])

mytuple = ("����һ��", "��������", "��������")
print(mytuple[-1])

mytuple = ("����һ��", "��������", "��������",'˧�紨��','�������')
print(mytuple[2:5])

mytuple = ("����һ��", "��������", "��������",'˧�紨��','�������')
print(mytuple[:4])


mytuple = ("����һ��", "��������", "��������",'˧�紨��','�������')
print(mytuple[2:])

mytuple = ("����һ��", "��������", "��������",'˧�紨��','�������')
print(mytuple[-4:-1])


thistuple = ("����һ��", "��������", "��������",'˧�紨��','�������')
if "˧�紨��" in thistuple:
  print("����, ˧�紨��' ��Ԫ���б�")
