# coding=gbk
"""
作者：川川
时间：2021/8/24
群：970353786
"""
class MyClass:
  x = 5
print(MyClass)


class MyClass:
  x = 5
p1 = MyClass()
print(p1.x)


class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("川川菜鸟", 20)

print(p1.name)
print(p1.age)


class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("我的名字是 " + self.name)

p1 = Person("川川菜鸟", 20)
p1.myfunc()



class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("我的名字是 " + abc.name)

p1 = Person("川川菜鸟", 20)
p1.myfunc()



class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("我的名字是 " + abc.name)

p1 = Person("川川菜鸟", 20)
p1.age = 21
print(p1.age)


lass Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)

del p1.age
print(p1.age)#没有了自然打印报错


class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)

del p1

print(p1)
