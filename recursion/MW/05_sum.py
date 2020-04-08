def our_sum(a_list):
	if len(a_list) == 0:
		return 0
	else:
		return a_list[0] + our_sum(a_list[1:])

def main():
	test = [10, 20, 30, 50]
	print(our_sum(test))

if __name__ == "__main__":
	main()
