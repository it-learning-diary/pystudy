# coding=gbk
"""
���ߣ�����
ʱ�䣺2021/8/23
Ⱥ��970353786
"""
x = ("����һ��", "��������", "��������",'����һ��')
y = list(x)
y[1] = "˧��"
x = tuple(y)
print(x)


thistuple = ("����һ��", "��������", "��������",'����һ��')
y = list(thistuple)
y.append("����")
thistuple = tuple(y)
print(thistuple)

thistuple = ("����һ��", "��������", "��������",'����һ��')
y = ("����",)
thistuple += y
print(thistuple)

thistuple = ("��������", "��������", "��������",'����һ��')
y = list(thistuple)
y.remove("��������")
thistuple = tuple(y)
print(thistuple)

this = ("��������", "��������", "��������",'����һ��')
del this
print(this)