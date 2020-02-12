# a more clear (but still quite complex) example of break usage with nested loops

i = 0

while i < 3:
	print("First!")

	j = 0
	while j < 3:
		print("Second!!")

		k = 0
		while k < 3:
			print("Starting third...")
			break
			print("Third!!!")

			k += 1

		print()
		j += 1

	print()
	i += 1
