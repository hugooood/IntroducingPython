#ex4-11-2
short_list = [1,2,3]
while True:
	value = input('Position [q to quit]?')
	if value == 'q':
		break
	try:
		position = int(value)
		print(short_list[position])
	except IndexError as err:#索引错误
		print('Bad index:',position)
	except Exception as other:#其他错误
		print('Something else broke:',other)