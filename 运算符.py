#运算符
    #算术运算符
print("----算术运算符----")
a, b, c = 2, 2, "2"
# 加
print(a+b,a+int(c))
# 减
print(a-b,a-int(c))
# 乘
print(a*b,a*int(c))
# 除
print(a/b,a/int(c))
# 取模
print(a%b,a%int(c))
# 取整
print(a//b,a//int(c))
# 幂
print(a**b,a**int(c))

    #比较运算符
print("----比较运算符----")
a, b = 10, 5
print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)

    #赋值运算符
print("----赋值运算符----")
a, c = 2, 0
c = a; print(c)
c += a; print(c)
c -= a; print(c)
c *= a; print(c)
c /= a; print(c)
c %= a; print(c)
c **= a; print(c)
c //= a; print(c)
    #位运算符
print("----位运算符----")
    
    #逻辑运算符
a = 10
b = 20
print(a and b)
print(a or b)
print(not b)

    #成员运算符
    # 测试实例中包含了一系列的成员，包括字符串，列表或元组
    # in 和 not in
list = [1,2,3,4]
print(10 in list)

    #身份运算符 
    # 用于比较两个对象的存储单元
    # (is 与 == 区别：is 用于判断两个变量引用对象是否为同一个， == 用于判断引用变量的值是否相等。)
a = 20
b = 20
c = 10
print(a is b, a is c)

    # 运算符优先级
    