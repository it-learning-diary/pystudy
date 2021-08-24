# coding=gbk
"""
作者：川川
时间：2021/8/24
群：970353786
"""
import json
# some JSON:
x ='{ "name":"川川", "age":20, "city":"上海"}'

# 解析x
y = json.loads(x)
#会返回字典
print(y["age"])


import json
# x为字典
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}
# 转为json
y = json.dumps(x)
# 结果为json字符串
print(y)
print(type(y))