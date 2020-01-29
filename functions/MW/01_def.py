def something_else():
	print("CALLING MESSAGE")
	any_name()
	print("DONE CALLING MESSAGE")

def any_name():
	print("Hello there!")
	print("How are you?")

def print_input():
	a_val = input("Enter something to print: ")
	print("You entered:", a_val)

print_input()
