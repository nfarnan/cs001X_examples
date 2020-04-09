def rsum(a_list):
	if len(a_list) == 0:
		return 0

	else:
		return a_list[0] + rsum(a_list[1:])

def main():
	print(rsum([10, 20, 40, 60]))

if __name__ == "__main__":
	main()
