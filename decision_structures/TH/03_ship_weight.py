# get weight from the user
weight = float(input("How heavy is the package to ship (lbs)? "))

if weight <= 0:
	print("Invalid weight (you jerk)")
	total = None

elif weight <= 2:
	# flat rate of $5
	total = 5

# between 2 and 6 lbs:
elif weight <= 6:
	# $5 + $1.50 per lb over 2
	total = 5 + 1.5 * (weight - 2)

# between 6 and 10 lbs:
elif weight <= 10:
	# $11 + $1.25 per lb over 6
	total = 11 + 1.25 * (weight - 6)

# over 10 lbs:
else:
	# $16 + $1 per lb over 10
	total = 16 + (weight - 10)

if total != None:
	# output total cost to user:
	print("It will cost $", format(total, ".2f"), " to ship", sep="")
