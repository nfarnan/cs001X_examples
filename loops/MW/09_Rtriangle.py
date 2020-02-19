height = int(input("Enter height of R triangle: "))

# approach 1
for i in range(1, height + 1):
	for k in range(height - i):
		print(" ", end="")

	for j in range(i):
		print("*", end="")

	print()

# approach 2
for i in range(1, height + 1):
	print(" " * (height - i), end="")
	print("*" * i)	
