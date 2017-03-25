#ex3-2-6
#指定范围切片提取元素

marxes = ['Groucho','Chico','Harpo']

print(marxes)
#步长默认为1
print(marxes[0:2])

print(marxes[::2])

#实现逆序
print(marxes[::-1])

#append()实现尾增
marxes.append('Zeppo')
print("After append:",marxes)

#extend()可以将一个列表合并到另一个列表中
others = ['Gummo','karl']
marxes.extend(others)
print("After extend:",marxes)

#+=与extend具有相同效果
marxes += others
print("After += :",marxes)


marxes1 = ['Groucho','Chico','Harpo']

#insert()在指定位置插入元素			
marxes1.insert(3,'Gummo')
print("insert 'Gummo':",marxes1)
marxes1.insert(10,'karl')
print("insert 'karl':",marxes1)

#del删除指定位置的元素，不改变元素的位置
del  marxes1[-1]
print("After del:",marxes1)

marxes = ['Groucho','Chico','Harpo','Gummo','Zeppo']
print("marxes[2]:",marxes[2])
del marxes[2]
print("After del marxes[2]:",marxes[2])


#使用remove()删除具有指定值的元素,会改变元素的位置
marxes = ['Groucho','Chico','Harpo','Gummo','Zeppo']
print("原来的列表:",marxes)

marxes.remove('Gummo')
print("After remove:",marxes)

#如下语法是错误的示范
#print("After remove:",marxes.remove('Gummo'))

#使用pop获取并删除指定位置的元素
marxes = ['Groucho','Chico','Harpo','Zeppo']
#空参和-1都是删除最后的元素
#marxes.pop(-1)
marxes.pop()
print("After pop:",marxes)

print("marxes.pop(1)",marxes.pop(1))
print("After marxes.pop(1):",marxes)

#使用index()查询具有特定值的元素位置
marxes = ['Groucho','Chico','Harpo','Zeppo']
print("The 'Harpo' index is : ",marxes.index('Harpo'))

#使用in判断值是否存在
marxes = ['Groucho','Chico','Harpo','Zeppo']
print("'Groucho' in marxes :",'Groucho'in marxes)
print("'Bob' in marxes :",'Bob'in marxes)

print("---------------------------------")

#使用count()记录特定值出现的次数
marxes = ['Groucho','Chico','Harpo','Zeppo']
print("marxes.count('Harpo'):",marxes.count('Harpo'))
print("marxes.count('Bob'):",marxes.count('Bob'))

snl_skit = ['cheeseburger','cheeseburger','cheeseburger']
print("snl_skit.count('cheeseburger'):",snl_skit.count('cheeseburger'))
print("---------------------------------")

#重点方法	
#join()是一个字符串方法
marxes = ['Groucho','Chico','Harpo']
print("marxes[]->string_marxes:",','.join(marxes))
#下面例子方便理解join方法的使用
print("marxes[]->string_marxes:",'+'.join(marxes))

#join()与split()互逆  实现细节不是很懂  此坑带填
print("---------------------------------")
friends = ['Harry','Hermione','Ron']
separator = '*'
#以separator为分隔符将friends的所有元素合并成一个新字符串
joined = separator.join(friends)
print(joined)

#以separator为分隔符将joined的所有元素拆分成一个列表
separator = '*'
separator = joined.split(separator)
print("separator:",separator)

print("separator==friends",separator==friends)


print("---------------------------------")
marxes = ['Groucho','Chico','Harpo']

print("marxes:",marxes)

#sorted()是通用函数，则会返回排好序的列表副本，原列表内容不变。
print("After sorted():",sorted(marxes))

print("marxes:",marxes)

#sort()是列表方法，会对原列表进行排序，改变原列表内容。
#默认升序
#marxes = ['Groucho','Chico','Harpo']
marxes.sort(reverse = True)
print("After sort():",marxes)

print("marxes:",marxes)
print("---------------------------------")

#同一列表之间，能够自动地互相转换，也能进行排序
numbers = [2,1,4.0,3]
print(numbers)
numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)

print("---------------------------------")
#3.2.18
marxes = ['Groucho','Chico','Harpo']
print(len(marxes))


print("---------------------------------")
#3.2.19
#使用=赋值
a = [1,2,3]
print("a:",a)
b = a
print("b:",b)
a[0] = "surprise"
print("a[0]:",a[0])
print("a:",a)

b[0] = "I hate surprise"
print("b[0]:",b[0])
print("a:",a)


print("---------------------------------")
#使用copy()复制
a = [1,2,3]
b = a.copy()
c = list(a)
d = a[:]
print('\n','a:',a,
	'\n','b:',b,
	'\n','c:',c,
	'\n','d:',d
	)
a[0] = 'integer lists are boring'
print('\n','a:',a)
print('\n','b:',b)
print('\n','c:',c)
print('\n','d:',d)