a = []

a.append(1)
a.append(2)
a.append(3)
a.append(4)
a.append(5)

print("initial a:")
print(a)
print()

b = a

a.append(10)
a = a + [20]
a.append(30)

print("a:")
print(a)
print("b:")
print(b)
print()

print("removal test on a:")
a.append(2)
print(a)
a.remove(2)
print(a)
print()

print("popping:")
a.pop()
print(a)
a.pop(2)
print(a)
print()

print("clear:")
a.clear()
print(a)

