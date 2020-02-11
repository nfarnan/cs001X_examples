count = 0
ans = "y"
while ans == "y":
	count += 1
	print("on loop", count)

	# needed to avoid infinite loops
	ans = input("Keep going? ")

cur = 50
while cur > 0:
	print(cur)
	cur -= 1

