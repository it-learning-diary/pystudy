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
thisdict.pop("address")
print(thisdict)
thisdict.popitem()
print(thisdict)

thisdict = {
  "name": "川川",
  "address": "上海",
  "year": 2000
}
del thisdict['name']
print(thisdict)

thisdict = {
  "name": "川川",
  "address": "上海",
  "year": 2000
}
thisdict.clear()
print(thisdict)

