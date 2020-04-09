def find_min(a_list):
	if len(a_list) == 0:
		return None

	else:
		min_rest = find_min(a_list[1:])

		if min_rest == None or a_list[0] < min_rest:
			return a_list[0]
		else:
			return min_rest

def main():
	print(find_min([100, 50, 25, 70, 2, 8, 95, 7]))

if __name__ == "__main__":
	main()
