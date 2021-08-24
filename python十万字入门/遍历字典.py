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
for x in thisdict:
  print(x)

thisdict = {
  "name": "川川",
  "address": "上海",
  "year": 2000
}
for x in thisdict:
  print(thisdict[x])

thisdict = {
  "name": "川川",
  "address": "上海",
  "year": 2000
}
for x in thisdict.values():
  print(x)

thisdict = {
  "name": "川川",
  "address": "上海",
  "year": 2000
}
for x in thisdict.keys():
  print(x)

thisdict = {
  "name": "川川",
  "address": "上海",
  "year": 2000
}
for x, y in thisdict.items():
  print(x, y)