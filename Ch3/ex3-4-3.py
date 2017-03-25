#ex3-4-3
#使用 [key] 添加或修改元素

pyhtons = {
	'Chapman':'Graham',
	'Cleese':'John',
	'Idle':'Eric',
	'Jones':'Terry',
	'Palin':'Michael',
}

print('python:',pyhtons)

#insert
pyhtons['Gilliam'] = 'Gerry'
print('python:',pyhtons)

#modify
pyhtons['Gilliam'] = 'Terry'
print('python:',pyhtons)