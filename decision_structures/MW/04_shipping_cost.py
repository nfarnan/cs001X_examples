# get input from the user
weight = float(input("How much does the package weigh? "))

# check weight
if weight <= 0:
	print("Invalid weight entered, you jerk")
	total = None
elif weight < 2:
	# <2lbs: $5
	total = 5
elif weight < 6:
	# between 2 and 6: $5 + $1.50/lb over 2
	total = 5 + (weight - 2) * 1.5
elif weight < 10:
	# between 6 and 10: $11 + $1.25/lb over 6
	total = 11 + (weight - 6) * 1.25
else:
	# over 10lbs: $16 + $1/lb over 10
	total = 16 + (weight - 10)

if total != None:
	# output resulting cost
	ftotal = format(total, ".2f")
	print("The cost of shipping is $", ftotal, ".", sep="")

