def a():
	b()

def b():
	c()

def c():
	a()

if __name__ == "__main__":
	a()
