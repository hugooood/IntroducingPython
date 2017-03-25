#ex3-4-4
#使用update()合并字典

pyhtons = {
	'Chapman':'Graham',
	'Cleese':'John',
	'Idle':'Eric',
	'Jones':'Terry',
	'Palin':'Michael',
}

print('pyhtons:',pyhtons)

others = {'Marx':'Groucho','Howard':'Moe'}

print('others:',others)

pyhtons.update(others)

print('After add others:',pyhtons)

#新值覆盖旧值
first = {'a':1,'b':2}
second = {'b':'platypus'}
first.update(second)
print(first)

#3-4-5
#使用 del 删除具有指定键的元素
print("--------------------------")
print(pyhtons)

del pyhtons['Marx']
print("del Marx:",pyhtons)

del pyhtons['Howard']
print("del Howard:",pyhtons)

print("--------------------------")

#3-4-6使用clear()删除所有元素
print(pyhtons)
#fun1
#pyhtons.clear()
#print(pyhtons)

#fun2
pyhtons = {}
print(pyhtons)

print("--------------------------")

#ex3-4-7
#使用 in 判断是否存在
pythons = {'Chapman': 'Graham', 'Cleese': 'John',
'Jones': 'Terry', 'Palin': 'Michael'}

print(pythons)
print('Chapman in pyhtons:','Chapman' in pythons)
print('Palin in pyhtons:','Palin' in pythons)

print("--------------------------")
#ex3-4-8
#使用[key]获取元素
print(pythons['Cleese'])

#先判断，在查询
if 'Marx' in pythons:
	print(pythons['Marx'])
else:
	print('Not a pyhton')

#或者使用get()方法查询
print(pythons.get('Marx'))

print("--------------------------")

#3-4-9
#使用 keys() 获取所有键
signals = {'green': 'go', 'yellow': 'go faster', 'red': 'smile for the camera'}
print(signals,'\n')

#使用keys()获取所有键
print(signals.keys())
print(list(signals.keys()),'\n')

#使用values()获取所有值
print(signals.values())
print(list(signals.values()),'\n')

print(signals.items())
print(list(signals.items()),'\n')

print("--------------------------")

#3-4-12
#使用=赋值,使用copy()复制
signals = {'green': 'go', 'yellow': 'go faster', 'red': 'smile for the camera'}
#对字典内容进行的修改会反映到所有与之相关联的变量名上
save_signals = signals
#创建一个副本
original_signals = signals.copy()

signals['blue'] = 'confuse everyone'
print(save_signals)
print(original_signals)