#迭代是Python最强大的功能之一，<是访问集合元素的一种方式>
#迭代器有两个基本的方法：iter() 和 next()
#字符串，列表或元组对象都可用于创建迭代器
import sys         # 引入 sys 模块
list = [1,2,3,4,5]
str = "12345"
tuple = (1,2,3,4,5)
it = iter(list)
print(next(it)) 
print(next(it)) 
print(next(it)) 

list=[1,2,3,4]
it = iter(list)    # 创建迭代器对象
for x in it:
    print (x, end=" ")

    list=[1,2,3,4]
    it = iter(list)    # 创建迭代器对象
     
# while True:
#     try:
#         print (next(it))
#     except StopIteration:
#         pass
        # sys.exit()

# 创建一个迭代器
# 1.把一个类作为一个迭代器使用需要在类中实现两个方法 __iter__() 与 __next__() 
# Python 的构造函数为 __init__(), 它会在对象初始化的时候执行
# StopIteration 异常用于标识迭代的完成，防止出现无限循环的情况，
# 在 __next__() 方法中我们可以设置在完成指定循环次数后触发 StopIteration 异常来结束迭代。
print("-----创建一个迭代器------")
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a +=1
            return x
        else:
            raise StopIteration


myclass = MyNumbers()
myiter = iter(myclass)
for x in myiter:
    print(x)



#  生成器 generator 
    #使用了 yield 的函数被称为生成器（generator）

# TODO