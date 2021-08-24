# coding=gbk
"""
作者：川川
时间：2021/8/24
群：970353786
"""
thisdict = {
  "name": "川川",
  "address": "上海",
  "year": 2000
}
x = thisdict["name"]
y=thisdict.get('name')
print(x)
print(y)

thisdict = {
  "name": "川川",
  "address": "上海",
  "year": 2000
}
x = thisdict.keys()
print(x)

thisdict = {
  "name": "川川",
  "address": "上海",
  "year": 2000
}
thisdict['age']=20
print(thisdict)
x = thisdict.items()
print(x)

thisdict = {
  "name": "川川",
  "address": "上海",
  "year": 2000
}
if 'name' in thisdict:
    print('name在字典')