print(22/7)

# precision
print(format(4.777, ".2f"))

# commas
formatted = format(10000000, ",d")
print(formatted)

# precision and commas
print(format(10000000.55555, ",.3f"))
print(format(10000000.55555, ".3f"))

# width and alignment
formatted = "!" + format(10, "^5d") + "!"
print(formatted)

formatted = "!" + format(10, "<5d") + "!"
print(formatted)

formatted = "!" + format(10, ">5d") + "!"
print(formatted)

formatted = "!" + format(10, "d") + "!"
print(formatted)

# fill, width, and alighnment
formatted = "!" + format(10, ">15d") + "!"
print(formatted)

# all together
print(format(7.555, "@^10,.2f"))
