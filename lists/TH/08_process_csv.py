NAME = 0
MIDTERM = 1

def process_csv(fname):
	rv = []
	# open file
	with open(fname) as inf:
		for line in inf:
			# approach 1
			#stripped_line = line.strip()
			#split_line = stripped_line.split(",")

			# alternative approach
			split_line = line.strip().split(",")

			rv.append(split_line)
	

	# return a list of lists representing the file
	# each nested list should be a row of the csv
	return rv

def print_midterms(glists):
	for item in glists:
		print(format(item[NAME], "10s"), format(item[MIDTERM], "10s"))

def main():
	grade_lists = process_csv("fake_grades.csv")
	print_midterms(grade_lists)

main()
