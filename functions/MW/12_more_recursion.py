def a(num):
	if num > 0:
		# recursive case
		print("Hello")
		a(num - 1)
		print("Goodbye")
	else:
		# base case
		print("all done!")
		return


def b(num):
	if num <= 0:
		# base case
		print("all done!")
		return
	else:
		# recursive case
		print("Hello")
		b(num - 1)
		print("Goodbye")

def c(num):
	print("Hello")
	c(num - 1)
	print("Goodbye")

#a(5)
#b(5)
c(5)
