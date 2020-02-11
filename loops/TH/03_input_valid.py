def get_non_negative():
	num = int(input("Enter a non-negative int: "))
	while num < 0:
		print("Invalid! Please try again.")
		num = int(input("Enter a non-negative int: "))

	return num

def get_rgb():
	color = input("Red, Green, or Blue? ")

	while color != "Red" and color != "Green" and color != "Blue":	
		print("Invalid! Please try again.")
		color = input("Red, Green, or Blue? ")

	return color

def get_rgb2():
	print("Please select a color:")
	print("1: Red")
	print("2: Green")
	print("3: Blue")
	choice = input("Enter 1, 2, or 3: ")
	
	while choice != "1" and choice != "2" and choice != "3":
		print("Invalid! Please try again.")
		choice = input("Enter 1, 2, or 3: ")

	if choice == "1":
		return "Red"
	elif choice == "2":
		return "Green"
	else:
		return "Blue"

#an_int = get_non_negative()
#print(an_int)

#a_color = get_rgb()
a_color = get_rgb2()
print(a_color)
