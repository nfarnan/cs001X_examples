def mult_inplace(a_list, cur_index=0):
	if cur_index >= len(a_list):
		return
	else:
		a_list[cur_index] *= 2
		mult_inplace(a_list, cur_index + 1)

def mult(a_list):
	if len(a_list) == 0:
		return []

	else:
		last_item = a_list[-1]
		ret_list = mult(a_list[:-1])
		ret_list.append(last_item * 2)
		return ret_list

def main():
	test = [5, 10, 15]
	print("Running mult:")
	print("\t returns:", mult(test))
	print("\t original:", test)
	print()
	print("Running mult_inplace:")
	print("\t returns:", mult_inplace(test))
	print("\t original:", test)

if __name__ == "__main__":
	main()
