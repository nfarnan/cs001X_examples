height = int(input("Enter height of L triangle: "))

# approach 1
for i in range(1, height + 1):
	for j in range(0, i):
		print("*", end="")

	print()

# approach 2
for i in range(1, height + 1):
	print("*" * i)	
