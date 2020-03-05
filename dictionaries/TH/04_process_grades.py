NAME = 0
MIDTERM = 1
FINAL = 2
PROJECTS = 3

def process_csv(fname):
	rv = {}
	# open file
	with open(fname) as inf:
		headers = inf.readline()
		headers = headers.strip().split(",")

		# double check content of headers
		#print(headers)

		for line in inf:
			# approach 1
			#stripped_line = line.strip()
			#split_line = stripped_line.split(",")

			# alternative approach
			split_line = line.strip().split(",")

			cur_name = split_line[NAME]
			cur_dict = {}
			for col in range(1, len(split_line)):
				# double check content of headers
				#print(col)
				#print(headers[col])
				cur_dict[headers[col]] = split_line[col]

			rv[cur_name] = cur_dict
	

	# return a list of lists representing the file
	# each nested list should be a row of the csv
	return rv

def print_midterms(gdicts):
	print(format("Name", "10s"), format("Midterm grade", "10s"))
	for name in gdicts:
		# if we need help debugging later
		#print(name)
		#print(gdicts[name])

		print(format(name, "10s"), format(gdicts[name]["Midterm"], "10s"))


def print_for_student(gdicts, student_name):
	print(student_name, "'s grades:", sep="")
	for item in gdicts[student_name]:
		print("\t", item, ": ", gdicts[student_name][item])

def main():
	grade_dicts = process_csv("fake_grades.csv")

	#print(grade_dicts)

	print_midterms(grade_dicts)

	print()

	print_for_student(grade_dicts, "Alice")

	print()
	
	print_for_student(grade_dicts, "Bob")
	
main()
