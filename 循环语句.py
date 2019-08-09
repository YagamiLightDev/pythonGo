# 循环语句
# 1
# while expression:
#     pass

# 2 在 while … else 在条件语句为 false 时执行 else 的语句块：
# while expression:
#     pass
# else:
#     pass

# 3
# for target_list in expression_list:
#     pass
# 4
# for target_list in expression_list:
#     pass
# else:
#     pass

# range()函数 生成数列

print(range(5))

# break 语句可以跳出 for 和 while 的循环体。如果你从 for 或 while 循环中终止，任何对应的循环 else 块将不执行。
# continue语句被用来告诉Python跳过当前循环块中的剩余语句，然后继续进行下一轮循环。
for letter in 'Runoob':     # 第一个实例
    if letter == 'b':
       break
    #    continue
    print ('当前字母为 :', letter)
else:
    print('else')

#pass 语句 
    # pass是空语句，是为了保持程序结构的完整性。

