#ex3-2-2

#字符串转列表
print(list('cat'))

#元组转换成列表
a_tuple = ('ready','fire','aim')
print(list(a_tuple))

#split() 可以依据分隔符将字符串切割成由若干子串组成的列表
birthday = '1/6/1952'
print(birthday.split('/'))

splitme = 'a/b//c/d///e'
splitme.split('//')