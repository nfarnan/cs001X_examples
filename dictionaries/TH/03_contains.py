d = {"one": 1, "two": 2, "three": 3}

if "one" in d:
	print("one is a valid key in d!")
else:
	print("one is not a key in d...")

if "Two" in d:
	print("Two is valid key in d!")
else:
	print("Two is not a valid key in d...")

if "five" not in d:
	print("five is not a valid key")
else:
	print("five is a key")

print(2 in d)

print()

l = [1, 2, 3, 4, 5]
print(0 in l)
print(4 in l)

print()

t = ("a", "b", 7)
print("a" in t)
print(8 in t)

print()

s = "abcdef"
print("a" in s)
print("q" in s)

print()

all_vals = d.values()
print(all_vals)
print(2 in all_vals)
print(7 in all_vals)
