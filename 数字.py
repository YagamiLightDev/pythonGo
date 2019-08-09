import random
var1 = 1
var2 = 10
print(var1, var2)
del var1,var2

# int float complex
number16 = 0xFF #16进制
number8 = 0o37 #8进制
print(number16, number8)
cpx= complex(number8)
print(cpx)

#随机数函数
    #从序列的元素(列表，元组或字符串)中随机挑选一个元素
print(random.choice(range(10)))
print(random.choice([1,2,3,4,6]))
print(random.choice("123456"))
print(random.choice((1,2,3,4,5)))

print(random.randrange(22))