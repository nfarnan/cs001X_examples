class Empty:
	pass

e = Empty()
e.test = 1
e.other_test = "another attribute!"
print(e.test)
print(e.other_test)

f = {}
f["test"] = 1
f["other_test"] = "another key/value pair!"

print(f["test"])
print(f["other_test"])
