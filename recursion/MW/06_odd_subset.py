def odd_subset(a_list):
	if len(a_list) == 0:
		return []
	else:
		odds = odd_subset(a_list[1:])
		if a_list[0] % 2 != 0:
			odds.append(a_list[0])
			
		return odds

def main():
	test = [2, 5, 7, 1, 8, 10, 12, 3]
	print(odd_subset(test))

if __name__ == "__main__":
	main()
