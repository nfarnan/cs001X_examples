def repeat(name, times):
	return name * times
	print("this will never print")

result = repeat("nick", 5)
print(result)

result = repeat("a" + "b", 2 * 5)
print(result)

result = repeat(repeat("i", 5), 5)
print(result)

print(repeat(repeat("i", 5), 5))
