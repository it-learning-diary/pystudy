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
x = thisdict["name"]
y=thisdict.get('name')
print(x)
print(y)

thisdict = {
  "name": "����",
  "address": "�Ϻ�",
  "year": 2000
}
x = thisdict.keys()
print(x)

thisdict = {
  "name": "����",
  "address": "�Ϻ�",
  "year": 2000
}
thisdict['age']=20
print(thisdict)
x = thisdict.items()
print(x)

thisdict = {
  "name": "����",
  "address": "�Ϻ�",
  "year": 2000
}
if 'name' in thisdict:
    print('name���ֵ�')