a = []

a.append(1)
a.append(2)
a.append(3)

b = a

print("initial: ")
print(a)
print(b)
print()

a.append(10)

print("after append(10): ")
print(a)
print(b)
print()

a = a + [20]
# how is different from a.append(20)?

print("after a = a+[20]: ")
print(a)
print(b)
print()

a.append(30)

print("after a.append(30): ")
print(a)
print(b)
print()

