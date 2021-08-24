
@[TOC]

# 推荐：个人推荐学习系列，推荐的一定是好的！

[matlab2021数学建模小白零基础学习系列](https://blog.csdn.net/weixin_46211269/category_11242184.html?spm=1001.2014.3001.5482)

[python制作qq机器人系列](https://blog.csdn.net/weixin_46211269/category_10912318.html?spm=1001.2014.3001.5482)

[三万字SQL数据库讲解系列](https://chuanchuan.blog.csdn.net/article/details/119814777)


# 0、源码下载地址

本博客代码下载地址：

```c
https://github.com/89461561511656/pystudy
```
你大可把本篇文章当作一本2021最新python基础书籍，所以大家好好利用。
关注一下吧，麻烦了。

# 一、内容过多，前言一定要看

**拥有本篇文章，意味着你拥有一本最完善的书籍**，讲得比书上全，语法也会比买的书上更详细，大家要慢慢看。拥有本篇文章，你将基础无敌，从此可以有能力自学一些高级教程。作者写了好几天，实在很累，**希望你三连支持。**

python，言简意赅就是：通俗易懂，功能强大无比，上手快，实用强。你跟着我在这里认真学完这一篇，你一定会学会最扎实的python基础，同时我还可以提供**免费辅导**，作者本是一名学生，并不图有任何好处。如果需要辅导，可以加从左侧栏加群，当然仅是交流，不会有时间一直教你，只能帮助你解决一些问题，更多要靠自己。

# 二、 python入门

软件安装我就不介绍了，大家b站搜一下python和pycharm安装安装即可，个人是推荐**python和pycharm**结合使用，pycharm是什么？是python的编译器，如果我们没有编译器，写代码是很困难的，而且pycharm提供了许多插件和优美的界面，使得你写代码又快又舒服，不会因为在python的IDE上写得头疼。
当然!下载软件不用到官网下，你只需要到软件管家下载即可，我也是这个公众号的忠实粉丝了。
入门第一步：打印

```c
print("Hello, World!")
```

当然，你想打印别的也可以，对吧？

```c
print('川川帅哥，我爱你')
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/89c86045dac6409cb57620dc648dc88d.png)


# 三、python缩进

最基本的语法，我不可能在这里把所有的语法都讲一遍，但是最基本语法要说一下。在这里，我们又不得不鸣谢**pycharm编译器**，实在帮助我们太多了。为什么这么说？pycharm中，它会自动帮助我们完成换行，缩进等问题，不会像IDE中写代码，要自己手动，如果忘记手动就回报错，因此我是不建议只用python解释器，一定要用pycharm!

举一些例子,当然，如果你是小白，现在只会打印，大可不必着急，你只需要看看，后面我会讲到。
比如缩进问题，缩进是指代码行开头的空格。if后面的语句需要tap一下（当然，如果你用pycharm编译器，会自动tap）。
例如：

```c
if 6 > 2:
  print("六大于二")
```

# 四、Python注释

注释可用于解释 Python 代码。注释可用于使代码更具可读性。注释可用于在测试代码时阻止执行。

## 1.单行注释

将需要注释的部分开头用#
例如：

```c
#川川真帅
print('川川帅哥，我爱你')
```

或者这样：

```c
print("Hello, World!") #川川真帅
```

你可以看到如下，这就是注释意义了，懂了吧。
![在这里插入图片描述](https://img-blog.csdnimg.cn/e5f8c9a845c14f3bbef03859529f3e49.png)

## 2.多行注释

第一种方法（不建议，太麻烦）

```c
#川川真帅
#川川真帅
#川川真帅
print("Hello, World!")
```

你也可以左键选中我们需要注释的代码，松开，按：Ctrl+/，就完成相同效果注释。
第二种方法：
把要注释的内容放到三个引号对里面。，例如：

```c
'''
川川真帅
川川真帅
'''
print('川川帅哥，我爱你')
```

**取消注释**
左键选中我们需要取消注释的代码，松开，按：Ctrl+/

# 五、Python 变量

## 1.变量定义理解

在 Python 中，当你给它赋值时就会创建变量：Python 没有用于声明变量的命令。变量在您第一次为其赋值时创建。
例如：

```c
x = 5
y = "川川"
print(x)
print(y)
```

对于同一个变量，赋值类型不同则会发生类型的变化，例如：

```c
x = 4       # x 现在是整形
x = "川川" # x 现在是字符串
print(x)
```

则打印为：
![在这里插入图片描述](https://img-blog.csdnimg.cn/21d9fd8f068344ea8867a93e86f4f83e.png)
如果要指定变量的数据类型，可以通过强制转换来完成，比如：

```c
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
```

那么刚刚我说到了类型，小白肯定还不知道类型是什么，怎么查看,我们来说一下如何获取类型，这里我们要用到type函数，举个例子：

```c
x = 5
y = "川川"
print(type(x))
print(type(y))
```

看看返回什么：int为整形，str为字符串。这是你要背的。
![在这里插入图片描述](https://img-blog.csdnimg.cn/0da912231f874f33b152c19f89dc9273.png)
可以使用单引号或双引号来声明字符串变量：

```c
x1 = "川川真棒"
x2 = '川川真棒'
print(x1)
print(x2)
```

返回为：
![在这里插入图片描述](https://img-blog.csdnimg.cn/5c258abf53294fbb924e70ddfef2f37c.png)
变量名区分大小写：

```c
a = 4
A = "川川"
print(a)
print(A)
```

返回为：

![在这里插入图片描述](https://img-blog.csdnimg.cn/17ac4237b957477ea314df3e6785abec.png)

## 2. 变量名命名

变量可以有一个简短的名称（如 x 和 y）或一个更具描述性的名称（age、carname、total_volume）。Python 变量的规则：

 - 变量名必须以字母或下划线字符开头
 - 变量名不能以数字开头
 - 变量名称只能包含字母数字字符和下划线（Az、0-9 和 _ ）
 - 变量名区分大小写（age、Age和AGE是三个不同的变量）

  例如：


```c
myvar = "川川"
my_var = "川川""
_my_var = "川川""
myVar = "川川""
MYVAR = "川川""
myvar2 = "川川""
```

**命名法则：**
骆驼法则：除了第一个单词外，每个单词都以大写字母开头

```c
myNameIs = "川川"
```

帕斯卡法则：每个单词都以大写字母开头

```c
MyNameIs = "川川"
```

蛇形法则：每个单词由下划线字符分隔

```c
My_Name_Is = "川川"
```

## 3. 分配多个值

**多个变量的多个值。**
Python 允许您在一行中为多个变量赋值：

```c
x, y, z = "川川一号", "川川二号", "川川三号"
print(x)
print(y)
print(z)
```

输出为：
![在这里插入图片描述](https://img-blog.csdnimg.cn/0c32b47f669a4e5ba2ee8594542415cb.png)
注意：确保变量的数量与值的数量相匹配，否则你会得到一个错误。

**多个变量的一个值**
您可以在一行中为多个变量分配相同的值：

```c
x = y = z = "川川菜鸟"
print(x)
print(y)
print(z)
```

输出为：
![在这里插入图片描述](https://img-blog.csdnimg.cn/f45ae5f1a9694cda94bc5e72e6447644.png)

**打开一个集合**
如果您在列表、元组等中有一组值。Python 允许您将值提取到变量中。这称为拆包。当然，在这里，你可能还不知道集合列表，元组是什么，没有关系，后面我会讲到。

```c
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)
```

## 4. 输出变量

print语句通常用于输出变量。
为了组合文本和变量，Python 使用 +字符：

```c
x = "川川"
print("帅哥是" + x)
```

输出为：
![在这里插入图片描述](https://img-blog.csdnimg.cn/025384ddb5db456d98aa8a692ef826ec.png)
您还可以使用该+字符将一个变量添加到另一个变量中：

```c
x = "川川真"
y = "帅"
z = x + y
print(z)
```

返回一样：
![在这里插入图片描述](https://img-blog.csdnimg.cn/b09ce74528744ea1b7b34af7280b04e7.png)
对于数字，该+字符用作数学运算符：

```c
x = 6
y = 10
print(x + y)
```

返回：
![在这里插入图片描述](https://img-blog.csdnimg.cn/7dad99dc3657410ebbce452877ab8875.png)
如果你尝试组合一个字符串和一个数字，Python 会给你一个错误，比如：

```c
​```c
x = 5
y = "川川"
print(x + y)
```


该怎么修改呢？把数字转为字符即可，则修改为：

```c
x = 5
y = "川川"
print(str(x) + y)
```

成功返回：
![在这里插入图片描述](https://img-blog.csdnimg.cn/4af3fe6874fc42d09a5cce029bf2515b.png)

## 5. 全局变量与局部变量，全局关键字

在函数外部创建的变量称为**全局变量**。都可以使用全局变量，无论是在函数内部还是外部。当然，在这里，你可能还不知道函数是什么，后面我会讲到，大可不必慌张。

```c
x = "川川"
def myfunc():
  print("帅哥是 " + x)
myfunc()
```

返回为：
![在这里插入图片描述](https://img-blog.csdnimg.cn/505a9df327a34676bedbca0b09e826b4.png)
如果在函数内部创建同名变量，该变量将是**局部变量**，只能在函数内部使用。具有相同名称的全局变量将保持原样，全局且具有原始值。

```c
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)
```

返回为：
![在这里插入图片描述](https://img-blog.csdnimg.cn/2cb34546817648e4acfd9b48e6187f55.png)
**全局关键字**
通常，当您在函数内部创建变量时，该变量是局部的，并且只能在该函数内部使用。要在函数内创建全局变量，可以使用 global关键字。

```c
x = "帅哥"

def myfunc():
  global x
  x = "菜鸟"

myfunc()

print("川川" + x)
```

返回为：
![在这里插入图片描述](https://img-blog.csdnimg.cn/0c274d234ff6428cbdaaeb3a124b96ff.png)

## 6. 练习题

  1. 创建一个名为的变量carname并为其赋值菜鸟。
  2. 创建一个名为的变量x并为其赋值60。
  3. 5 + 10使用两个变量x和y。显示，打印它们的总和
  4. 创建一个名为的变量z，x=8,y=9,分配x + y给它，并显示结果。

# 六、Python数据类型

## 1.置数据类型

默认情况下，Python 具有以下内置数据类型，在这些类别中：

```c
文本类型：	str
数字类型：	int, float, complex
序列类型：	list, tuple, range
映射类型：	dict
套装类型：	set, frozenset
布尔类型：	bool
二进制类型：	bytes, bytearray, memoryview
```

此时你大可不必知道这些类型到底是什么，在后续的深入中，你一定会用得到，所以是需要记住的。

## 2.获取数据类型

您可使用以下**type()函数**获取**任何**对象的数据类型。
例如，打印变量 x 的数据类型：

```c
x = 6
print(type(x))
```

我们可以看到返回为：int类型
![在这里插入图片描述](https://img-blog.csdnimg.cn/39f9b340ecd442a3b59308b36e05fe67.png)

## 3.设置数据类型

在 Python 中，数据类型是在为变量赋值时设置的。
例如以下例子。
str字符串：

```c
x = "Hello World"
print(x)
print(type(x)) 
```

int整形：

```c
x1 = 6
print(type(x1))
```

float浮点类型：

```c
x2 = 6.5
print(type(x2))
```

complex复数类型：

```c
x3 = 2j
print(x3)
print(type(x3))
```

list列表类型：

```c
x4 = ["apple", "banana", "cherry"]
print(x4)
print(type(x4))
```

tuple元祖类型：

```c
x5 = ("apple", "banana", "cherry")
print(x5)
print(type(x5)) 
```

后面还有其它一些类型，我就不以完整代码形式演示了，直接以例子形式让大家看看什么样子是什么类型，当然如果你能亲自动手像我上面的例子一样进行操作打印看一看就再好不过了。
range范围类型

```c
x = range(6
```

dict字典类型

```c
x = {"name" : "John", "age" : 36}	
```

set集合类型：

```c
x = {"apple", "banana", "cherry"}
```

不常用的冻结集类型：

```c
x = frozenset({"apple", "banana", "cherry"})
```

bool布尔类型：

```c
x = True
```

不常用byte字节类型：

```c
x = b"Hello"
```

不常用bytearray字节数组类型：

```c
x = bytearray(5)
```

更有冷门到爆的memoryview内存试图类型

```c
x = memoryview(bytes(5))
```

## 4.设置特定数据类型

我会举一些例子说明，尽量很全，大可不必担心。先举一个完整例子，后面的是一样的打印就不演示了。
强调特定x为字符串：

```c
x = str("Hello World")
print(x)
print(type(x))
```

返回为：
![在这里插入图片描述](https://img-blog.csdnimg.cn/6d879abacfc845afb87292a790923caa.png)
强调x为整形：

```c
x = int(20)
```

强调x为浮点：

```c
x = float(20.5)
```

强调x为复数：

```c
x = complex(1j)
```

强调为列表

```c
x = list(("apple", "banana", "cherry"))
```

强调为元祖

```c
x = tuple(("apple", "banana", "cherry"))
```

强调为范围

```c
x = range(6)
```

强调为字典

```c
x = dict(name="John", age=36)
```

强调为集合

```c
x = set(("apple", "banana", "cherry"))
```

强调冻结集（没啥用的类型）

```c
x = frozenset(("apple", "banana", "cherry"))
```

强调布尔类型

```c
x = bool(5)
```

强调字节类型

```c
x = bytes(5)
```

强调字节组类型

```c
x = bytearray(5)
```

强调内存试图类型（又是没啥用的类型）

```c
x = memoryview(bytes(5))
```

## 6.练习题

回答下面的问题结果为什么类型？
1-

```c
x = 5
print(type(x))
```

2-

```c
x = "Hello World"
print(type(x))
```

3-

```c
x = 20.5
print(type(x))
```

4-

```c
x = ["apple", "banana", "cherry"]
print(type(x))
```

5-

```c
x = ("apple", "banana", "cherry")
print(type(x))
```

6-

```c
x = {"name" : "John", "age" : 36}
print(type(x))
```

7-

```c
x = True
print(type(x))
```

# 七、python数字

Python 共有三种数字类型：

 - int
 - float
 - complex
   三种类型分别对应如下例子：


```c
x = 1    # int
y = 2.8  # float
z = 1j   # complex
```

要验证 Python 中任何对象的类型，请使用以下type()函数：

```c
print(type(x))
print(type(y))
print(type(z))
```

因此你可以运行如下代码：

```c
x = 1    # int
y = 2.8  # float
z = 1j   # complex
print(type(x))
print(type(y))
print(type(z))
```

## 1.整数

Int 或 integer，是一个整数，正负，不带小数，长度不限。
例如：

```c
x = 1
y = 3562254887
z = -35522
print(type(x))
print(type(y))
print(type(z))
```

## 2.浮点数

浮点数或“浮点数”是包含一位或多位小数的正数或负数。
例如：

```c
x = 1.10
y = 1.0
z = -35.59
print(type(x))
print(type(y))
print(type(z))
```

浮点数也可以是带有“e”的科学数字，表示 10 的幂。
例如：

```c
x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))
```

## 3.虚数

复数写有“j”作为虚部。

```c
x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))
```

## 4.类型转换

比如你可以从一种类型转变成另一种同int()， float()和complex()方法。
例如：（你可以亲自运行一下）

```c
x = 1    # int
y = 2.8  # float
z = 1j   # complex


a = float(x)


b = int(y)


c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))
```

## 5.随机数

Python 有一个内置模块 random可以用来生成随机数。
示例：导入 random 模块，并显示 1 到 10之间的一个随机数：

```c
import random
print(random.randrange(1, 11))
```

## 6.练习题

1-插入正确的语法将 x 转换为浮点数。

```c
x = 5
x = _(x)
```

2-插入正确的语法以将 x 转换为整数。

```c
x = 5.5
x = _(x)
```

3-插入正确的语法以将 x 转换为复数。

```c
x = 5
x = _(x)
```

## 八、python指定变量类型

python 中的转换是使用构造函数完成的：

 - int() - 从整数文字、浮点文字（通过删除所有小数）或字符串文字（提供字符串表示整数）构造整数
 - float() - 从整数文字、浮点文字或字符串文字构造浮点数（提供字符串表示浮点数或整数）
 - str() - 从多种数据类型构造一个字符串，包括字符串、整数文字和浮点文字

我将每一个类型都举例子说明。
**整数**

```c
x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3
```

**浮点**

```c
x2 = float(1)     # x will be 1.0
y2 = float(2.8)   # y will be 2.8
z2 = float("3")   # z will be 3.0
w2 = float("4.2") # w will be 4.2
```

**字符串**

```c
x1 = str("s1") # x will be 's1'
y1 = str(2)    # y will be '2'
z1 = str(3.0)  # z will be '3.0'
```

# 九、Python字符串

## 一.字符串基本使用

### 1.字符串理解

python 中的字符串被单引号或双引号包围。'hello'与"hello"相同。您可以使用以下print()函数显示字符串文字：

```c
print("Hello")
print('Hello')
```

### 2.将字符串分配给变量

```c
a = "川川"
print(a)
```

### 3.多行字符串

您可以使用三个引号将多行字符串分配给变量：

```c
a = """从前有座山，
山里有座庙
庙里有个小和尚"""
print(a)
```

返回如下：
![在这里插入图片描述](https://img-blog.csdnimg.cn/13e8c413a3da49038f21921334d72ac3.png)
或三个单引号：

```c
a = '''从前有座山，
山里有座庙
庙里有个小和尚'''
print(a)
```

### 4.字符串是数组

Python 没有字符数据类型，单个字符只是一个长度为 1 的字符串。方括号可用于访问字符串的元素。这里用到了切片，你可以不懂。
获取位置 1 处的字符（记住第一个字符的位置为 0）：

```c
a = "Hello, World!"
print(a[1])
```

### 5.遍历字符串

循环遍历单词“chuanchuan”中的字母：

```c
for x in "chuanchuan":
  print(x)
```

### 6.字符串长度

len()函数返回字符串的长度，注意标点符号和空格也算一个长度：

```c
a = "Hello, World!"
print(len(a))
```

### 7.检查字符串

要检查字符串中是否存在某个短语或字符，我们可以使用关键字 in。

```c
txt = "The best things in life are free!"
print("free" in txt)
```

返回布尔类型(True代表有)：
![在这里插入图片描述](https://img-blog.csdnimg.cn/01d225d5655e408f94d853f7a3366b29.png)
也可以通过if来判断是否存在：

```c
txt = "The best things in life are free!"
if "free" in txt:
  print("是的, 'free'存在.")
```

### 8.检查如果不是

检查以下文本中是否不存在“川川”：

```c
txt = "川川就读上海交大!"
print("川川" not in txt)
```

因为存在，返回false:
![在这里插入图片描述](https://img-blog.csdnimg.cn/d5574c6df0bc4e1597735362cb0a3d8f.png)
仅在不存在“川川”时才打印：

```c
txt = "川川就读上海交大!"
if "川川" not in txt:
  print("No, '川川' 不在文档.")
```

因为不符合条件，所以不会打印。

## 二.切片字符串

### 1.切片

您可以使用切片语法返回一系列字符。指定开始索引和结束索引，以冒号分隔，以返回字符串的一部分。
示例：获取从位置 2 到位置 5 的字符（不包括在内）：

```c
b = "Hello, World!"
print(b[2:5])
```

返回为：
![在这里插入图片描述](https://img-blog.csdnimg.cn/796bd4586f6e449ea2e40d4a652359ff.png)
**注意**：第一个字符的索引为 0。

### 2.从头开始切片

示例：获取从开始到位置 5 的字符（不包括在内）：

```c
b = "Hello, World!"
print(b[:5])
```

返回为：
![在这里插入图片描述](https://img-blog.csdnimg.cn/add8aa002e6440f1b05f5e8735f09f81.png)

### 3.切到最后

通过省略结束索引，范围将到最后。
例如，获取从位置 2 到最后的字符：

```c
b = "Hello, World!"
print(b[2:])
```

返回：
![在这里插入图片描述](https://img-blog.csdnimg.cn/b625364d9a044bba9ccd46af50f78528.png)

### 4.负索引

使用负索引从字符串末尾开始切片，就是从右往左看，不再是从左往右看。
例如：

```c
b = "Hello, World!"
print(b[-5:-2])
```

返回为：
![在这里插入图片描述](https://img-blog.csdnimg.cn/df85f626d839467d9bafec41774ff048.png)

## 三.修改字符串

### 1.小写转大写

upper()方法以大写形式返回字符串：

```c
a = "Hello, World!"
print(a.upper())
```

返回为：
![在这里插入图片描述](https://img-blog.csdnimg.cn/df741ab91196485b8f88c40e2fa09b6c.png)

### 2.大写转小写

lower()方法以小写形式返回字符串：

```c
a = "Hello, World!"
print(a.lower())
```

返回为：
![在这里插入图片描述](https://img-blog.csdnimg.cn/4ea02a5c095e44ecaeb41a904c21b6c3.png)

### 3.删除空格

空白是实际文本之前和/或之后的空间，通常您想删除这个空间。
strip()方法从开头或结尾删除任何空格：

```c
a = " Hello, World! "
print(a.strip())
```

返回为：
![在这里插入图片描述](https://img-blog.csdnimg.cn/1117174003da48b983be3827569dc181.png)

### 4.替换字符串

replace()方法用另一个字符串替换一个字符串.

```c
a = "Hello, World!"
print(a.replace("H", "J"))
```

返回为：
![在这里插入图片描述](https://img-blog.csdnimg.cn/8bb859b2814845c08e8973f0d35a933c.png)

### 5.拆分字符串

split()方法返回一个列表，其中指定分隔符之间的文本成为列表项。split()如果找到分隔符的实例，该方法会将字符串拆分为子字符串。
例如我要将下面的字符串以逗号分隔：

```c
a = "Hello, World!"
print(a.split(","))
```

返回为：
![在这里插入图片描述](https://img-blog.csdnimg.cn/e52130d79f2d4918ad66ec088e6c7729.png)

##  四.字符串连接

要连接或组合两个字符串，您可以使用 + 运算符。
例如，将变量a与变量b, 合并到变量中c：

```c
a = "Hello"
b = "World"
c = a + b
print(c)
```

返回为：
![在这里插入图片描述](https://img-blog.csdnimg.cn/b997b12bd9ce49ed9b9b1728b5c5ed78.png)
例如要在a和b变量之间添加空格，请添加" "：

```c
a = "Hello"
b = "World"
c = a + " " + b
print(c)
```

返回为：
![在这里插入图片描述](https://img-blog.csdnimg.cn/63e1fd0df0dc4ce6b3d3731ca44ee418.png)

## 五.格式化字符串

### 1.format单个传参

我们不能像这样组合字符串和数字：

```c
#会报错
age = 20
txt =" 川川今年 " + age
print(txt)
```

但是我们可以通过使用**format()** 方法来组合字符串和数字！format()方法接受传递的参数，格式化它们，并将它们放在占位符所在的字符串中 {}。
例如，使用format()方法将数字插入字符串:

```c
age = 20
txt = "川川今年 {}"
print(txt.format(age))
```

返回为：
![在这里插入图片描述](https://img-blog.csdnimg.cn/7a5d777a49b74ed08e77f68289f7f436.png)

### 2.format多个个传参

format() 方法接受无限数量的参数，并放置在各自的占位符中：

```c
quantity = 20
itemno = 3000
price = 49.95
myorder = "川川今年 {}岁 买了个华为手机 {} 每个月花费 {} 元."
print(myorder.format(quantity, itemno, price))
```

返回为：
![在这里插入图片描述](https://img-blog.csdnimg.cn/dbe4564cdacb490fabc03a36a3cdaba4.png)
您可以使用索引号{0}来确保参数放置在正确的占位符中：

```c
quantity = 20
itemno = 3000
price = 49.95
myorder = "川川今年 {2}岁 买了个华为手机 {0} 每个月花费 {1} 元."
print(myorder.format(quantity, itemno, price))
```

这样就会导致数字传的顺序发生了变化，看看结果就明白了：
![在这里插入图片描述](https://img-blog.csdnimg.cn/949b564a95214be0bb8c7a0a1421ba31.png)

## 六. 字符串的其它处理方法总结

  1. capitalize() 将第一个字符转换为大写
  2. casefold() 将字符串转换为小写
  3. center() 返回一个居中的字符串
  4. count()	 返回指定值在字符串中出现的次数
  5. encode()  返回字符串的编码版本
  6. endswith() 如果字符串以指定的值结尾，则返回 true
  7. join()	 将可迭代的元素连接到字符串的末尾
  8. find() 在字符串中搜索指定值并返回找到它的位置
  9. format() 初始化字符串中的指定值
     10.index()  在字符串中搜索指定值并返回找到它的位置
      当然还有很多，个人感觉不是很常用，就不继续总结别的了。

## 七.练习题

1-使用 len 方法打印字符串的长度。

```c
x = "Hello World"
print(  )
```

2-获取字符串 txt 的第一个字符。

```c
txt = "Hello World"
x =
```

3.获取从索引 2 到索引 4 (llo) 的字符。

```c
txt = "Hello World"
x =
```

4.返回开头或结尾没有任何空格的字符串。

```c
txt = " Hello World "
x = 
```

**提示** 使用strip()
5-将 txt 的值转换为大写。

```c
txt = "Hello World"
txt =
```

6-将 txt 的值转换为小写。

```c
txt = "Hello World"
txt = 
```

7-用 J 替换字符 H。

```c
txt = "Hello World"
txt = txt.
```

8-插入正确的语法以添加年龄参数的占位符。

```c
age = 36
txt = "My name is John, and I am   "
print(txt.format(age))
```

提示：{}

# 十、Python布尔值

布尔值表示两个值之一： True或False。在编程中，您经常需要知道表达式是否为 True或False。举一些例子就明白了。

### 1.比较

当您比较两个值时，将计算表达式并且 Python 返回布尔值答案：

```c
print(10 > 9)
print(10 == 9)
print(10 < 9)
```

返回为：
![在这里插入图片描述](https://img-blog.csdnimg.cn/10e6905db0cf4865836177f013a11f6f.png)
在 if 语句中运行条件时，Python 返回 True or False：

```c
a = 100
b = 30

if b > a:
  print("b大于a")
else:
  print("b不大于a")
```

返回为：
![在这里插入图片描述](https://img-blog.csdnimg.cn/8d6c9ae6dea7494a9b24f3ee79c883c8.png)

### 2.评估值和变量

bool()函数允许您评估任何值，并给您 True或False 作为返回。
例如：评估一个字符串和一个数字

```c
print(bool("川川"))
print(bool(20))
```

返回为：
![在这里插入图片描述](https://img-blog.csdnimg.cn/e8c22d36a0d74415b20d90b7f130ed54.png)
评估两个变量：

```c
x = "川川"
y = 15

print(bool(x))
print(bool(y))
```

返回为：
![在这里插入图片描述](https://img-blog.csdnimg.cn/020bd6ba402e410ca9e453e590b57174.png)

### 3.布尔真值

True如果它具有某种内容，几乎任何值都会被评估。任何字符串都是True，空字符串除外。任何数字都是True，除了 0。任何列表、元组、集合和字典都是True，空的除外。
例如以下都会返回True:

```c
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])
```

### 4.布尔假值

实际上，False除了空值（例如()、 []、{}、 ""、 数字 0和 值 ）之外，计算为 的值 None。当然，结果为 False。

```c
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})
```

返回为：
![在这里插入图片描述](https://img-blog.csdnimg.cn/0a0fbe95c2f34fa09456871993e63bdb.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NjIxMTI2OQ==,size_16,color_FFFFFF,t_70)

### 5.函数可以返回布尔值

```c
def myFunction() :
  return True

print(myFunction())
```

返回为：
![在这里插入图片描述](https://img-blog.csdnimg.cn/ea1af825753d46148b07233ac728139e.png)
打印“YES！” 如果函数返回 True，否则打印“NO！”：

```c
def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")
```

Python 也有许多返回布尔值的内置函数，如 isinstance() 函数，可用于确定对象是否属于某种数据类型
例如：检查对象是否为整数

```c
x = 200
print(isinstance(x, int))
```

返回为
![在这里插入图片描述](https://img-blog.csdnimg.cn/78a0ce68ecde40f3b854533611e740f5.png)

### 6.练习题

1.回答下面的语句返回值True还是False:

```c
print(10 > 9)
```

2.回答下面的语句返回值True还是False:
`print(10 == 9)`

3.回答下面的语句返回值True还是False:

```c
print(10 < 9)
```

4.回答下面的语句返回值True还是False:

```c
print(bool("abc"))
```

5.回答下面的语句返回值True还是False:

```c
print(bool(0))
```

# 十一、python运算符

## 1.算术运算符

自己赋值粘贴运行下就懂了！
加减法：（+ -）

```c
a=2
b=3
c=a-b
d=a-b
print(c,d)
```

乘除法：（* /）

```c
a=(50-5*6)/4
print(a)

a=8/5
print(a)
```

取余数（同时与除法比较）

```c
'''/返回为float,//返回整数，%返回余数'''
a=17/3
print(a)


a=17//3
print(a)

a=5*3+2
print(a)
```

幂运算 （**'）

```c
'''幂运算  **'''
# a=4**2
# b=2**3
# print(a,b)
```

## 2.赋值运算符

等于（=）

```c
x = 5
print(x)
```

加等于（ +=）等效：	x = x + 

```c
x = 5
x += 3
print(x)
```

减等于（-=） 等效：x=x-

```c
x = 5
x -= 3
print(x)
```

类似的我们可以得到以下不同的方式等效：

```c
	x *= 3 等效	x = x * 3
```

```c
	x /= 3等效	x = x / 3
```

```c
	x %= 3	等效 x = x % 3
```

```c
	x //= 3	等效 x = x // 3
```

```c
	x **= 3	等效 x = x ** 3
```

```c
	x &= 3	等效 x = x & 3
```

```c
	x |= 3	等效 x = x | 3
```

```c
	x ^= 3	等效 x = x ^ 3
```

```c
	x >>= 3	等效x = x >> 3
```

```c
	x <<= 3	等效x = x << 3
```

# 十二、Python列表

## 一.列表基本知识

基本形式为：

```c
mylist = ["川川一号", "川川二号", "川川三号"]
```

### 1.创建列表

列表是使用方括号创建的：

```c
mylist = ["川川一号", "川川二号", "川川三号"]
print(mylist)
```

返回：
![在这里插入图片描述](https://img-blog.csdnimg.cn/86f039c8d1304a07810416fc982c888b.png)
创建新列表时也可以使用 **list()** 构造函数。

```c
thislist = list(("apple", "banana", "cherry"))
print(thislist)
```

**允许重复**
由于列表已编入索引，因此列表可以包含具有相同值的项目：

```c
thislist = ["川川一号", "川川二号", "川川三号","川川一号"]
print(thislist)
```

### 2.列出表值

列表项是有序的、可变的，并允许重复值。列表项被索引，第一项有索引[0]，第二项有索引[1]等等。
**单个索引**
例如我要索取川川一号：

```c
mylist = ["川川一号", "川川二号", "川川三号"]
print(mylist)
print(mylist[0])
```

返回：
![在这里插入图片描述](https://img-blog.csdnimg.cn/5d03bb804e604b599d7db4079a47fbd3.png)
**遍历列表**

```c
for i in mylist:
    print(i)
```

返回为：
![在这里插入图片描述](https://img-blog.csdnimg.cn/faf565e9d61b474aaeb6d8e5ed4ad4a8.png)

### 3.列表长度

确定列表有多少项，请使用以下 len()函数：

```c
thislist = ["川川一号", "川川二号", "川川三号","川川一号"]
print(len(thislist))
```

返回：
![在这里插入图片描述](https://img-blog.csdnimg.cn/78305e7738924925b4aedeb431101aba.png)

### 4.列表项 - 数据类型

列表项可以是任何数据类型。例如：

```c
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

print(list1)
print(list2)
print(list3)
```

### 5.Python 集合（数组）

  1. List列表是一个有序且可变的集合。允许重复成员。
  2. turple元组是一个有序且不可更改的集合。允许重复成员。
  3. Set集合是一个无序且无索引的集合。没有重复的成员。
  4. dict字典是一个有序*且可变的集合。没有重复的成员。
     ！！！从 Python 3.7 版开始，字典才是有序的！！！

## 二.访问列表

### 1.正常索引

列表项已编入索引，您可以通过引用索引号来访问它们：

```c
mylist = ["川川一号", "川川二号", "川川三号"]
print(mylist[0])
```

**注意**：第一项的索引为 0。

### 2.负索引

负索引意味着从头开始，-1指最后一项， -2指倒数第二项等。

```c
mylist = ["川川一号", "川川二号", "川川三号"]
print(mylist[-1])
```

### 3.索引范围

```c
mylist = ["川川一号", "川川二号", "川川三号"]
print(mylist[1:3])
```

### 4.负指数范围

```c
mylist = ["川川一号", "川川二号", "川川三号"]
print(mylist[-3:-1])
```

### 5.检查是否存在

要确定列表中是否存在指定的项目，请使用in关键字。
例如，检查列表中是否存在“apple”：

```c
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
```

## 三.更改列表

### 1.单个更改

要更改特定位置的值，需要通过索引号：

```c
mylist = ["川川一号", "川川二号", "川川三号","川川四号"]
mylist[0]="川川五号"
print(mylist[0])
```

修改成功：
![在这里插入图片描述](https://img-blog.csdnimg.cn/9188fe6359444b1fb4a392df390f4ad9.png)

### 2.多个更改

索引号需要用范围表示。

```c
mylist = ["川川一号", "川川二号", "川川三号","川川四号","川川五号"]
mylist[1:3]=["哈皮川川","憨批川川"]
print(mylist)
```

修改成功：
![在这里插入图片描述](https://img-blog.csdnimg.cn/512d201257134946a22ff82922317815.png)

### 3.插入列表

insert()方法在指定的索引处插入一个项目。

```c
mylist = ["川川一号", "川川二号", "川川三号","川川四号"]
mylist.insert(2,'帅哥呀')
print(mylist)
```

插入成功：
![在这里插入图片描述](https://img-blog.csdnimg.cn/747ce10e28ca45e9bc61366a00722d5c.png)

## 四.添加列表

### 1.末尾添加

要将值添加到列表的末尾，请使用append() 方法：

```c
mylist = ["川川一号", "川川二号", "川川三号","川川四号"]
mylist.append("憨批川川")
print(mylist)
```

添加成功：
![在这里插入图片描述](https://img-blog.csdnimg.cn/da75ff86ea104c95a4da5386567fd0a5.png)

### 2.指定位置添加

```c
mylist = ["川川一号", "川川二号", "川川三号","川川四号"]
mylist.insert(2,'川川菜鸟')
print(mylist)
```

添加成功：
![在这里插入图片描述](https://img-blog.csdnimg.cn/74026c5b04064f47abe39f4347295deb.png)

### 3.合并列表

要将另一个列表中的元素附加到当前列表，请使用extend()方法。

```c
mylist = ["川川一号", "川川二号", "川川三号","川川四号"]
mylist1 = ["川川一号", "川川二号", "川川三号","川川四号"]
mylist.extend(mylist1)
print(mylist)
```

合并成功：
![在这里插入图片描述](https://img-blog.csdnimg.cn/f51acb03a7ee42e9af2587e899747ffb.png)
extend()方法不一定要 列表，您也可以添加任何可迭代对象（元组、集合、字典等）。

```c
mylist = ["川川一号", "川川二号", "川川三号","川川四号"]
mylist2=("川川","菜鸟")
mylist.extend(mylist2)
print(mylist)
```

添加成功：
![在这里插入图片描述](https://img-blog.csdnimg.cn/721175685e5c480897c05c0583dc3be3.png)

## 五.删除列表

### 1.删除指定目标

remove()方法删除指定的项目。

```c
mylist = ["川川一号", "川川二号", "川川三号","川川四号"]
mylist.remove('川川二号')
print(mylist)
```

删除成功：
![在这里插入图片描述](https://img-blog.csdnimg.cn/281f15338fe34f71856c80ed721e5e83.png)

### 2.删除指定索引

pop()方法删除指定的索引。

```c
mylist = ["川川一号", "川川二号", "川川三号","川川四号"]
mylist.pop(2)
print(mylist)
```

删除成功：
![在这里插入图片描述](https://img-blog.csdnimg.cn/8e08f6f4d2aa4b3c86d410c1779deb87.png)
如果不指定索引，该pop()方法将删除最后一项。

```c
mylist = ["川川一号", "川川二号", "川川三号","川川四号"]
mylist.pop()
print(mylist)
```

删除成功：
![在这里插入图片描述](https://img-blog.csdnimg.cn/71dffe1b5d674f3bb48eb117447b0b62.png)

### 3.del删除指定的索引

```c
mylist = ["川川一号", "川川二号", "川川三号","川川四号"]
del mylist[0]
print(mylist)
```

删除成功：
![在这里插入图片描述](https://img-blog.csdnimg.cn/2c594ceea8144c76880b0cc30164816a.png)
该del关键字也可以完全删除列表。

```c
mylist = ["川川一号", "川川二号", "川川三号","川川四号"]
del mylist
```

### 4.清除列表

clear()方法清空列表。该列表仍然存在，但没有内容。

```c
mylist = ["川川一号", "川川二号", "川川三号","川川四号"]
mylist.clear()
print(mylist)
```

清空：
![在这里插入图片描述](https://img-blog.csdnimg.cn/3bca8e5afaf143dfb42db72706d3245f.png)

##  六.循环列表

### 1.for循环遍历

方法一：
循环遍历列表您可以使用循环遍历列表项for 。

```c
mylist = ["川川一号", "川川二号", "川川三号","川川四号"]
for i in mylist:
    print(i)
```

遍历成功：
![在这里插入图片描述](https://img-blog.csdnimg.cn/48c1f717a4124a419ba43f2c91028d5c.png)
方法二：遍历索引号

```c
mylist = ["川川一号", "川川二号", "川川三号","川川四号"]
for i in range(len(mylist)):
    print(mylist[i])
```

返回：
![在这里插入图片描述](https://img-blog.csdnimg.cn/40abe080deaa4841b7b5f94908338f89.png)

### 2.while循环遍历

```c
mylist = ["川川一号", "川川二号", "川川三号","川川四号"]
i = 0
while i < len(mylist):
  print(mylist[i])
  i = i + 1
```

返回：
![在这里插入图片描述](https://img-blog.csdnimg.cn/7a0d677372c444e095d11fedf122311c.png)

## 七.列表推导式

例如：根据fruits列表，您需要一个新列表，其中仅包含名称中带有字母“a”的fruits。
如果没有列表理解，您将不得不编写一个for带有条件测试的语句：

```c
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)
```

返回为：
![在这里插入图片描述](https://img-blog.csdnimg.cn/f58dcc19ccd84912a1b95b231b94fc9a.png)

使用列表推导式，你只需要一行代码即可！

```c
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)
```

返回一样：
![在这里插入图片描述](https://img-blog.csdnimg.cn/ad95fa69d91e4a9f92fec12c8b5bd117.png)
换一个例子，只接受小于 5 的数字：

```c
newlist = [x for x in range(10) if x < 5]
print(newlist)
```

返回“orange”而不是“banana”：（这个不是很好理解，多想想）

```c
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)
```

返回为：
![在这里插入图片描述](https://img-blog.csdnimg.cn/97c25f6f18b744f783b56d2f74c30b17.png)

## 八.列表排序

### 1.区分大小写的排序

默认情况下，该sort()方法区分大小写，导致所有大写字母都排在小写字母之前：

```c
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)
```

返回：
![在这里插入图片描述](https://img-blog.csdnimg.cn/da9f81614ee54515800ff59ec0ba66a1.png)

### 2.不区分大小写的排序

如果你想要一个不区分大小写的排序函数，使用 str.lower 作为键函数：

```c
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)
```

返回：
![在这里插入图片描述](https://img-blog.csdnimg.cn/d90cd674f3bc4678a0cc03e917df585c.png)

### 3.倒序

reverse()方法反转元素的当前排序顺序。

```c
mylist = ["川川一号", "川川二号", "川川三号","川川四号"]
mylist.reverse()
print(mylist)
```

返回为：
![在这里插入图片描述](https://img-blog.csdnimg.cn/caf7740e4d474abe9e94a8f0658d4f0e.png)

## 九.复制列表

copy()方法制作列表的副本：

```c
mylist = ["川川一号", "川川二号", "川川三号","川川四号"]
my = mylist.copy()
print(my)
```

返回：
![在这里插入图片描述](https://img-blog.csdnimg.cn/123eb074d9e043bfb48351bd8e3d6858.png)
list()方法制作列表的副本：

```c
mylist = ["川川一号", "川川二号", "川川三号","川川四号"]
my = list(mylist)
print(my)
```

返回为：
![在这里插入图片描述](https://img-blog.csdnimg.cn/7f37cfbc8365432bbb7b2d7d8a291491.png)

## 十.加入列表

最简单的方法之一是使用+ 运算符。

```c
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)
```

返回：
![在这里插入图片描述](https://img-blog.csdnimg.cn/73d269f72973482e9f178671a1c64d74.png)
稍微有意思点，连接两个列表的另一种方法是将 list2 中的所有项一个一个地附加到 list1 中：

```c
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)
```

返回：
![在这里插入图片描述](https://img-blog.csdnimg.cn/2b32a508055e46ae8efbd03716e703a0.png)
extend() 方法，其目的是将元素从一个列表添加到另一个列表：

```c
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)
```

返回：
![在这里插入图片描述](https://img-blog.csdnimg.cn/78e718c4dea74bbea0e5fe8dbfa392fd.png)

## 十一.列表所有操作总结

如果你英文好可以看看，当然，这些所有操作我都讲过一遍了。
![在这里插入图片描述](https://img-blog.csdnimg.cn/1712dbfb398b4485ae5c82ed2d389f9b.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NjIxMTI2OQ==,size_16,color_FFFFFF,t_70)

## 十二.练习

1-打印fruits列表中的第二项。

```c
fruits = ["apple", "banana", "cherry"]
print( )
```

2-将fruits列表中的值从“apple”改为“kiwi”。

```c
fruits = ["apple", "banana", "cherry"]
   =
```

3-使用 append 方法将“orange”添加到fruits列表中。

```c
fruits = ["apple", "banana", "cherry"]

```

4-使用插入方法将“柠檬”添加为fruits列表中的第二项。

```c
fruits = ["apple", "banana", "cherry"]
     ="lemon")
```

5-使用 remove 方法从fruits列表中删除“banana”。

```c
fruits = ["apple", "banana", "cherry"]

```

6-使用负索引打印列表中的最后一项。

```c
fruits = ["apple", "banana", "cherry"]
print（  ）
```

7-使用索引范围打印列表中的第三、第四和第五项。

```c
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[])
```

8-使用正确的语法打印列表中的项目数

```c
fruits = ["apple", "banana", "cherry"]
print( )
```

# 十三、Python元组

## 一.元组理解

### 1.1基本定义

元组用于在单个变量中存储多个项目。Tuple 是 Python 中用于存储数据集合的 4 种内置数据类型之一，其他 3 种是List、 Set和Dictionary，它们具有不同的性质和用法。元组是一个集合是有序的和不可改变的。元组是用圆括号写的。
基本形式如下：

```c
mytuple = ("川川一号", "川川二号", "川川三号")
print(mytuple)
```

元组项是**有序的、不可更改**的，并**允许重复**值。元组项被索引，第一项被索引[0]，第二项被索引[1]等。
允许**重复**举个例子：

```c
mytuple = ("川川一号", "川川二号", "川川三号",'川川一号')
print(mytuple)
```

**索引**举个例子：

```c
mytuple = ("川川一号", "川川二号", "川川三号")
# print(mytuple)
print(mytuple[0])
```

### 1.2元组长度

我们还是跟列表一样，用到len函数，例子如下：

```c
mytuple = ("川川一号", "川川二号", "川川三号",'川川一号')
# print(mytuple)
print(len(mytuple))
```

返回长度：
![在这里插入图片描述](https://img-blog.csdnimg.cn/82a74a8c75914de1baf530c4b6c18ae5.png)
**一项元组**，记住逗号，不然就不是元祖了！我将两个形式读写出来，可以做一个对比：

```c
mytuple = ("川川一号", )
print(type(mytuple))
mytuple = ("川川一号")
print(type(mytuple))
```

我们来看看返回什么：第一个是元祖，第二个是字符串。
![在这里插入图片描述](https://img-blog.csdnimg.cn/662350c0fa0b46cb957c24f97ed85808.png)

### 1.3数据类型

元组项可以是任何数据类型：字符串、整数和布尔数据类型.

```c
tuple1 = ("川川一号", "川川二号", "川川三号",'川川一号')
tuple2 = (1, 8, 5, 9, 3)
tuple3 = (True, False, False)
```

元组可以包含不同的数据类型。
包含字符串、整数和布尔值的元组，形式如下：

```c
tuple4 = ("川川一号", 34, True, 40, "帅哥")
```

使用tuple()来创建元组，形式如下：

```c
tuple5 = tuple(("川川一号", "川川二号", "川川三号",'川川一号'))
print(tuple5)
```

## 二.访问元组

### 2.1正常访问

您可以通过引用方括号内的索引号来访问元组项，比如打印第二项：

```c
mytuple = ("川川一号", "川川二号", "川川三号")
# print(mytuple)
print(mytuple[1])
```

**注意**：第一项的索引为 0。

### 2.2负索引

负索引意味着从头开始。-1指最后一项， -2指倒数第二项等。
例如打印元组的最后一项：

```c
mytuple = ("川川一号", "川川二号", "川川三号")
print(mytuple[-1])
```

### 2.3范围性索引

您可以通过指定范围的开始和结束位置来指定索引范围。指定范围时，返回值将是具有指定项的新元组。这里我们用到range函数，前面讲过。
返回第三、第四和第五项：

```c
mytuple = ("川川一号", "川川二号", "川川三号",'帅哥川川','川川真棒')
print(mytuple[2:5])
```

**注意**：搜索将从索引 2（包括）开始并在索引 5（不包括）处结束。
请记住，第一项的索引为 0。

通过**省略起始值**，范围将从第一项开始（自己打印看看）：

```c
mytuple = ("川川一号", "川川二号", "川川三号",'帅哥川川','川川真棒')
print(mytuple[:4])
```

通过**省略结束值**，范围将继续到列表的末尾：

```c
mytuple = ("川川一号", "川川二号", "川川三号",'帅哥川川','川川真棒')
print(mytuple[2:])
```

**负数范围**

```c
mytuple = ("川川一号", "川川二号", "川川三号",'帅哥川川','川川真棒')
print(mytuple[-4:-1])
```

**检查项目值是否存在**
要确定元组中是否存在指定的项目，请使用in关键字：

```c
thistuple = ("川川一号", "川川二号", "川川三号",'帅哥川川','川川真棒')
if "帅哥川川" in thistuple:
  print("哈哈, '帅哥川川' 在元祖列表")
```

返回：
![在这里插入图片描述](https://img-blog.csdnimg.cn/ff93b050eb9b46c699323268725a70c6.png)

## 三.更新元组

元组是不可更改的，这意味着一旦创建了元组，您就无法更改、添加或删除项目。但是有一些解决方法：将元组转换为列表，更改列表，然后将列表转换回元组。

### 3.1替换

比如我要将下面第二个元素改为帅哥：

```c
x = ("川川一号", "川川二号", "川川三号",'川川一号')
y = list(x)
y[1] = "帅哥"
x = tuple(y)
print(x)
```

返回为：
![在这里插入图片描述](https://img-blog.csdnimg.cn/b9a3d5a5c1084351943ccc5b749ef90e.png)

### 3.2添加项目值

由于元组是不可变的，它们没有内置 append()方法，但有其他方法可以向元组添加项。
**方法1**:转换为列表：就像更改元组的解决方法一样，您可以将其转换为列表，添加您的项目，然后将其转换回元组。
例如：将元组转换为列表，添加“爱你”，然后将其转换回元组：

```c
thistuple = ("川川一号", "川川二号", "川川三号",'川川一号')
y = list(thistuple)
y.append("爱你")
thistuple = tuple(y)
print(thistuple)
```

返回：
![在这里插入图片描述](https://img-blog.csdnimg.cn/71f8ec8aecfd4f4ba36aa849524663de.png)
方法2：将元组添加到元组。您可以向元组添加元组，因此如果您想添加一个（或多个）项目，请使用该项目创建一个新元组，并将其添加到现有元组中。
例如：创建一个值为“orange”的新元组，并添加该元组

```c
thistuple = ("川川一号", "川川二号", "川川三号",'川川一号')
y = ("爱你",)
thistuple += y
print(thistuple)
```

同样返回：
![在这里插入图片描述](https://img-blog.csdnimg.cn/877e8de13a2542fca3c6a9ab851ede40.png)
**注意**：创建只有一个item的元组时，记得在item后面加上逗号，否则不会被识别为元组。

### 3.3删除项目

注意：您不能删除元组中的项目。元组是不可更改的，因此您无法从中删除项目，但您可以使用与我们用于更改和添加元组项目相同的解决方法：

示例
将元组转换为列表，删除“apple”，然后将其转换回元组：

```c
thistuple = ("川川菜鸟", "川川二号", "川川三号",'川川一号')
y = list(thistuple)
y.remove("川川菜鸟")
thistuple = tuple(y)
print(thistuple)
```

或者您可以完全删除元组：该del关键字可以完全删除的元组

```c
this = ("川川菜鸟", "川川二号", "川川三号",'川川一号')
del this
print(this)
```

这就会返回错误，因为这个元祖已经不在了。
![在这里插入图片描述](https://img-blog.csdnimg.cn/6f3eec8913774bd292f91116ed95e577.png)

## 四.解包元组

当我们创建一个元组时，我们通常会为其分配值。这称为“打包”元组。
包装元组：

```c
fruits = ("apple", "banana", "cherry")
print(fruits)
```

但是，在 Python 中，我们也可以将值提取回变量中。这称为“解包”。
解包元组：

```c
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)
```

**使用星号***
如果变量的数量少于值的数量，您可以*在变量名中添加一个，值将作为列表分配给变量。
将其余值分配为名为“red”的列表：

```c
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)
```

如果星号被添加到另一个变量名而不是最后一个，Python 将为变量赋值，直到剩余的值数量与剩余的变量数量匹配。
添加值列表“tropic”变量：

```c
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)
```

## 五.循环元祖

### 5.1遍历元祖

也就是遍历元组的意思，只要我们提到遍历，那就是for循环。
**方法一**：直接遍历
例子如下：遍历项目并打印值

```c
thistuple = ("川川菜鸟", "川川二号", "川川三号",'川川一号')
for i in thistuple:
    print(i)
```

**方法二：** 遍历索引号
使用range()和len()函数创建合适的可迭代对象。

```c
thistuple = ("川川菜鸟", "川川二号", "川川三号",'川川一号')
for i in range(len(thistuple)):
    print(thistuple[i])
```

返回都i为：
![在这里插入图片描述](https://img-blog.csdnimg.cn/06803be67cf748cdba86ecc7b3383061.png)

### 5.2使用 While 循环

```c
thistuple = ("川川菜鸟", "川川二号", "川川三号",'川川一号')
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1
```

## 六.元组合并

合并两个元祖，我们用+连接即可。

```c
tuple1 = ("川川菜鸟", "川川二号", "川川三号",'川川一号')
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)
```

如果要将元组的内容乘以给定次数，可以使用* 运算符：

```c
tuple1 = ("川川菜鸟", "川川二号", "川川三号",'川川一号')
tuple4=tuple1*2
print(tuple4)
```

返回：
![在这里插入图片描述](https://img-blog.csdnimg.cn/eadc528736794e1db7132addbea6c84f.png)
count函数用于返回指定值次数：查找5出现次数

```c
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.count(5)
print(x)
```

返回：
![在这里插入图片描述](https://img-blog.csdnimg.cn/7bc89e8e865749169b75b7fac7a97714.png)

index()找出指定值并返回它的位置：查找元祖中8位置

```c
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.index(8)
print(x)
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/4c73f269500641dab8ce0a82825760c5.png)

## 七.练习

1-使用正确的语法打印fruits元组中的第一项

```c
fruits = ("apple", "banana", "cherry")
print
```

2-使用正确的语法打印fruits元组中的项目数。

```c
fruits = ("apple", "banana", "cherry")
print
```

3-使用负索引打印元组中的最后一项。

```c
fruits = ("apple", "banana", "cherry")
print
```

4-使用一系列索引打印元组中的第三、第四和第五项。

```c
fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(fruits[])
```

# 十四、Python集合

## 一.集合理解

基本形式：

```c
myset = {"川川一号", "川川二号", "川川三号"}
```

集合是用大括号写的。
创建一个集合：

```c
myset = {"川川一号", "川川二号", "川川三号"}
print(myset)
```

返回：
![在这里插入图片描述](https://img-blog.csdnimg.cn/acc7949313214a1690d93a0fe72254f2.png)
**注意**：集合是无序的，因此您无法确定项目的显示顺序。

## 二.访问集合

### 2.1遍历集合

您不能通过引用索引或键来访问集合中的项目。但是您可以使用循环遍历集合项for ，或者使用in关键字询问集合中是否存在指定的值 。
例如：

```c
myset = {"川川一号", "川川二号", "川川三号"}
for i in myset:
    print(i)
```

返回：
![在这里插入图片描述](https://img-blog.csdnimg.cn/c85b0c99b2fa4b77a5549a4723987556.png)

### 3.2检查是否存在

检查集合中是否存在“串串一号”：（显然不在）

```c
myset = {"川川一号", "川川二号", "川川三号"}
print('串串一号' in myset)
```

返回布尔值：
![在这里插入图片描述](https://img-blog.csdnimg.cn/f4dc1821c4c5468d8073f610175f141d.png)

## 三.添加集合

### 3.1添加项目值

创建集合后，您无法更改其项目，但可以添加新项目。要将一项添加到集合中，请使用add() 方法。
例如：添加川川菜鸟到集合中

```c
myset = {"川川一号", "川川二号", "川川三号"}
myset.add('川川菜鸟')
print(myset)
```

返回：
![在这里插入图片描述](https://img-blog.csdnimg.cn/d2b039067a86419da44d2ca5b3894f33.png)

### 3.2添加集合

要将另一个集合中的项目添加到当前集合中，请使用update() 方法。
例如将myset1添加到myset中：

```c
myset = {"川川一号", "川川二号", "川川三号"}
myset1 = {"川川一号", "川川二号", "川川三号",'川川菜鸟'}
myset.update(myset1)
print(myset)
```

返回：
![在这里插入图片描述](https://img-blog.csdnimg.cn/7b4314f3cc0249efa24cc1aed8755050.png)
为什么?别忘了我们的集合不能重复，重复的集合会被覆盖，因此只添加了新的值进来。

### 3.3添加任何可迭代对象

update()方法中的对象不一定是集合，它可以是任何可迭代对象（元组、列表、字典等）。
例如：将myset2列表加入集合myset1

```c
myset1 = {"川川一号", "川川二号", "川川三号",'川川菜鸟'}
myset2=['菜鸟','川川']
myset.update(myset2)
print(myset)
```

返回为：
![在这里插入图片描述](https://img-blog.csdnimg.cn/80960e2edb48456c8a63aee5690b5ead.png)

## 四.移除集合项

### 4.1remove方法

要删除集合中的项目，请使用remove()、 或discard()方法。
例如我要移除川川菜鸟：

```c
myset4 = {"川川一号", "川川二号", "川川三号",'川川菜鸟'}
myset4.remove('川川菜鸟')
print(myset4)
```

返回：
![在这里插入图片描述](https://img-blog.csdnimg.cn/74b9ebe7aa8e4966b483235406c1be9d.png)
**注意**：如果要删除的项目不存在，remove()将引发错误。

### 4.2discard() 方法

使用以下discard() 方法删除“川川菜鸟” ：

```c
myset4 = {"川川一号", "川川二号", "川川三号",'川川菜鸟'}
myset4.discard('川川菜鸟')
print(myset4)
```

返回：
![在这里插入图片描述](https://img-blog.csdnimg.cn/d2b4ea1a5fff440fa7dd68d0bb13fb6b.png)
**注意**：如果要删除的项目不存在，discard()则 不会引发错误。

### 4.3pop() 方法

使用以下pop() 方法删除最后一项：

```c
myset4 = {"川川一号", "川川二号", "川川三号",'川川菜鸟'}
myset4.pop()
print(myset4)
```

返回：
![在这里插入图片描述](https://img-blog.csdnimg.cn/6e4f314a4b71469aa9a61fedfcf7f9fc.png)
**注意**：集合是无序的，因此在使用该pop()方法时，您不知道哪个项目被删除。

### 4.4clear() 方法

clear() 方法清空集合：

```c
myset4 = {"川川一号", "川川二号", "川川三号",'川川菜鸟'}
myset.clear()
print(myset4)
```

打印为空。

### 4.5del关键字

该del关键字将完全删除该集合：

```c
myset4 = {"川川一号", "川川二号", "川川三号",'川川菜鸟'}
del myset4
```

集合已经不存在了，因此我们不打印。

## 五.循环集合

for循环遍历即可

```c
myset4 = {"川川一号", "川川二号", "川川三号",'川川菜鸟'}
for i in myset4:
    print(i)
```

返回：
![在这里插入图片描述](https://img-blog.csdnimg.cn/29855bbdfb82437499f3b0278786de0e.png)

## 六.集合连接

### 6.1普通连接

您可以使用union()返回包含两个集合中所有项的新集合的方法，或将一个集合中的所有项update()插入另一个集合的方法。
方法一：使用union()方法返回一个包含两个集合中所有项目的新集合

```c
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)
```

方法二：update()方法将 set2 中的项插入到 set1 中

```c
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)
```

**注意**：无论union()和update() 将排除任何重复的项目。

### 6.2仅保留重复项

intersection_update()方法将只保留两个集合中都存在的项目。
保留myset4和myset5重复项：

```c
myset4 = {"川川一号", "川川二号", "川川三号",'川川菜鸟'}
myset5 = {"川川一号", "川川五号", "川川三号",'川川菜鸟'}
myset4.intersection_update(myset5)
print(myset4)
```

或者用intersection()方法将返回一个新集合，该集合仅包含两个集合中都存在的项目。

```c
myset4 = {"川川一号", "川川二号", "川川三号",'川川菜鸟'}
myset5 = {"川川一号", "川川五号", "川川三号",'川川菜鸟'}
myset4.intersection(myset5)
print(myset4)
```

### 6.3保留所有，但不保留重复项

symmetric_difference_update()方法将只保留两个集合中都不存在的元素。

```c
myset4 = {"川川一号", "川川二号", "川川三号",'川川菜鸟'}
myset5 = {"川川一号", "川川五号", "川川三号",'川川菜鸟'}
myset4.symmetric_difference_update(myset5)
print(myset4)
```

返回：
![在这里插入图片描述](https://img-blog.csdnimg.cn/3a38491801df4c4eae0696b8cc039efa.png)
symmetric_difference()方法将返回一个新集合，该集合仅包含两个集合中都不存在的元素。

```c
myset4 = {"川川一号", "川川二号", "川川三号",'川川菜鸟'}
myset5 = {"川川一号", "川川五号", "川川三号",'川川菜鸟'}
myset4.symmetric_difference(myset5)
print(myset4)
```

## 七.练习

1-检查fruits集中是否存在“appl”。

```c
fruits = {"apple", "banana", "cherry"}
if "apple"   fruits:
  print("Yes, apple is a fruit!")
```

2-使用 add 方法将“orange”添加到fruits集中。

```c
fruits = {"apple", "banana", "cherry"}

```

3-使用正确的方法将多个项目（more_fruits）添加到fruits 集中。

```c
fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)#答案
```

4-使用 remove 方法从fruits 集中删除“banana。

```c
fruits = {"apple", "banana", "cherry"}

```

5-使用discard方法从fruits 集中删除“香蕉”。

```c
fruits = {"apple", "banana", "cherry"}

```

# 十五、Python字典

## 一.字典理解

基本形式：

```c
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
```

字典用于在键值对中存储数据值。字典是有序*、可变且不允许重复的集合。（从 Python 3.7 版开始，字典是有序的。在 Python 3.6 及更早版本中，字典是无序的。）

### 1.1创建字典与访问

字典是用大括号写的，有键和值。
创建并打印字典：

```c
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
```

字典项是有序的、可变的，并且不允许重复。字典项以键值对的形式呈现，可以使用键名进行引用。
例如打印brand的值

```c
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])
```

字典不能有两个具有相同键的项目：重复值将覆盖现有值
返回：
![在这里插入图片描述](https://img-blog.csdnimg.cn/b87beb1c6de84aa18916719969a360a9.png)

### 1.2字典长度

还是用用len函数

```c
hisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(len(thisdict))
```

### 1.3数据类型

字典项中的值可以是任何数据类型：
例如：

```c
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
```

类型：dict()
打印字典的数据类型：

```c
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(type(thisdict))
```

补充巩固：
![在这里插入图片描述](https://img-blog.csdnimg.cn/e505069070754184ae9a6695c6371db7.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_Q1NETiBA5bed5bed6I-c6bif,size_30,color_FFFFFF,t_70,g_se,x_16)

## 二.访问字典

### 2.1访问键名

您可以通过引用方括号内的键名来访问字典的项目：

```c
thisdict = {
  "name": "川川",
  "address": "上海",
  "year": 2000
}
x = thisdict["name"]
print(x)
```

还有一个被调用的方法get()会给你同样的结果：

```c
thisdict = {
  "name": "川川",
  "address": "上海",
  "year": 2000
}
x = thisdict["name"]
y=thisdict.get('name')
print(x)
print(y)
```

返回：
![在这里插入图片描述](https://img-blog.csdnimg.cn/283fa97d655c4db7b73c49892c97e29e.png)

### 2.2访问健值

keys()方法将返回字典中所有键的列表。

```c
hisdict = {
  "name": "川川",
  "address": "上海",
  "year": 2000
}
x = thisdict.keys()
print(x)
```

向原始字典**添加**一个新项目，并看到键列表也得到更新：

```c
thisdict = {
  "name": "川川",
  "address": "上海",
  "year": 2000
}
thisdict['age']=20
print(thisdict)
```

返回：
![在这里插入图片描述](https://img-blog.csdnimg.cn/a6f930e5eabc4c5c8080e12104a6d0af.png)
**获取值**
values()方法将返回字典中所有值的列表。

```c
x = thisdict.values()
```

items()方法将返回字典中的每个项目，作为列表中的元组。

```c
thisdict = {
  "name": "川川",
  "address": "上海",
  "year": 2000
}
thisdict['age']=20
print(thisdict)
x = thisdict.items()
print(x)
```

返回元祖：
![在这里插入图片描述](https://img-blog.csdnimg.cn/02b4b8a9041a4737bac9adf292977664.png)
要确定字典中是否存在指定的键，请使用in关键字：

```c
hisdict = {
  "name": "川川",
  "address": "上海",
  "year": 2000
}
if 'name' in thisdict:
    print('name在字典')
```

返回：
![在这里插入图片描述](https://img-blog.csdnimg.cn/afa9e11e6074420889df6f4d1b8828f2.png)

## 三.更改字典各种方法

前面我们讲到了一部分更改内容，这里我们具体讲一下。
例如我要把川川改为川川菜鸟：

```c
thisdict = {
  "name": "川川",
  "address": "上海",
  "year": 2000
}
thisdict['name'] = '川川菜鸟'
print(thisdict)
```

返回：
![在这里插入图片描述](https://img-blog.csdnimg.cn/6682fb216d08467a94f49788575dd43e.png)

或者我们使用update()方法：

```c
thisdict = {
  "name": "川川",
  "address": "上海",
  "year": 2000
}
thisdict.update({'name':'川川菜鸟'})
print(thisdict)
```

效果一样：
![在这里插入图片描述](https://img-blog.csdnimg.cn/e387f4f304f3498184c32f16881d5fdc.png)

## 四.添加字典项各种方法

比如我要添加一个年龄为20：

```c
thisdict = {
  "name": "川川",
  "address": "上海",
  "year": 2000
}
thisdict['age']=20
print(thisdict)
```

返回：![在这里插入图片描述](https://img-blog.csdnimg.cn/7ca3fddcf9c243e2bc0df1db65ea370b.png)

或者还是使用update:

```c
thisdict = {
  "name": "川川",
  "address": "上海",
  "year": 2000
}
thisdict['age']=20
print(thisdict)
thisdict.update({'age':'20岁'})
print(thisdict)
```

返回：
![在这里插入图片描述](https://img-blog.csdnimg.cn/bb73cb2ffdd049c98bd60c321627fa8d.png)

## 五.删除字典的各种方法

pop()方法删除具有指定键名的项。
比如我要删除地址项目：

```c
thisdict = {
  "name": "川川",
  "address": "上海",
  "year": 2000
}
thisdict.pop("address")
print(thisdict)
```

返回：
![在这里插入图片描述](https://img-blog.csdnimg.cn/e5e3a007e23541618ee1ca27a624f97b.png)

popitem()方法删除最后插入的项目（在 3.7 之前的版本中，将删除随机项目）：

```c
thisdict = {
  "name": "川川",
  "address": "上海",
  "year": 2000
}
thisdict.pop("address")
print(thisdict)
thisdict.popitem()
print(thisdict)
```

返回：
![在这里插入图片描述](https://img-blog.csdnimg.cn/9bc65c1c8d1d4ffbac10b0d4ee64a9f5.png)

del关键字删除与指定键名称的项目：

```c
thisdict = {
  "name": "川川",
  "address": "上海",
  "year": 2000
}
del thisdict['name']
print(thisdict)
```

返回：
![在这里插入图片描述](https://img-blog.csdnimg.cn/9d3fbc72b55c4404816adecb66c9693a.png)

del关键字也可以删除字典完全：

```c
del thisdict
```

clear()方法清空字典：

```c
thisdict = {
  "name": "川川",
  "address": "上海",
  "year": 2000
}
thisdict.clear()
print(thisdict)
```

返回空：
![在这里插入图片描述](https://img-blog.csdnimg.cn/67c794439ec04d1fb61be72a4fdd53a7.png)

## 六.遍历字典

将字典中的所有键名，一一打印出来：

```c
thisdict = {
  "name": "川川",
  "address": "上海",
  "year": 2000
}
for x in thisdict:
  print(x)
```

一一打印字典中的所有值：

```c
thisdict = {
  "name": "川川",
  "address": "上海",
  "year": 2000
}
for x in thisdict:
  print(thisdict[x])

```

返回：
![在这里插入图片描述](https://img-blog.csdnimg.cn/f34fc65c4a114c88b0947ca604ff474c.png)
您还可以使用该values()方法返回字典的值：

```c
thisdict = {
  "name": "川川",
  "address": "上海",
  "year": 2000
}
for x in thisdict.values():
  print(x)
```

您可以使用该keys()方法返回字典的键：

```c
hisdict = {
  "name": "川川",
  "address": "上海",
  "year": 2000
}
for x in thisdict.keys():
  print(x)
```

返回：
![在这里插入图片描述](https://img-blog.csdnimg.cn/a06b84d9abff4f02a5251b71d9600202.png)
使用以下 方法循环遍历keys和valuesitems()：

```c
thisdict = {
  "name": "川川",
  "address": "上海",
  "year": 2000
}
for x, y in thisdict.items():
  print(x, y)
```

返回：
![在这里插入图片描述](https://img-blog.csdnimg.cn/455f3dabb3d54865901bf7cc849b2dd0.png)

## 七.复制字典

用copy()函数

```c
thisdict = {
  "name": "川川",
  "address": "上海",
  "year": 2000
}
mydict=thisdict.copy()
print(mydict)
```

内置dict(）函数

```c
thisdict = {
  "name": "川川",
  "address": "上海",
  "year": 2000
}
mydict=dict(thisdict)
print(mydict)
```

效果都一样：
![在这里插入图片描述](https://img-blog.csdnimg.cn/7a8d876d92cc4d709ed06e8cd051151e.png)

## 八.嵌套字典

创建一个包含三个字典的字典：

```c
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamily)
```

返回：
![在这里插入图片描述](https://img-blog.csdnimg.cn/2b775bdbc83449e398dbef33f2698d3d.png)
创建三个字典，然后创建一个包含其他三个字典的字典：

```c
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}
print(myfamily)
```

效果一样：
![在这里插入图片描述](https://img-blog.csdnimg.cn/4c55319b19ec4cdfaf2dd177f46cd4f5.png)

## 九.练习

1-使用get方法打印汽车字典的“model”键的值。

```c
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print
```

2-将“year”值从 1964 更改为 2020。

```c
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

```

3-将键/值对 "color" : "red" 添加到汽车字典中。

```c
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

```

4-使用 pop 方法从汽车字典中删除“model”。

```c
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

```

5-使用clear方法清空car字典。

```c
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

```

# 十六、If ... Else语句

Python 支持数学中常见的逻辑条件：

 - 等于：a == b
 - 不等于：a != b
 - 小于：a < b
 - 小于或等于：a <= b
 - 大于：a > b
 - 大于或等于：a >= b

## 一.if语句

```c
a = 33
b = 200
if b > a:
  print("b 大于 a")
```

返回：
![在这里插入图片描述](https://img-blog.csdnimg.cn/878b478c7f94453a8bc2f25cbec27f31.png)
**注意**:if后面要有冒号
在这个例子中，我们使用两个变量a和b，它们用作 if 语句的一部分来测试b是否大于a。由于a是33，而b是200，我们知道 200 大于 33，所以我们打印到屏幕上“b 大于 a”。

## 二.缩进

Python 依靠缩进（行首的空格）来定义代码中的范围。为此，其他编程语言通常使用大括号。
If 语句，没有缩进（会引发错误）：

```c
a = 33
b = 200
if b > a:
print("b 大于 a")
```

## 三.elif语句

如果前面的条件是不正确的，那就试试这个条件。
例如：

```c
a = 33
b = 33
if b > a:
  print("b 大于 a")
elif a == b:
  print("a 等于b")
```

返回：
![在这里插入图片描述](https://img-blog.csdnimg.cn/9345cc2c3c5d48d4877abf6d7693d193.png)

在这个例子中a等于b，所以第一个条件不成立，但elif条件成立，所以我们打印到屏幕“a 和 b 相等”

## 四.else语句
### 4.1基本else

在其他关键字捕获任何未通过前面的条件抓获。

```c
a = 200
b = 33
if b > a:
  print("b 大于 a")
elif a == b:
  print("a 等于b")
else:
  print("a 小于 b")
```

返回：
![在这里插入图片描述](https://img-blog.csdnimg.cn/be75c187a15e4f7fb02709be7e288c72.png)
在这个例子中a大于b，所以第一个条件不成立，elif条件也不成立，所以我们转到else条件并打印到屏幕“a 小于 b”。

你也可以有一个else没有 elif：

```c
a = 200
b = 33
if b > a:
  print("b 大于 a")
else:
  print("b 小于 a")
```

### 4.2and语句
测试 if   a是否大于 b，并且 if     c 大于a：
```c
a = 200
b = 33
c = 500
if a > b and c > a:
  print("两种条件都满足")
```
### 4.3or 语句
测试 if  a是否大于 b，或 if   a 大于c：
```c
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")
```
### 4.4嵌套if语句

```c
x = 41
if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")
```
### 4.4pass语句
if语句不能为空，但如果您出于某种原因有一个if没有内容，pass语句请放入该语句以避免出错。

```c
a = 33
b = 200

if b > a:
  pass
```
# 十七、while循环语句
## 一.基本理解
使用while循环，只要条件为真，我们就可以执行一组语句。
例如：只要 i 小于 6 就打印 i

```c
i = 1
while i < 6:
  print(i)
  i += 1
```
返回为：
![在这里插入图片描述](https://img-blog.csdnimg.cn/14e55ef2832742c1bb32a30302abfd28.png)
**注意**：记住要限制 i，否则循环将永远持续下去。
## 二.中断声明
使用break语句，即使 while 条件为真，我们也可以停止循环：
例如当 i 为 3 时退出循环：

```c
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1
```
返回：
![在这里插入图片描述](https://img-blog.csdnimg.cn/78079ceeb9784cdd8f939001cbda9d71.png)

## 三.continue 声明
使用continue语句，我们可以停止当前的迭代，并继续下一个：

```c
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
```
返回：可以并没有打印3
![在这里插入图片描述](https://img-blog.csdnimg.cn/97479b5c3a514dd081f94b3c4f99aa91.png)
## 四.else 语句
使用else语句，当条件不再为真时，我们可以运行一次代码块：
一旦条件为假，打印一条消息：

```c
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")
```
# 十八、for循环语句
## 一.基本遍历
使用for循环，我们可以执行一组语句，对列表、元组、集合等中的每个项目执行一次。
例如：打印水果列表中的每个水果

```c
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
```
## 二.遍历字符串
例如循环遍历单词“banana”中的字母：

```c
for x in "banana":
  print(x)
```
## 三.中断声明
使用break语句，我们可以在循环遍历所有项目之前停止循环.
例如当x是“banana”时退出循环：

```c
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

```
当x是“banana”时退出循环，但这次中断出现在打印之前：

```c
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)
```
就会返回只有applr:
![在这里插入图片描述](https://img-blog.csdnimg.cn/4b09ae5dbf00421796cb4ab9cf2c9acc.png)
## 四.continue 声明
使用continue语句，我们可以停止循环的当前迭代，并继续下一个：
不要打印banana：

```c
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

```
## 五.range() 函数
要循环一组代码指定的次数，我们可以使用range()函数，的范围（）函数返回由1个数字，通过默认从0开始，并递增的顺序（缺省），并结束在指定次数。
例如：
```c
for x in range(6):
  print(x)
```
返回：
![在这里插入图片描述](https://img-blog.csdnimg.cn/3c98afbedeb041e1b4cb985ef33a167e.png)
**注意** range(6)不是 0 到 6 的值，而是 0 到 5 的值。
range函数默认被1至递增序列，但是有可能通过增加第三参数指定增量值：range（2，30，3）
## 六.嵌套循环
嵌套循环是循环内的循环。“内循环”将在“外循环”的每次迭代中执行一次。
为每个fruits打印每个形容词：
```c
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)
```
返回：
![在这里插入图片描述](https://img-blog.csdnimg.cn/db9d8a6845c3434ebc19a66b87677f17.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_Q1NETiBA5bed5bed6I-c6bif,size_24,color_FFFFFF,t_70,g_se,x_16)
## 七.pass语句
for循环不能为空，但如果由于某种原因有一个for没有内容的循环，请放入pass语句以避免出错。

```c
for x in [0, 1, 2]:
  pass
```
# 十九、函数
## 一.创建函数与调用
在 Python 中，函数是使用def 关键字定义的：

```c
def my_function():
  print("Hello from a function")
```
**调用函数**
要调用函数，请使用函数名称后跟括号：

```c
def my_function():
  print("川川菜鸟")
my_function()
```
返回：
![在这里插入图片描述](https://img-blog.csdnimg.cn/97d6ee5e947a4ae9b88fd39eb46c3aee.png)
## 二.参数
信息可以作为参数传递给函数。参数在函数名后的括号内指定。您可以根据需要添加任意数量的参数，只需用逗号分隔它们。

下面的示例有一个带一个参数 (fname) 的函数。当函数被调用时，我们传递一个名字，在函数内部使用它来打印全名：

```c
def my_function(fname):
  print(fname + " 菜鸟")

my_function("川川")
my_function("川川吗")
my_function("憨批")
```
返回：
![在这里插入图片描述](https://img-blog.csdnimg.cn/2ec46a81c80142979e635c08c8dfb926.png)
## 三.参数数量
默认情况下，必须使用正确数量的参数调用函数。这意味着如果您的函数需要 2 个参数，则必须使用 2 个参数调用该函数，不能多也不能少。

例如此函数需要 2 个参数，并获得 2 个参数：

```c
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("川川", "菜鸟")
```
返回：
![在这里插入图片描述](https://img-blog.csdnimg.cn/04b887581c834f7eabca564cd5b8128e.png)
## 四.任意参数，*args
如果您不知道将传递给函数的参数有多少，请*在函数定义中的参数名称前添加一个。这样，该函数将接收一个参数元组，并可以相应地访问这些项目。

如果参数数量未知，则*在参数名称前添加一个：

```c
def my_function(*kids):
  print("川川帅哥 " + kids[2])
my_function("名字", "性别", "菜鸟")
```
返回：
![在这里插入图片描述](https://img-blog.csdnimg.cn/ad4f2945e867491cad3f217f445b1b12.png)
## 五.关键字参数
您还可以使用key = value语法发送参数。这样，参数的顺序就无关紧要了。

```c
def my_function(child3, child2, child1):
  print("最帅的是 " + child3)

my_function(child1 = "大白", child2 = "小白", child3 = "猪猪侠")
```
返回：
![在这里插入图片描述](https://img-blog.csdnimg.cn/f6069d98fbeb401792bb4c193f19607a.png)

短语关键字参数在 Python 文档中通常缩写为kwargs。
## 七.任意关键字参数，**kwargs
如果您不知道有多少关键字参数将被传递到您的函数中，请**在函数定义中的参数名称之前添加两个星号。这样，该函数将接收一个参数字典，并可以相应地访问这些项目.
例如：
```c
def my_function(**kid):
  print("它的名字是 " + kid["lname"])

my_function(fname = "菜鸟", lname = "川川")
```
返回：
![在这里插入图片描述](https://img-blog.csdnimg.cn/02fac1a1e0704e3d9eeec9ad0e569e34.png)
## 八.默认参数值
如果我们不带参数调用函数，它使用默认值：

```c
def my_function(country = "Norway"):
  print("I am from " + country)
my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")
```
返回：
![在这里插入图片描述](https://img-blog.csdnimg.cn/9d2b196eae424cb89f732c8f96cd6d86.png)
## 九.将列表作为参数传递
例如，如果你发送一个 List 作为参数，当它到达函数时它仍然是一个 List：

```c
def my_function(food):
  for x in food:
    print(x)
fruits = ["apple", "banana", "cherry"]
my_function(fruits)
```
返回：
![在这里插入图片描述](https://img-blog.csdnimg.cn/2c25901fc7974f799f4cfa0997ba2968.png)
## 十.返回值
要让函数返回值，请使用以下return 语句：

```c
ef my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))
```
## 十一.pass语句
function定义不能为空，但如果您出于某种原因有一个function没有内容的定义，请放入pass语句中以避免出错。

```c
def myfunction():
  pass
```
# 二十、lambda
lambda 函数是一个小的匿名函数。一个 lambda 函数可以接受任意数量的参数，但只能有一个表达式。
语法：
`lambda arguments : expression
`
执行表达式并返回结果：

示例将 10 添加到 argument a，并返回结果：

```c
x = lambda a : a + 10
print(x(5))
```
返回：
![在这里插入图片描述](https://img-blog.csdnimg.cn/4eb10ffee5364c719ee3733248578248.png)
Lambda 函数可以接受任意数量的参数。
例将参数a与参数 相乘b并返回结果：

```c
x = lambda a, b : a * b
print(x(5, 6))
```
返回：
![在这里插入图片描述](https://img-blog.csdnimg.cn/35ac69bf4b854d469ba7aeaceceaa9d6.png)
把参数a、 b和c并返回结果：

```c
x = lambda a, b, c : a + b + c
print(x(5, 6, 2))
```
返回：
![在这里插入图片描述](https://img-blog.csdnimg.cn/89bc1de6ef1b40dcad467ed716bb9596.png)
假设您有一个接受一个参数的函数定义，并且该参数将乘以一个未知数：

```c
def myfunc(n):
  return lambda a : a * n
```
使用该函数定义来创建一个函数，该函数始终将您发送的数字加倍：

```c
def myfunc(n):
  return lambda a : a * n
mydoubler = myfunc(2)
print(mydoubler(11))
```
使用相同的函数定义来创建一个始终将您发送的数字增加三倍的函数：

```c
def myfunc(n):
  return lambda a : a * n

mytripler = myfunc(3)

print(mytripler(11))
```
# 二十一、数组
 Python 没有对数组的内置支持，但可以使用Python 列表代替。
 例如：
```c
chuan = ["川川", "菜鸟", "帅哥"]
```
## 一.访问数组的元素
您可以通过引用索引号来引用数组元素。例如：

```c
chuan = ["川川", "菜鸟", "帅哥"]
te=chuan[0]
print(te)
```
修改数组：

```c
chuan = ["川川", "菜鸟", "帅哥"]
chuan[0]='高富帅'
print(chuan)
```
返回：![在这里插入图片描述](https://img-blog.csdnimg.cn/4a06fdd98a6f41518868924ffc0103d7.png)

## 二.数组的长度
用len函数。
例如：

```c
chuan = ["川川", "菜鸟", "帅哥"]
chuan[0]='高富帅'
# print(chuan)
print(len(chuan))
```
## 三.修改数组
补充一点：循环数组元素，您可以使用for in循环遍历数组的所有元素。
例如：

```c
chuan = ["川川", "菜鸟", "帅哥"]
for i in chuan:
    print(i)
```

**添加数组元素**
使用append函数（跟列表一样）

```c
chuan = ["川川", "菜鸟", "帅哥"]
chuan.append('上海')
print(chuan)
```
返回：
![在这里插入图片描述](https://img-blog.csdnimg.cn/2dc8194f6fad4e22a96fc6b71a3d20be.png)
 **删除数组元素**
 您可以使用该pop()方法从数组中删除一个元素。（注意起始位置是0）
 例如删除第二个元素：
```c
chuan = ["川川", "菜鸟", "帅哥"]
chuan.pop(1)
print(chuan)
```
返回：
![在这里插入图片描述](https://img-blog.csdnimg.cn/5fec18098ea94702b4c396ef1ca8fbcc.png)
您还可以使用该remove()方法从数组中删除一个元素。

```c
chuan = ["川川", "菜鸟", "帅哥"]
chuan.pop(1)
print(chuan)
chuan.remove('帅哥')
print(chuan)
```
返回：
![在这里插入图片描述](https://img-blog.csdnimg.cn/6f4687037c364aef88d8e040ef1380e5.png)
**注意**：列表的remove()方法只删除指定值的第一次出现。
## 四.数组的其它操作
![在这里插入图片描述](https://img-blog.csdnimg.cn/1a366b94e1e04424b6d7a88286749a27.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_Q1NETiBA5bed5bed6I-c6bif,size_40,color_FFFFFF,t_70,g_se,x_16)
# 二十二、Python类和对象
Python 类/对象。Python 是一种面向对象的编程语言。Python 中的几乎所有东西都是一个对象，有它的属性和方法。类就像一个对象构造函数，或者是创建对象的“蓝图”。
## 一.创建类
要创建一个类，请使用关键字**class**。
例如：创建一个名为 MyClass 的类，其属性名为 x

```c
class MyClass:
  x = 5
print(MyClass)
```

## 二.创建对象
现在我们可以使用名为 MyClass 的类来创建对象。
例如创建一个名为 p1 的对象，并打印 x 的值：

```c
class MyClass:
  x = 5
p1 = MyClass()
print(p1.x)
```
返回：
![在这里插入图片描述](https://img-blog.csdnimg.cn/6b1e869957464d94b726b3b8a8ca93f7.png)
##  三.__init__() 函数
上面的例子是最简单形式的类和对象，在现实生活应用程序中并没有真正有用。要理解类的含义，我们必须了解内置的 __init__() 函数。所有类都有一个名为 __init__() 的函数，它总是在类被初始化时执行。使用 __init__() 函数为对象属性赋值，或在创建对象时需要执行的其他操作。

例如创建一个名为 Person 的类，使用 __init__() 函数为 name 和 age 赋值：

```c
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("川川菜鸟", 20)

print(p1.name)
print(p1.age)
```
返回：
![在这里插入图片描述](https://img-blog.csdnimg.cn/222d6731d2e1404db935a059a745d015.png)
注意：__init__()每次使用该类创建新对象时都会自动调用该函数。
## 四.对象方法
让我们在 Person 类中创建一个方法。
例如插入一个打印问候语的函数，并在 p1 对象上执行它：

```c
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("我的名字是 " + self.name)

p1 = Person("川川菜鸟", 20)
p1.myfunc()
```
返回：
![在这里插入图片描述](https://img-blog.csdnimg.cn/f5a4e9033b654570831271514f0b9bc4.png)
## 五.自参数
self参数是对类当前实例的引用，用于访问属于该类的变量。它不必命名self，您可以随意调用它，但它必须是类中任何函数的第一个参数：

```c
lass Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("我的名字是 " + abc.name)

p1 = Person("川川菜鸟", 20)
p1.myfunc()
```
跟使用self效果一样
![在这里插入图片描述](https://img-blog.csdnimg.cn/f139a3ff4103428f8a1540de2a16fa80.png)
## 六.对象及其属性更改
**替换**
例如修改年龄为21
```c
class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("我的名字是 " + abc.name)

p1 = Person("川川菜鸟", 20)
p1.age = 21
print(p1.age)
```
返回：
![在这里插入图片描述](https://img-blog.csdnimg.cn/c334df98e42a4f62b4f3d303c988c7ea.png)
**删除对象属性**
例如从 p1 对象中删除 age 属性：

```c
lass Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)
p1 = Person("John", 36)
del p1.age
print(p1.age)#没有了自然打印报错
```
**删除对象**
比如删除对象p1

```c
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)

del p1

print(p1)#对象都不在了肯定报错
```
## 七.pass语句
class定义不能为空，但如果您出于某种原因有一个class没有内容的定义，请放入pass语句中以避免出错。

```c
class Person:
  pass
```
# 二十三、Python继承
继承允许我们定义一个从另一个类继承所有方法和属性的类。父类是被继承的类，也称为基类。子类是从另一个类继承的类，也称为派生类。

## 一.创建父类
任何类都可以是父类，因此语法与创建任何其他类相同：
这里创建一个名为Person、 firstname和lastname属性的类，以及一个printname方法：

```c
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)


x = Person("川川", "菜鸟")
x.printname()
```
返回：
![在这里插入图片描述](https://img-blog.csdnimg.cn/a6226e395309488eb6aefae01d3de4e0.png)
## 二.创建子类
创建从另一个类继承功能的类，请在创建子类时将父类作为参数发送。
例如：创建一个名为 的类Student，它将继承该类的属性和方法Person

```c
class Student(Person):
  pass
```
**注意：** pass 当您不想向类添加任何其他属性或方法时，请使用关键字。
现在 Student 类具有与 Person 类相同的属性和方法。使用Student类创建对象，然后执行printname方法：

```c
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  pass

x = Student("川川", "菜鸟")
x.printname()

```
返回还是一样
![在这里插入图片描述](https://img-blog.csdnimg.cn/f483366149444ce8b977e7d16e24dbad.png)

## 三.添加 __init__() 函数
到目前为止，我们已经创建了一个继承父类的属性和方法的子类。我们想将__init__()函数添加到子类（而不是pass关键字）。
**注意**：__init__()每次使用该类创建新对象时都会自动调用该函数。
例如：将__init__()函数添加到 Student类中

```c
class Student(Person):
  def __init__(self, fname, lname):
```
添加__init__()函数后，子类将不再继承父类的__init__()函数。注：孩子的__init__() 功能覆盖父母的继承 __init__()功能。为了保持父__init__() 函数的继承，添加对父函数的调用__init__()：

```c
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)

x = Student("川川", "菜鸟")
x.printname()
```
这样效果一样：
![在这里插入图片描述](https://img-blog.csdnimg.cn/99ab2e59900340ff963ab35c8291d49e.png)

## 四.使用 super() 函数
Python 还有一个super()函数可以让子类继承其父类的所有方法和属性：

```c
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)

x = Student("川川", "菜鸟")
x.printname()
```
一样返回：
![在这里插入图片描述](https://img-blog.csdnimg.cn/385cd39d9b0b487e8792105a1f03056e.png)
通过使用该super()函数，您不必使用父元素的名称，它会自动从其父元素继承方法和属性。

## 五.添加属性
添加一个属性调用graduationyear到 Student类：

```c
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    self.graduationyear = 2021

x = Student("川川", "菜鸟")
print(x.graduationyear)

```
返回：
![在这里插入图片描述](https://img-blog.csdnimg.cn/662b6ca490c04e02a3c147119dd413ea.png)
年份2019应该是一个变量，并Student在创建学生对象时传递给 类。为此，请在 __init__() 函数中添加另一个参数。
添加year参数，并在创建对象时传递正确的年份：

```c
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

x = Student("川川", "菜鸟", 2021)
print(x.graduationyear)
```
返回一样为2021
## 六.添加方法
添加一个调用welcome到 Student类的方法：

```c
lass Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = Student("川川", "菜鸟", 2021)
x.welcome()
```
返回
![在这里插入图片描述](https://img-blog.csdnimg.cn/66f484fda4fe4a9ea10a09d4f05b2553.png)
# 二十四、Python日期
Python 中的日期不是它自己的数据类型，但我们可以导入一个名为的模块datetime来处理日期作为日期对象。
## 一.日期输入输出
导入 datetime 模块并显示**当前日期**：

```c
import datetime

x = datetime.datetime.now()
print(x)
```
返回：
![在这里插入图片描述](https://img-blog.csdnimg.cn/bde824aaebb54da986d2ff211aa05a48.png)
**日期输出**
当我们执行上面示例中的代码时，结果将是：2021-08-25 05:36:01.704218
日期包含年、月、日、小时、分钟、秒和微秒。

回工作日的年份和名称：

```c
import datetime

x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))
```
返回：
![在这里插入图片描述](https://img-blog.csdnimg.cn/e13bde5ef431411f8aac67a4caa8d53f.png)
## 二.创建日期对象
要创建日期，我们可以使用模块的datetime()类（构造函数） datetime。本datetime()类需要三个参数来创建日期：年，月，日。

```c
import datetime

x = datetime.datetime(2021, 8, 25)

print(x)
```
返回
![在这里插入图片描述](https://img-blog.csdnimg.cn/e1e7d9e8a0b84fd9a056cad61f069521.png)

datetime()类也需要参数的时间和时区（小时，分钟，秒，微秒，tzone），但它们是可选的，并且具有一个默认值0，（None对时区）。

## 三.strftime() 方法
该datetime对象具有将日期对象格式化为可读字符串的方法。该方法被调用strftime()，并采用一个参数 format，来指定返回字符串的格式。
例如显示月份名称：

```c
import datetime
x = datetime.datetime(2011, 8, 25)
print(x.strftime("%B"))
```
返回
![在这里插入图片描述](https://img-blog.csdnimg.cn/8eec8d0ace7b41fba97a5e40e6251ce4.png)
## 四.其它调用方法
实在太多，不能一一演示，大家自己看下。
![在这里插入图片描述](https://img-blog.csdnimg.cn/0c6f641c3f51488d95862cd45b16efde.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_Q1NETiBA5bed5bed6I-c6bif,size_36,color_FFFFFF,t_70,g_se,x_16)

![在这里插入图片描述](https://img-blog.csdnimg.cn/ce5fa6ebdada4e11812337f5e5311c08.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_Q1NETiBA5bed5bed6I-c6bif,size_36,color_FFFFFF,t_70,g_se,x_16)
![在这里插入图片描述](https://img-blog.csdnimg.cn/3d60a5b8038e41408847abad07ab82bb.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_Q1NETiBA5bed5bed6I-c6bif,size_37,color_FFFFFF,t_70,g_se,x_16)
# 二十五、Python JSON
JSON 是一种用于存储和交换数据的语法。JSON 是文本，用 JavaScript 对象表示法编写。
Python 有一个名为 的内置包json，可用于处理 JSON 数据。
导入 json 模块：
```c
import json
```
## 一.从 JSON 转换为 Python
如果您有 JSON 字符串，则可以使用json.loads()方法对其进行解析 。
结果将是一个Python 字典。
例如：
```c
import json
# some JSON:
x ='{ "name":"川川", "age":20, "city":"上海"}'

# 解析x
y = json.loads(x)
#会返回字典
print(y["age"])
```
返回：
![在这里插入图片描述](https://img-blog.csdnimg.cn/76bc4a2200c547878844af2daab4cada.png)

如果您有 Python 对象，则可以使用json.dumps()方法将其转换为 JSON 字符串。

```c
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
```
返回为
![在这里插入图片描述](https://img-blog.csdnimg.cn/0c197483e6db42d9b0c2664fcb213f28.png)
# 二十六、异常处理
try块可让您测试代码块的错误。except块可让您处理错误。finally无论 try- 和 except 块的结果如何，该块都允许您执行代码。
##  一.异常处理
例如该try块将产生异常，因为x未定义：

```c
try:
  print(x)
except:
  print("An exception occurred")
```
返回![在这里插入图片描述](https://img-blog.csdnimg.cn/909001a9594b4d76b453752ca2e6b6c8.png)

由于 try 块引发错误，因此将执行 except 块。如果没有 try 块，程序将崩溃并引发错误。
## 二.else搭配
else如果没有出现错误，您可以使用关键字来定义要执行的代码块：

```c
try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")
```
返回：
![在这里插入图片描述](https://img-blog.csdnimg.cn/fac6e6ffce6845f09a1aae4d4dae17ac.png)
## 三.finally语句
finally如果指定了该块，则无论 try 块是否引发错误，都将执行该块。
例如：

```c
try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")
```
返回：
![在这里插入图片描述](https://img-blog.csdnimg.cn/a68dbd8098544a6da2aa5eb4b0fb66f8.png)
这对于关闭对象和清理资源很有用。
例如尝试打开并写入不可写的文件：

```c
try:
  f = open("demofile.txt")
  f.write("Lorum Ipsum")
except:
  print("Something went wrong when writing to the file")
finally:
  f.close()
```
程序可以继续，而无需打开文件对象。
## 四.引发异常
要抛出（或引发）异常，请使用raise关键字。
例如如果 x 小于 0，则引发错误并停止程序：

```c
x = -1

if x < 0:
  raise Exception("Sorry, no numbers below zero")
```
返回：
![在这里插入图片描述](https://img-blog.csdnimg.cn/02540f4401c14b2cb5673c79a215bb12.png)
该raise关键字用于引发异常。您可以定义要引发的错误类型以及要打印给用户的文本。
例如如果 x 不是整数，则引发 TypeError：

```c
x = "hello"

if not type(x) is int:
  raise TypeError("Only integers are allowed")
```
返回
![在这里插入图片描述](https://img-blog.csdnimg.cn/25e0e84376354789a145dc37e276b76d.png)
# 二十七、用户输入
实在太简单了，就是使用一个input(),将输入后的值传递给另一个变量，相当于动态赋值、
例如：

```c
username = input("你叫什么名字:")
print("名字叫: " + username)
```
返回：
![在这里插入图片描述](https://img-blog.csdnimg.cn/ffaa0dfb0ab64d0ca2e638f98eabfb8d.png)
# 二十七.格式化输入输出
讲解在注释里面。
```c
'''在字符串开头的引号/三引号前添加 f 或 F 。在这种字符串中，可以在 { 和 } 字符之间输入引用的变量'''
# year = 2021
# event = 'Referendum'
# a=f'Results of the {year} {event}'
# print(a)
'''str.format() 该方法也用 { 和 } 标记替换变量的位置a  这种方法支持详细的格式化指令'''
# yes_votes = 42_572_654
# no_votes = 43_132_495
# percentage = yes_votes / (yes_votes + no_votes)
# a='{:-5} YES votes  {:1.1%}'.format(yes_votes, percentage)#调整{}内部感受下
# print(a)


'''只想快速显示变量进行调试，可以用 repr() 或 str() 函数把值转化为字符串。'''
# s = 'Hello, world.'
# print(str(s))#str() 函数返回供人阅读的值
# print(repr(s))#repr() 则生成适于解释器读取的值
# print(str(1/7))
# hellos = repr('hello')
# print(hellos)

'''7.1.1. 格式化字符串字面值'''
'''格式化字符串字面值 （简称为 f-字符串）在字符串前加前缀 f 或 F，通过 {expression} 表达式，把 Python 表达式的值添加到字符串内'''
'''下例将 pi 舍入到小数点后三位'''
# import math
# print(f'The value of pi is approximately {math.pi:.3f}.')
'''在 ':' 后传递整数，为该字段设置最小字符宽度，常用于列对齐'''
# table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
# for name, phone in table.items():
#     print(f'{name:10} ==> {phone:10d}')


'''7.1.2. 字符串 format() 方法'''
# print('We are the {} who say "{}!"'.format('knights', 'Ni'))
'''花括号及之内的字符（称为格式字段）被替换为传递给 str.format() 方法的对象。花括号中的数字表示传递给 str.format() 方法的对象所在的位置。'''
# print('{0} and {1}'.format('spam', 'eggs'))
# print('{1} and {0}'.format('spam', 'eggs'))
'''使用关键字参数名引用值。'''
# print('This {food} is {adjective}.'.format(food='spam', adjective='absolutely horrible'))
'''位置参数和关键字参数可以任意组合'''
# print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred',
#                                                        other='Georg'))

'''用方括号 '[]' 访问键来完成'''
# table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
# print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; ''Dcab: {0[Dcab]:d}'.format(table))
'''也可以用 '**' 符号，把 table 当作传递的关键字参数。'''
# print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))

'''生成一组整齐的列，包含给定整数及其平方与立方'''
# for x in range(1, 11):
#     print('{0:2d} {1:3d} {2:4d}'.format(x, x * x, x * x * x))


'''7.1.3. 手动格式化字符串'''
# for x in range(1, 11):
#     print(repr(x).rjust(2), repr(x * x).rjust(3), end=' ')
#     print(repr(x * x * x).rjust(4))

'''7.1.4. 旧式字符串格式化方法'''
# import math
# print('The value of pi is approximately %5.3f.' % math.pi)


'''7.2. 读写文件¶'''
'''最常用的参数有两个: open(filename, mode)'''
# f = open('workfile', 'w')
'''
第一个实参是文件名字符串第二个实参是包含描述文件使用方式字符的字符串。
mode 的值包括 'r' ，表示文件只能读取；'w' 表示只能写入（现有同名文件会被覆盖）；
'a' 表示打开文件并追加内容，任何写入的数据会自动添加到文件末尾。'r+' 表示打开文件进行读写。
mode 实参是可选的，省略时的默认值为 'r'。
'''
# with open('workfile') as f:
#     read_data = f.read()
#     print(read_data)
# f.close()#如果没有使用 with 关键字，则应调用 f.close() 关闭文件，即可释放文件占用的系统资源。

# with open('workfile') as f:
#     a=f.read()
#     print(a)
# f.close()

'''f.readline() 从文件中读取单行数据'''
# with open('workfile') as f:
   # a=f.readline()
   # b=f.readline()
   # c=f.readline()
   # print(a,b,c)
   # for i in f:
   #     print(i)
# f.close()

'''从文件中读取多行时，可以用循环遍历整个文件对象'''
# with open('workfile') as f:
#     for line in f:
#         print(line, end='')
# f.close()

'''f.write(string) 把 string 的内容写入文件，并返回写入的字符数。'''
# with open('workfile','w') as f:
#     f.write('This is a test\n')
# f.close()

'''写入其他类型的对象前，要先把它们转化为字符串（文本模式）或字节对象（二进制模式）'''
# with open('workfile','a') as f:
#     value = ('the answer', 42)
#     s = str(value)
#     f.write(s)
# f.close()

# f = open('workfile', 'rb+')
# f.write(b'0123456789abcdef')
# print(f.read())
# print(f.seek(5))
# print(f.read(1))

'''7.2.2. 使用 json 保存结构化数据'''
# import json
# a=json.dumps([1, 'simple', 'list'])
# print(a)
'''dumps() 函数还有一个变体， dump() ，它只将对象序列化为 text file '''
#如果 f 是 text file 对象
# json.dump(x, f)
#要再次解码对象，如果 f 是已打开、供读取的 text file 对象
# x = json.load(f)
© 2021 GitHub, Inc.
```
# 二十八.总结
本篇文章你大可当作一本书使用，也算是博主的一个温习，对于小白会是一个不错的手册。私人群: `970353786`。如果有时间，我会讲高阶的知识，比如文件处理，爬虫，数据分析，机器学习，有时间我都会再来继续讲下去，因为本篇文章已经讲完了所有基础知识。
博主创作实在不易，三连加个关注吧！但我更希望你能从本篇博客学有所获，后续我还会继续推出新的系类。
