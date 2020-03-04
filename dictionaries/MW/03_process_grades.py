def read_file(fname):
	main_dict = {}
	with open(fname) as infile:
		headers = infile.readline()
		headers = headers.strip().split(",")
		# testing file parsing
		#print("headers:")
		#print(headers)
		#print("rest of the file:")

		for line in infile:
			clean_line = line.strip()
			cur_row = clean_line.split(",")
			# testing row parsing
			#print(cur_row)

			nested_dict = {}
			for i in range(1, len(cur_row)):
				nested_dict[headers[i]] = cur_row[i]

			# testing creation of nested_dict
			#print(nested_dict)

			main_dict[cur_row[0]] = nested_dict

	return main_dict

def print_midterms(grades):
	print("Name, Midterm score")
	for key in grades:
		print(key, ": ", grades[key]["Midterm"])

	print()

def print_for_student(grades, stud_name):
	print(stud_name, "'s grades:", sep="")
	for key in grades[stud_name]:
		print("\t", key, ": ", grades[stud_name][key])

	print()

def main():
	grades_nd = read_file("fake_grades.csv")
	
	# debugging result of read_file
	#print(grades_nd)

	print_midterms(grades_nd)
	print_for_student(grades_nd, "Bob")

main()
