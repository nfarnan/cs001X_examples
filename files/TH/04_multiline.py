print("for approach:")

inf = open("name.txt")

for line in inf:
	clean_line = line.strip()
	print("Hello,", clean_line)

inf.close()


print()
print("while approach:")

inf = open("name.txt")

cur_line = inf.readline()

for i in range(2):
	cur_line = inf.readline()

while cur_line != "":
	cur_line = cur_line.strip()
	print("Hello,", cur_line)

	cur_line = inf.readline()

inf.close()
