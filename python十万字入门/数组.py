# coding=gbk
"""
���ߣ�����
ʱ�䣺2021/8/24
Ⱥ��970353786
"""
chuan = ["����", "����", "˧��"]
te=chuan[0]
print(te)

chuan = ["����", "����", "˧��"]
chuan[0]='�߸�˧'
# print(chuan)
print(len(chuan))


chuan = ["����", "����", "˧��"]
for i in chuan:
    print(i)

chuan = ["����", "����", "˧��"]
chuan.append('�Ϻ�')
print(chuan)

chuan = ["����", "����", "˧��"]
chuan.pop(1)
print(chuan)
chuan.remove('˧��')
print(chuan)