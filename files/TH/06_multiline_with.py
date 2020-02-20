print("for approach:")

with open("name.txt") as inf:
	for line in inf:
		clean_line = line.strip()
		print("Hello,", clean_line)

print()
print("while approach:")

with open("name.txt") as inf:
	cur_line = inf.readline()

	for i in range(2):
		cur_line = inf.readline()

	while cur_line != "":
		cur_line = cur_line.strip()
		print("Hello,", cur_line)

		cur_line = inf.readline()

