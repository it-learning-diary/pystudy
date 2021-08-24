# coding=gbk
"""
作者：川川
时间：2021/8/24
群：970353786
"""
chuan = ["川川", "菜鸟", "帅哥"]
te=chuan[0]
print(te)

chuan = ["川川", "菜鸟", "帅哥"]
chuan[0]='高富帅'
# print(chuan)
print(len(chuan))


chuan = ["川川", "菜鸟", "帅哥"]
for i in chuan:
    print(i)

chuan = ["川川", "菜鸟", "帅哥"]
chuan.append('上海')
print(chuan)

chuan = ["川川", "菜鸟", "帅哥"]
chuan.pop(1)
print(chuan)
chuan.remove('帅哥')
print(chuan)