# coding=gbk
"""
���ߣ�����
ʱ�䣺2021/8/24
Ⱥ��970353786
"""
def my_function():
  print("��������")
my_function()

def my_function(fname):
  print(fname + " ����")

my_function("����")
my_function("������")
my_function("����")

def my_function(fname, lname):
  print(fname + " " + lname)

my_function("����", "����")

def my_function(*kids):
  print("����˧�� " + kids[2])
my_function("����", "�Ա�", "����")


def my_function(child3, child2, child1):
  print("��˧���� " + child3)

my_function(child1 = "���", child2 = "С��", child3 = "������")

def my_function(**kid):
  print("���������� " + kid["lname"])

my_function(fname = "����", lname = "����")




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