inf = open("name.txt")
for line in inf:
	clean_line = line.strip()
	print("Hello", clean_line)
inf.close()

inf = open("name.txt")
cur_line = inf.readline()
while cur_line != "":
	cur_line = cur_line.strip()
	print("Hello", cur_line)
	cur_line = inf.readline()
inf.close()
