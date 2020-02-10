def nested():
	num = int(input("Enter num from 1-10, or -1 to stop: "))
	while num != -1 and (num < 1 or num > 10):
		print("Invalid input, try again")
		num = int(input("Enter num from 1-10, or -1 to stop: "))

	while num != -1:
		print(num, "square is", num ** 2)

		num = int(input("Enter num from 1-10, or -1 to stop: "))
		while num != -1 and (num < 1 or num > 10):
			print("Invalid input, try again")
			num = int(input("Enter num from 1-10, or -1 to stop: "))


def get_valid():
	num = int(input("Enter num from 1-10, or -1 to stop: "))
	while num != -1 and (num < 1 or num > 10):
		print("Invalid input, try again")
		num = int(input("Enter num from 1-10, or -1 to stop: "))

	return num

def non_nested():
	num = get_valid()
	while num != -1:
		print(num, "squared is", num ** 2)
		num = get_valid()


def main():
	print("NESTED APPROACH:")
	nested()

	print("NON NESTED APPROACH:")
	non_nested()

main()
