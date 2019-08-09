#List（列表） 列表是写在方括号 [] 之间、用逗号分隔开的元素列表
list = [ 'abcd', 786 , 2.23, 'runoob', 70.2 ]
print(list)
#Tuple（元组） 组（tuple）与列表类似，不同之处在于元组的元素不能修改。元组写在小括号 () 里，元素之间用逗号隔开
tuple = ('123456',123456,20.23)
print(tuple)
#Set（集合）
    # 1.可以使用大括号 { } 或者 set() 函数创建集合
    # 2.创建一个<空集合>必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典
student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}
set1 = set("15154d5sd")
print(student,set1)   # 输出集合，重复的元素被自动去掉

#Dictionary（字典）
    # 列表是有序的对象集合，字典是无序的对象集合。两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取
    # 键(key)必须使用不可变类型。
dict = {}
dict['one'] = "1 - 菜鸟教程"
dict[2]     = "2 - 菜鸟工具"
tinydict = {'name': 'runoob','code':1, 'site': 'www.runoob.com'}
print(tinydict.keys(),tinydict.values())

#Python数据类型转换
    #将数据类型作为函数名即可

