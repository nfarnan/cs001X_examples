print(format(22/7, ".3f"))

print(format(10000000, ",d"))

print(format(12570209.876, ",.1f"))

print(format(5, "10d"))
print(format(100000, "10,d"))

print(format(7, "@<6d"))
print(format(7, "@^6d"))
print(format(7, "@>6d"))

print(1, 2, 3)
print(1, 2, 3, sep=" ")

print(format(7/22, "!^15.5f"), "more text data")

a_string = "!" + format(100000, "20,d") + "!"
print(a_string)
