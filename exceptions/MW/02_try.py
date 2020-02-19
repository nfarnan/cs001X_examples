try:
	x = int(input("Enter a number: "))
	y = int(input("Enter a number: "))
	print("TESTING")
	print(x, "divided by", y, "is", x/y)
	print("MORE TESTING")
except ValueError:
	print("Must enter an integer value!")
except ZeroDivisionError:
	print("Can't divide by 0!")
except:
	print("What have you done now?!?")
else:
	print("Thanks for not being a jerk")
finally:
	print("always printed")
