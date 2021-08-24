# coding=gbk
"""
作者：川川
时间：2021/8/24
群：970353786
"""
import datetime

x = datetime.datetime.now()
print(x)

import datetime
x = datetime.datetime.now()
print(x.year)
print(x.strftime("%A"))

import datetime
x = datetime.datetime(2021, 8, 25)
print(x)

import datetime
x = datetime.datetime(2011, 8, 25)
print(x.strftime("%B"))