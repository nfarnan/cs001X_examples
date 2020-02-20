try:
	with open("numbers.txt") as infile:
		total = 0
		for line in infile:
			total += int(line.strip())
except Exception as err:
	print(err)
else:
	print("The total is", total)
finally:
	print("DONE")
