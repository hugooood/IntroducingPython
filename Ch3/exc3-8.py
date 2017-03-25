#exc3-8.py
#第三章练习
#author:hugooood
#email:hugooood@outlook.com

# ex(1) to (3) 
print('--------------------------------------------')
year_list = [1980,1981,1982,1983,1984,1985]
age = int(input("Do you want to know the date of your birthday:"))
print("%d is your three years birthday "%year_list[age])
max_age = len(year_list)
print("The most of age in the list is date:",year_list[max_age-1])
print('--------------------------------------------')

# ex(4) to (7)
things = ['mozzarella','cinderella','salmonella']
things = ' '.join(things).split()
print(things)
#print(temple)
for name in things:
	if name == 'mozzarella':
		#注：capitalize是字符串方法
		things[things.index('mozzarella')]=things[things.index('mozzarella')].capitalize()
		#print(type(things[things.index('mozzarella')].capitalize()))
		print(things)
# 		temple = ','.join(things)
# 		print(temple.capitalize())
# 		things = temple.split(',')
# 		print(temple)
# 		print(things)
	elif name == 'cinderella':
		things[things.index('cinderella')]=things[things.index('cinderella')].upper()
		print(things)
	elif name == 'salmonella':
	 	del things[things.index('salmonella')]
	 	print(things)
	else:
		pass	

print('--------------------------------------------')

#ex(8)(9)
surprise = ['Groucho','Chico','Harpo']
print('原始:',surprise)
surprise[len(surprise)-1]=surprise[len(surprise)-1].lower()
print('最后一个元素变小写:',surprise)
surprise[len(surprise)-1]=surprise[len(surprise)-1][::-1]
print('翻转:',surprise)
surprise[len(surprise)-1]=surprise[len(surprise)-1].capitalize()
print('首字母大写:',surprise)

print('--------------------------------------------')


#(10) to (14)
e2f = {'dog':'chien',
		'cat':'chat',
		'walrus':'morse'}
print('e2f:',e2f)
print('walrus <e2f>:',e2f['walrus'])

#第一对v:k 是字典生成值，将得到的结果直接赋给字典发f2e
f2e = {v:k for k,v in e2f.items()}
print('f2e:',f2e)

print('chien <f2e>:',f2e['chien'])

set_e2f = set(e2f.keys())
print('set_e2f',set_e2f)

print('--------------------------------------------')

#(15) to (18)
life = {'animals':{'cats':['Henri','Grumpy','Lucy'],
					'octopi':' ',
					'emus':' '},
		'plants':' ',
		'others':' '
		}
# print(dict(life))
print('life top keys:',life.keys())
print(life['animals'].keys())
print(life['animals']['cats'])