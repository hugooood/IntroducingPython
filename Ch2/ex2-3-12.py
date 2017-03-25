#字符串函数二
#ex2-3-12

setup = 'a duck goes into abar...'
setup1 = '..a duck goes into abar...'

#1.原始字符串
print("1:",setup)

#2.原始字符串
#表面上是进行了删除操作，
#实际是将原字符串进行操作后得到的新字符串
print("2:",setup.strip('.'))


#同样操作的是复制后的字符串，对原字符串没影响
#3.将字符串首字母变大写
print("3:",setup.capitalize())
# print("原始字符串:",setup)
# print("当字符串首字符不为大写时，函数不起作用",setup1.capitalize())

#4.让所有单词的开头字母变成大写
print("4:",setup.title())
# print(setup1.title())

#5.让所有字母都变成大写
print("5:",setup.upper())

#6.将所有字母转换成小写
print("6:",setup.lower())

#7.将所有字母的大小写转换
print("7:",setup.swapcase())

#格式排版
#8.居中
print(setup.center(30))
#9.左对齐
print(setup.ljust(30))
#10.右对齐
print(setup.rjust(30))