cs = {"Alice", "Bob", "Charlie", "Edward", "Gale"}
bio = {"Bob", "Fred", "Gale", "Harry", "Iris"}
chem = {"Janice", "Fred", "Gale", "Kyle"}
math = {"Alice", "Gale", "Lisa", "Matt"}

value = 1 + 2 + 3

# all students
a = cs | bio | chem | math
print(a)

# students in both cs and bio classes
cs_and_bio = cs & bio
print(cs_and_bio)

# in cs but no in bio
cs_no_bio = cs - bio
print(cs_no_bio)

# in bio but not in cs
bio_no_cs = bio - cs
print(bio - cs)

either_not_both = bio ^ cs
print(either_not_both)

print(either_not_both == (cs_no_bio | bio_no_cs))

# students taking all subjects
overachievers = cs & bio & chem & math
print(overachievers)

cs.add("Nick")

french = {"Oliver", "Patty", "Sam", "Bob"}

# french & cs == set()
print(french.isdisjoint(cs))
# french & chem == set()
print(french.isdisjoint(chem))

french.clear()
