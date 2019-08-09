# 数据结构
# 列表
# 将列表当做堆栈使用
stack = [3, 4, 5]
stack.append(6)
stack.append(7)
print(stack)

stack.pop()
stack.pop()
print(stack)

# 将列表当作队列使用
# 在列表的最后添加或者弹出元素速度快，然而在列表里插入或者从头部弹出速度却不快
# 效率不高

# 嵌套列表解析
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

a = [[row[i] for row in matrix] for i in range(4)]
print(a)

# 集合
# 字典
# 构造函数 dict() 直接从键值对<元组列表>中构建字典。如果有固定的模式，列表推导式指定特定的键值对：
dic = dict([('a', 1), ('b', 2), ('c', 3)])
print("字典:", dic)

# 遍历技巧
# items 关键字和对应的值    ---字典中遍历
# enumerate 索引位置和对应值  --- 序列中遍历
# zip() 同时遍历两个或更多的序列   --- 序列中遍历
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
list = [1, 2, 3, 4, 5, 6]
str = "yukimwoo"
for k, v in knights.items():
    print('items', k, v)
for k, v in enumerate(list):
    print('list', k, v)
for k, v in zip(list,str):
    print('zip', k, v)
