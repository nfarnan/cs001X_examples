def doubler(a_list):
	if len(a_list) == 0:
		return []

	else:
		rv = [a_list[0] * 2]
		return rv + doubler(a_list[1:])

def inplace_doubler(a_list, index=0):
	if index >= len(a_list):
		return

	else:
		a_list[index] *= 2
		inplace_doubler(a_list, index + 1)

def main():
	test = [10, 20, 50]
	print(test)
	#print(doubler(test))
	print(inplace_doubler(test))
	print(test)

if __name__ == "__main__":
	main()
