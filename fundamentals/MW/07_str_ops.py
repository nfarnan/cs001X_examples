# concatenation operator
cur = "a string" + "another string"
print(cur)

# ERROR
#cur = "a string" + 1
#print(cur)

print("a" + "b" + "c")
print("a", "b", "c")
print("a" + " " + "b" + " " + "c")

# ERROR
#print("a" + 1)
print("a", 1)
print("a" + " " + str(1))

a = 1
b = 2
c = 3
print(a + b + c)

a = "a"
b = str(2) # same as b = "2"
c = "c"
print(a + b + c)

# repetition operator
cur = "a string" * 5
print(cur)

# len()
cur_length = len(cur)
print(cur_length)

cur = "four"
print(len(cur))

