def testing(a, b, c, d=4, e=5, f=6):
	print(a, b, c, d, e, f)

# this will error
#testing(1)

testing(1, 2, 3)

testing(1, 2, 3, 40, 50, 60)

testing(1, 2, 3, 400)

testing(1, 2, 3, f=600)

# this will also error
#testing(1, 2, 3, f=600, 400, 500)

testing(1, 2, 3, f=600, e=500, d=400)

# this will error
#testing(1, 2, 3, d=400, 500, 600)

testing(1, 2, 3, 400, f=600)

testing(f=600, e=500, d=400, c=300, b=200, a=100)

testing(f=300, a=3, b=4, c=2)
