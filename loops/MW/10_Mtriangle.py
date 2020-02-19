# get height from user
height = int(input("Enter height of M triangle: "))

# iterate through each row
for i in range(1, height + 1):
	# print out spaces
	for k in range(height - i):
		print(" ", end="")

	# print out stars (part 1)
	for j in range(i):
		print("*", end="")

	# print out the stars (part 2)
	for l in range(i - 1):
		print("*", end="")

	# end the row
	print()
