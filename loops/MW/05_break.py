def get_valid():
	while True:
		num = int(input("Enter num from 1-10, or -1 to stop: "))

		if num != -1 and (num < 1 or num > 10):
			print("Invalid input, try again")
		else:
			break

	return num

def square_nums():
	while True:
		num = get_valid()
		
		if num == -1:
			break
		else:
			print(num, "squared is", num ** 2)		

def main():
	square_nums()

	# break only exits inner-most current loop
	# TERRIBLE CONFUSING EXAMPLE
	a = 1
	while a < 5:
		b = 10	
		while b < 15:
			c = 20	
			while c < 25:
				if c == 22:
					break

				print(a, b, c)

				c += 1
			b += 1
		a += 1

main()

