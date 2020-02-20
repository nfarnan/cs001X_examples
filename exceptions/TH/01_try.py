try:
	x = int(input("Enter a number: "))
	y = int(input("Enter a number: "))
	print(x, "divided by", y, "is", x / y)
except ZeroDivisionError as e:
	print("Can't divide by 0!")
	print(e)
except ValueError as e:
	print("That's not a valid integer!")
	print(e)
except Exception as e:
	print("What have you done now??!")
	print(e)
else:
	print("No errors!")
finally:
	print("Maybe an error?")

print("After try")
