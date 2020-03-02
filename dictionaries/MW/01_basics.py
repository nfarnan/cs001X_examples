d = {}

d["a"] = "First"
d["b"] = "Second"

print(d)

print(d["a"])
print(d["b"])

# Will error:
#print(d[0])

d[0] = "Third"
d[2] = "Fourth"
d[1] = "Fifth"

print(d)
print(d[0])
print(d[1])
print(d[2])

d[None] = "Sixth"
print(d[None])
