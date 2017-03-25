#ex4-12
#编写自己的异常
class UppercaseExceptiom(Exception):
	pass

words = ['eeenie','meenie','miny','MO']
for word in words:
	if word.isupper():
		raise UppercaseExceptiom(word)
