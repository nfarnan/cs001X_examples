NAME = 0
MIDTERM = 1
FINAL = 2
PROJECTS = 3

def read_file(fname):
	main_list = []
	with open(fname) as infile:
		for line in infile:
			clean_line = line.strip()
			main_list.append(clean_line.split(","))

	# method 1
	#return main_list[1:]
	# method 2
	main_list.pop(0)
	return main_list

def print_midterms(grades):
	for sublist in grades:
		print(sublist[NAME], ": ", sublist[MIDTERM], sep="")

def main():
	grades_nl = read_file("fake_grades.csv")
	print_midterms(grades_nl)

main()
