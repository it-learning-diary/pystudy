# coding=gbk
"""
作者：川川
时间：2021/8/22
群：970353786
"""
#会报错
# age = 20
# txt ="川川今年 " + age
# print(txt)

age = 20
txt = "川川今年 {}"
print(txt.format(age))

quantity = 20
itemno = 3000
price = 49.95
myorder = "川川今年 {}岁 买了个华为手机 {} 每个月花费 {} 元."
print(myorder.format(quantity, itemno, price))


quantity = 20
itemno = 3000
price = 49.95
myorder = "川川今年 {2}岁 买了个华为手机 {0} 每个月花费 {1} 元."
print(myorder.format(quantity, itemno, price))