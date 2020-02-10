def get_non_negative():
	cur = int(input("Enter a non-negative int: "))

	while cur < 0:
		print("Invalid value, please try again")
		cur = int(input("Enter a non-negative int: "))

	return cur

def get_one_to_ten():
	cur = int(input("Enter a number from 1-10: "))
	while cur < 1 or cur > 10:
		print("Invalid value, please try again")
		cur = int(input("Enter a number from 1-10: "))

	return cur

def get_rgb():
	print("Make a selection:")
	print("\t1: Red")
	print("\t2: Green")
	print("\t3: Blue")
	cur = input("Enter 1, 2, or 3: ")

	while cur < 1 or cur > 3:
		print("Invalid value, please try again")
		cur = input("Enter 1, 2, or 3: ")
		
	# base cases
	if cur == "1":
		return "Red"
	elif cur == "2":
		return "Green"
	else:
		return "Blue"

#num = get_non_negative()
#print(num)

#num = get_one_to_ten()
#print(num)

color = get_rgb()
print(color)
