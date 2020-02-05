def get_non_negative():
	cur = int(input("Enter a non-negative int: "))

	# base case
	# have non-negative
	if cur > 0:
		return cur

	# recursive case
	# have a negative
	else:
		print("Invalid! Try again")
		
		#two lines 
		#cur = get_non_negative()
		#return cur

		return get_non_negative()

def get_one_to_ten():
	cur = int(input("Enter a number from 1-10: "))
	if cur >= 1 and cur <= 10:
		return cur
	else:
		print("Invalid! Try again")
		return get_one_to_ten()

def get_rgb():
	print("Make a selection:")
	print("\t1: Red")
	print("\t2: Green")
	print("\t3: Blue")
	cur = input("Enter 1, 2, or 3: ")
	# base cases
	if cur == "1":
		return "Red"
	elif cur == "2":
		return "Green"
	elif cur == "3":
		return "Blue"

	# recursive case
	else:
		print("Invalid! Try again")
		return get_rgb()

#num = get_non_negative()
#print(num)

#num = get_one_to_ten()
#print(num)

color = get_rgb()
print(color)
