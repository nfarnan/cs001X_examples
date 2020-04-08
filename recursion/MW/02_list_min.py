def lmin(a_list, cur_min=None):
	if len(a_list) == 0:
		# base case
		return cur_min
	else:
		# recursive case
		if cur_min == None or a_list[0] < cur_min:
			return lmin(a_list[1:], a_list[0])
		else:
			return lmin(a_list[1:], cur_min)

def imin(a_list):
	cur_min = a_list[0]
	for item in a_list[1:]:
		if item < cur_min:
			cur_min = item

	return cur_min

def main():
	test = [5, 15, 2, 10, 87, 1, 100, 25]
	print(lmin(test))
	print(imin(test))

if __name__ == "__main__":
	main()
