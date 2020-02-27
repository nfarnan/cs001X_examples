d = {"one":1, "two":2, "three":3}
print(d["one"])

print(d)

d["five"] = 5

print(d["five"])
print(d)

d[7] = "seven"
print(d[7])
print(d)

d[7] = "SEVEN"
print(d[7])
print(d)

d["SEVEN"] = 7
print(d["SEVEN"])
print(d)

d["one"] = 7
d["two"] = 7
print(d)
