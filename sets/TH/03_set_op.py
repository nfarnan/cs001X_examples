s1 = {1, 2, 3, 4, 5}
s2 = {1, 3, 5}
s3 = {2, 4, 6}
s4 = {6, 7, 8, 9, 10}

#s1 = {"a", "b", "c", "d", "e"}
#s2 = {"a", "c", "e"}
#s3 = {"b", "d", "f"}
#s4 = {"f", "g", "h", "i", "j"}

#s1 = {1, True, 3, "d", 5}
#s2 = {1, 3, 5}
#s3 = {True, "d", "f"}
#s4 = {"f", "g", 7, "i", "j"}

s4.add(12)

# False
print(s1.isdisjoint(s3))
# True
print(s1.isdisjoint(s4))

s3.clear()

# symmetric difference: ^
def sym_diff(a, b):
	print("The sym diff of", a, "and", b, "is:")
	print(a ^ b)

sym_diff(s1, s2)
sym_diff(s1, s3)
sym_diff(s2, s3)
sym_diff(s1, s1)

# difference: -
def diff(a, b):
	print("The difference of ", a, "and", b, "is:")
	print(a - b)

#diff(s1, s2)
#diff(s2, s3)
#diff(s1, s1)
#diff(s2, s1)
#print()

# intersection: &
def inter(a, b):
	print("The intersection of", a, "and", b, "is:")
	print(a & b)

#inter(s1, s2)
#inter(s3, s4)
#inter(s2, s3)
#print()

# union: |
def union(a, b):
	print("The union of", a, "and", b, "is:")
	print(a | b)

#union(s2, s3)
#union(s1, s2)
#union(s2, s3)
#print()

# subset op
def subset_check(a, b):
	print("Is", a, "a subset of", b, "? ", end="")
	print(a <= b)

#subset_check(s2, s1)
#subset_check(s2, s2)
#subset_check(s3, s1)
#subset_check(s4, s3)
#print()

# strict subset op
def strict_subset_check(a, b):
	print("Is", a, "a strict subset of", b, "? ", end="")
	print(a < b)

#strict_subset_check(s2, s1)
#strict_subset_check(s2, s2)
#strict_subset_check(s3, s1)
#strict_subset_check(s4, s3)
