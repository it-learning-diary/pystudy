# coding=gbk
"""
���ߣ�����
ʱ�䣺2021/8/24
Ⱥ��970353786
"""
thisdict = {
  "name": "����",
  "address": "�Ϻ�",
  "year": 2000
}
for x in thisdict:
  print(x)

thisdict = {
  "name": "����",
  "address": "�Ϻ�",
  "year": 2000
}
for x in thisdict:
  print(thisdict[x])

thisdict = {
  "name": "����",
  "address": "�Ϻ�",
  "year": 2000
}
for x in thisdict.values():
  print(x)

thisdict = {
  "name": "����",
  "address": "�Ϻ�",
  "year": 2000
}
for x in thisdict.keys():
  print(x)

thisdict = {
  "name": "����",
  "address": "�Ϻ�",
  "year": 2000
}
for x, y in thisdict.items():
  print(x, y)