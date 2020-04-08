def rev_lprint(a_list):
	if len(a_list) == 0:
		return
	else:
		# approach 1
		# original list unmodified due to slice copy
		print(a_list[-1])
		rev_lprint(a_list[:-1])

		# approach 2
		# original list modified by pop
		#print(a_list.pop())
		#rev_lprint(a_list)

def lprint(a_list):
	if len(a_list) == 0:
		# base case
		return
	else:
		# recursive case
		print(a_list[0])
		lprint(a_list[1:])

def main():
	#lprint([1, 2, 3, 4, 5])
	test = [1, 2, 3, 4, 5]
	rev_lprint(test)
	print(test)

if __name__ == "__main__":
	main()
