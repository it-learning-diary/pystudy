# coding=gbk
"""
作者：川川
时间：2021/8/22
群：970353786
"""
a = "川川"
print(a)

a = """从前有座山，
山里有座庙
庙里有个小和尚"""
print(a)

a = '''从前有座山，
山里有座庙
庙里有个小和尚'''
print(a)

a = "Hello, World!"
print(a[1])

for x in "chuanchuan":
  print(x)

a = "Hello, World!"
print(len(a))

txt = "The best things in life are free!"
print("free" in txt)

txt = "The best things in life are free!"
if "free" in txt:
  print("是的, 'free'存在.")


txt = "川川就读上海交大!"
print("川川" not in txt)


txt = "川川就读上海交大!"
if "川川" not in txt:
  print("No, '川川' 不在文档.")