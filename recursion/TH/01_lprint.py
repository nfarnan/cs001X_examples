def lprint(a_list):
	# base case
	if len(a_list) == 0:
		return
	
	# recursive case
	else:
		print(a_list[0])
		lprint(a_list[1:])

def rev_lprint(a_list):
	if len(a_list) == 0:
		return

	else:
		print(a_list[-1])
		
		# approach 1, modifies argument
		#a_list.pop()
		#rev_lprint(a_list)

		# approach 2, creates a copy
		rev_lprint(a_list[:-1])

def main():
	test = [1, 2, 3, 4, 5]
	#lprint(test)
	print(test)
	rev_lprint(test)
	print(test)

if __name__ == "__main__":
	main()
