count = 5
while count > 0:
	print(count)
	count -= 1

count = 0
ans = "y"
while ans == "y":
	count += 1
	print("I'm on loop", count, "!")
	ans = input("Keep going? ")

