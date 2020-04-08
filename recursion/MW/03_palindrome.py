def is_palindrome(word):
	if len(word) <= 1:
		return True
	elif word[0] != word[-1]:
		return False
	else:
		return is_palindrome(word[1:-1])

def main():
	words = ["racecar", "intro"]
	words.append("amanaplanacanalpanama")
	words.append("atoyota")
	for word in words:
		print("Is", word, "a palindrome?")
		print(is_palindrome(word))

if __name__ == "__main__":
	main()
