def get_non_negative():
	valid = False
	while not valid:
		try:
			num = int(input("Enter a non-negative int: "))
		except:
			print("Invalid! Not an integer.")
		else:
			if  num < 0:
				print("Invalid! Was negative.")
			else:
				valid = True

	return num

def get_non_negative2():
	while True:
		try:
			num = int(input("Enter a non-negative int: "))
		except:
			print("Invalid! Not an integer.")
		else:
			if num < 0:
				print("Invalid! Was negative.")
			else:
				break

an_int = get_non_negative()
print(an_int)
