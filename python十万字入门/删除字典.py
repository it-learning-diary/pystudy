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
thisdict.pop("address")
print(thisdict)
thisdict.popitem()
print(thisdict)

thisdict = {
  "name": "����",
  "address": "�Ϻ�",
  "year": 2000
}
del thisdict['name']
print(thisdict)

thisdict = {
  "name": "����",
  "address": "�Ϻ�",
  "year": 2000
}
thisdict.clear()
print(thisdict)

