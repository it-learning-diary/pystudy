# coding=gbk
"""
���ߣ�����
ʱ�䣺2021/8/24
Ⱥ��970353786
"""
import json
# some JSON:
x ='{ "name":"����", "age":20, "city":"�Ϻ�"}'

# ����x
y = json.loads(x)
#�᷵���ֵ�
print(y["age"])


import json
# xΪ�ֵ�
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}
# תΪjson
y = json.dumps(x)
# ���Ϊjson�ַ���
print(y)
print(type(y))