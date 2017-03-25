#字符串函数一:
#ex2-3-11
poem = '''All that doth flow we cannot liquid name
Or else would fire and water be the same;
But that is liquid which is moist and wet
Fire that property can never get.
Then 'tis not cold that doth the fire put out
But 'tis the wet that makes it die, no doubt.'''

#提取开头13个字符
print(poem[:13])

#len()计算这首诗有多少字符(计入空格和换行符)
print(len(poem))

#startswith判断一个文本是否以某个或几个字符开始，
#结果以True或者False返回
print('判断开始：')
print(poem.startswith('All'))
print(poem.startswith('Allt'))
print(poem.startswith('All t'))
print(poem.startswith('All that'))
print('\n')

#endswith判断一个文本是否以某个或几个字符结束，
#结果以True或者False返回
print('判断结尾：')
print(poem.endswith('That\'s all, folks!'))
print('\n')

word = 'the'
print('第一次出现单词the的位置:',poem.find(word))

print('单词the最后一次出现的位置:',poem.rfind(word))
print('the出现的次数:',poem.count(word))
print('判断所有字符是否全是字母或数字:',poem.isalnum())

