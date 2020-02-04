def tricky(a, b, c, d=4, e=5, f=6):
	print(a, b, c, d, e, f)

tricky(1, 2, 3)

tricky(1, 2, 3, 40, 50, 60)

# this will error
#tricky(1)

# this will error
#tricky(1, 2, 3, 40, 50, 60, 70)

tricky(10, 20, 30, 40)

tricky(10, 20, 30, f=60)

# this will error
#tricky(10, 20, 30, f=60, 40, 50)

tricky(10, 20, 30, 40, f=60)

tricky(10, 20, 30, f=60, e=50, d=40)

tricky(f=60, d=40, a=10, c=30, b=20)
