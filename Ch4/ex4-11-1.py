#ex4-11-1
short_list = [1,2,3]
position = 2
try:
	print(short_list[position])
except :
	print('Need a position between 0 and',len(short_list)-1,'but got',position)