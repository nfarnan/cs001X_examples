a_list = [1, 2, "3", 4.0]
a_string = "1234.0"

# indexing
#     0      1      2
# [ item1, item2, item3 ]
#    -3     -2     -1

print(a_list)
print(a_string)

print("list indexing")
print(a_list[0])
print(a_list[3])

# will error
#print(a_list[4])

print(a_list[-1])

print("string indexing")
print(a_string[0])
print(a_string[3])

print(a_string[-1])

print("variable assignment")
an_item = a_list[1]
# the same as:
a_value = 2
another_item = a_value
print(an_item)
print(another_item)

print("slicing examples")
a_slice = a_list[:2]
print(a_slice)

another_slice = a_string[2:]
print(another_slice)

print(a_string[-4:-2])
print(a_string[-4:5])
print(a_string[-4:1])
print(a_string[-4:])
print(a_string[:-1])
