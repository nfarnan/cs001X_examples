NAME = 0
MIDTERM = 1
FINAL = 2
PROJECTS = 3

def read_file(fname):
	main_dict = {}
	with open(fname) as infile:
		for line in infile:
			clean_line = line.strip()
			cur_row = clean_line.split(",")
			nested_dict = {"Midterm":cur_row[MIDTERM], \
				"Final":cur_row[FINAL], \
				"Projects":cur_row[PROJECTS]}
			main_dict[cur_row[NAME]] = nested_dict

	return main_dict

def print_midterms(grades):
	for sublist in grades:
		print(sublist[NAME], ": ", sublist[MIDTERM], sep="")

def print_for_student(grades, stud_name):
	for row in grades:
		if row[NAME] == stud_name:
			print(stud_name, "got:")
			print("\tMidterm:", row[MIDTERM])
			print("\tFinal:", row[FINAL])
			print("\tProjects:", row[PROJECTS])

def main():
	grades_nd = read_file("fake_grades.csv")
	print(grades_nd)

main()
