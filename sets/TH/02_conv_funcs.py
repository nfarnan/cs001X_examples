l = [ ("one", 1), ("two", 2), ("three", 3) ]
d1 = {"one":1, "two":2, "three":3}
d2 = dict(l)

print(d1)
print(d2)

l = [1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 4, 5, 5, 5]

# alternative approach
#l = list(set(l))

print(l)

s = set(l)

print(s)

l = list(s)

print(l)
