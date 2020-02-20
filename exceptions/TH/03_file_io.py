try:
	inf = open("name.txt")
except FileNotFoundError:
	print("name.txt does not exist!")
else:
	print(inf.read())
	inf.close()
