#ex3-3
#3.3.1
empty_tuple = ()
print(empty_tuple)

#创建元组细节，每个元素最后都要加逗号(,)
one_marx = 'Groucho',
print(one_marx)

one_marx01 = 'Groucho'
print(one_marx01)

marx_tuple = 'Groucho','Chico','Harpo'
print('marx_tuple:',marx_tuple)
marx_tuple01 = ['Groucho','Chico','Harpo']
print('marx_tuple01:',marx_tuple01)
marx_tuple02 = ('Groucho','Chico','Harpo')
print('marx_tuple02:',marx_tuple02)
print("---------------------------------")


#元组解包
marx_tuple = ('Groucho','Chico','Harpo')
a,b,c = marx_tuple
print('元组解包')
print('a:'+a+'\n'+'b:'+b+'\n'+'c:'+c)

marx_list = ['Groucho','Chico','Harpo']
print(tuple(marx_list))
