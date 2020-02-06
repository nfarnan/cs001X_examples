def get_non_negative():
	num = int(input("Enter a non-negative int: "))
	# base case
	if num >= 0:
		return num

	# recursive case
	else:
		print("Invalid input! Please try again")
		num = get_non_negative()
		return num

def get_rgb():
	color = input("Red, Green, or Blue? ")

	# base case
	if color == "Red" or color == "Green" or color == "Blue":
		return color

	# recursive
	else:
		print("Invalid input! Please try again")
		return get_rgb()

def get_rgb2():
	print("Please select a color:")
	print("1: Red")
	print("2: Green")
	print("3: Blue")
	choice = input("Enter 1, 2, or 3: ")
	
	if choice == "1":
		return "Red"
	elif choice == "2":
		return "Green"
	elif choice == "3":
		return "Blue"

	else:
		print("Invalid input! Please try again")
		return get_rgb2()

#an_int = get_non_negative()
#print(an_int)

#a_color = get_rgb()
a_color = get_rgb2()
print(a_color)
