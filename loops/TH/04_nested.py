num = int(input("Enter 1-10, -1 to stop: "))
while num != -1 and (num < 1 or num > 10):
	print("Invalid, please try again")
	num = int(input("Enter 1-10, -1 to stop: "))

while num != -1:
	print(num, "squared is", num ** 2)

	num = int(input("Enter 1-10, -1 to stop: "))
	while num != -1 and (num < 1 or num > 10):
		print("Invalid, please try again")
		num = int(input("Enter 1-10, -1 to stop: "))

