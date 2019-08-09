# 定义函数使用 def 关键字，一般格式如下：

# def 函数名（参数列表）:
#     函数体

# 函数调用
# 函数名()

# 参数传递
# 以下是调用函数时可使用的正式参数类型：

# 必需参数
# 关键字参数
# 默认参数
# 不定长参数
# 加了星号 * 的参数会以元组(tuple)的形式导入，存放所有未命名的变量参数。
# 加了两个星号 ** 的参数会以字典的形式导入 <参数必须用关键字传入>
# 声明函数时，参数中星号 * 可以单独出现，<星号 * 后的参数必须用关键字传入>。


def funcname1(self, *parameter_list):
    print("输出:", self, parameter_list)


def funcname2(self, **parameter_list):
    print("输出:", self, parameter_list)


def funcname3(self, *, c):
    print("输出:", self, c)


# 调用函数
funcname1(1, 2, 3, 4)
funcname2(1, a=2, b=3, c=4)
funcname3(1, c=2)

# 匿名函数
# 匿名即不再使用 def 语句这样标准的形式定义一个函数

sum = lambda arg1, arg2: arg1 + arg2
print(sum(10, 20))

# return语句
    #return [表达式] 语句用于退出函数
    # 不带参数值的return语句返回None

def sum1(arg1, arg2):
    total = arg1 + arg2
    print("函数内:", total)
    return total

# 调用sum1函数
total = sum1(10, 20)
print("函数外：", total)

#变量作用域 L –> E –> G –>B 的规则查找
    # L （Local） 局部作用域
    # E （Enclosing） 闭包函数外的函数中
    # G （Global） 全局作用域
    # B （Built-in） 内置作用域（内置函数所在模块的范围）

import builtins
# print(dir(builtins))

#Python 中只有模块（module），类（class）以及函数（def、lambda）才会引入新的作用域，
# 其它的代码块（如 if/elif/else/、try/except、for/while等）是不会引入新的作用域的，
# 也就是说这些语句内定义的变量，外部也可以访问，

def test():
    if True:
        msg = "I am from Runoob"
    print(msg)

test()

# global

globalVar = 1
def fun1():
    global globalVar # 使用global关键字声明
    print("G", globalVar)
    globalVar =123
    print("L", globalVar)

fun1()
print("G", globalVar)