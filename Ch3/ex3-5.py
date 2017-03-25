#ex3-5.py
#使用set创建集合

empty_set = set()
print(empty_set)

even_numbers = {0,2,4,6,8}
print(even_numbers)

odd_numbers = {1,3,5,7,9}
print(odd_numbers)

#将字符串转换成集合
print(set('letters'))

#用元组建立集合
sot = set(('Ummagumma','Echoes','Atom Heart Mother'))
print(sot)

#用列表建立集合
sol = set(['Dasher','Dancer','Prancer','Mason-Dixon'])
print(sol)
print('------------------------------')
#3-5-3
#使用 in 测试值是否存在
drinks = {
	'martint':{'vodka','vermouth'},
	'black russian':{'vodka','kahlua'},
	'white russian':{'cream','kahlua','vodka'},
	'manhattan':{'rye','vermouth','bitters'},
	'screwdriver':{'orange juice','vodka'}
}

# for name,contents in drinks.items():
# 	if 'vodka' in contents:
# 		print(name)
print('Drinks:',drinks)
print('\n')

#打印所有种类的伏特加
print('All kind of vodka:')
for name,item in drinks.items():
	if 'vodka' in item:
		print(name,':',item)
print('\n')

#打印不含vermouth和cream的vodka
print('vodka without vermouth and cream:')
for name,contents in drinks.items():
	if 'vodka' in contents and \
	not('vermouth' in contents or \
		'cream' in contents):
		print(name)

#对上例的改写
for name,contents in drinks.items():
	if 'vodka' in contents and not contents & {'vermouth','cream'}:
		print(name)

bruss = drinks['black russian']
wruss = drinks['white russian']
print(bruss & wruss) # ‘&’ 求交集
print(bruss.intersection(wruss)) #同上

print(bruss | wruss) # '|' 求并集
print(bruss.union(wruss))# 同上	

print(bruss - wruss) #差集
print(bruss.difference(wruss)) #同上