with open("name.txt") as inf:
	for line in inf:
		print(line.strip())

# inf no longer valid here, has been closed
