def get_valid():
	num = int(input("Enter 1-10, -1 to stop: "))
	while num != -1 and (num < 1 or num > 10):
		print("Invalid, please try again")
		num = int(input("Enter 1-10, -1 to stop: "))

	return num

def get_valid2():
	while True:
		num = int(input("Enter 1-10, -1 to stop: "))

		if num != -1 and (num < 1 or num > 10):
			print("Invalid, please try again")
		else:
			break

	return num

def main():
	num = get_valid()
	while num != -1:
		print(num, "squared is", num ** 2)

		num = get_valid()

main()

