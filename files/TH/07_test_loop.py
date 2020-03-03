with open("test.txt") as inf:
	for line in inf:
		print(line)

	
with open("test.txt") as inf:
	cur_line = inf.readline()
	while cur_line != "":
		print(cur_line)
		cur_line = inf.readline()
