a_var = 10

def a():
	a_var = 5
	b()
	print(a_var)

def b():
	#a_var = 7
	print(a_var)

a()
print(a_var)

