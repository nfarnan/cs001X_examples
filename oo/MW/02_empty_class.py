class Empty:
	pass

e = Empty()
e.an_attribute = "this is an attribute"
e.another = 5

print(e.an_attribute)
print(e.another)

f = {}
f["an_attribute"] = "this is not an attribute"
f["another"] = 5
print(f["an_attribute"])
print(f["another"])
