a_list = ["a", "b", "c", "d", "e"]

print(len(a_list))

# concatenation op
b = a_list + ["f", "g"]
print(b)

# repetition op
c = ["a", "b"] * 5
print(c)

s_list = sorted(c)
print(s_list)
s_string = sorted("this is just a string")
print(s_string)
print(c)

str_list = ",".join(a_list)
print(str_list)
