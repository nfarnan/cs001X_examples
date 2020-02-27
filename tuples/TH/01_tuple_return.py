a_tuple = 1, 2, 3
print(a_tuple)
print(type(a_tuple))

a, b, c = a_tuple
print(a)
print(b)
print(c)

print()
print("now for functions")
print()

def return_multiple():
	return 1, 2, 3

d, e, f = return_multiple()
print(d)
print(e)
print(f)

test = return_multiple()
print(test)
print(type(test))
