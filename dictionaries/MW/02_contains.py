d = {"a":1, "b":2, "c":3, "d":4, "e":5}

if "f" in d:
	print(d["f"])
else:
	print("f is not in the dictionary")

l = ["a", "b", "c", "d", "e"]

if "b" in l:
	print("b is in the list")
else:
	print("b is not in the list")

t = ("a", "b", "c", "d", "e")
if "c" in l:
	print("c is in the tuple")
else:
	print("c is not in the tuple")

s = "abcde"
if "d" not in s:
	print("d is not in the string")
else:
	print("d is in the string")

