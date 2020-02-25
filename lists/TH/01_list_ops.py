l = [1, 2, "3", 4.0]
s = "1234.0"

print("lengths:")
print(len(l))
print(len(s))
print()

print("concatenation:")
new_l = [1] + l + ["5", 6]
print(new_l)
print(l)
print("repetition:")
print(["a", "b"] * 5)
print()

#index values
#   0    1    2    3
#[ "a", "b", "c", "d" ]
#  -4   -3   -2   -1
print("indexing:")
print(l[0])
print(s[0])
# this will error
#print(l[4])
print(l[-1])
print(s[-1])
print()

print("slicing:")
print(l[1:-1])
print(l[1:3])
print(l[:2])
print(l[-3:])

print(s[2:5])
print()
