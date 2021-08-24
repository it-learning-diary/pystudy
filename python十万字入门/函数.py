# coding=gbk
"""
作者：川川
时间：2021/8/24
群：970353786
"""
def my_function():
  print("川川菜鸟")
my_function()

def my_function(fname):
  print(fname + " 菜鸟")

my_function("川川")
my_function("川川吗")
my_function("憨批")

def my_function(fname, lname):
  print(fname + " " + lname)

my_function("川川", "菜鸟")

def my_function(*kids):
  print("川川帅哥 " + kids[2])
my_function("名字", "性别", "菜鸟")


def my_function(child3, child2, child1):
  print("最帅的是 " + child3)

my_function(child1 = "大白", child2 = "小白", child3 = "猪猪侠")

def my_function(**kid):
  print("它的名字是 " + kid["lname"])

my_function(fname = "菜鸟", lname = "川川")




def my_function(country = "Norway"):
  print("I am from " + country)
my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")


def my_function(food):
  for x in food:
    print(x)
fruits = ["apple", "banana", "cherry"]
my_function(fruits)

def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))

def myfunction():
  pass