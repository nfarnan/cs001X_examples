def a(num):
	if num > 0:
		# recursive case
		print("Hello from recursive case")
		a(num - 1)
		print("Goodbye from scope with", num)

	else:
		# base case
		print("Base case")
		return

	print("another print")

a(5)
a(3)
print("all done!")
