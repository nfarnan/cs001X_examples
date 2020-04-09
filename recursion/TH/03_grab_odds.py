def grab_odds(a_list):
	if len(a_list) == 0:
		return []

	else:
		odds = grab_odds(a_list[1:])
		if a_list[0] % 2 != 0:
			odds.append(a_list[0])
		return odds

def main():
	print(grab_odds([2, 3, 10, 112, 5, 14, 7, 9, 11, 8]))

if __name__ == "__main__":
	main()
