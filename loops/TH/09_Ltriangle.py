# draw an left-leaning triangle of *'s

# ask the user for height
height = int(input("Enter a triangle height: "))

# Approach 1
# iterate over rows of the triangle
for i in range(1, height + 1):
	#print("working on row", i)

	# use repetition operator!
	stars = "*" * i
	print(stars)

# Approach 2
# iterate over rows of the triangle
for i in range(1, height + 1):
	#print("working on row", i)

	# DON't use repetition operator!
	# print out i *'s per row
	for counter in range(i):
		print("*", end="")

	# print newline once per row
	print()

