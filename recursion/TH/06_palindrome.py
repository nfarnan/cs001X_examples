def check_palindrome(word):
	if len(word) <= 1:
		return True
	elif word[0] != word[-1]:
		return False
	else:
		return check_palindrome(word[1:-1])

def main():
	words = ["racecar", "intro"]
	words.append("amanaplanacanalpanama")
	words.append("tacocat")
	words.append("evacanistabbatsinacave")
	for word in words:
		print("Checking", word, ":", check_palindrome(word))

if __name__ == "__main__":
	main()
