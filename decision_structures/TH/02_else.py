an_int = 5

if an_int < 10:
	print("less than 10")
else:
	print("not less than 10")

print("always printed")

# color checking approach1
a_color = "red"
if a_color == "red":
	print("its red!")
else:
	if a_color == "blue":
		print("its blue!")
	else:
		print("its something else!")

# color checking approach2
if a_color == "red":
	print("its red!")
elif a_color == "blue":
	print("its blue!")
elif a_color == "purple":
	print("its purple!")
else:
	print("its something else!")

