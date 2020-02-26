def print_nested_list(nl):
	for sublist in nl:
		print(sublist)
		for item in sublist:
			print(item, "  ", end="")

		print()
	print()
	print()

nl = [["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"]]

print_nested_list(nl)

nl[1].append("q")

#print_nested_list(nl)

nl[2].clear()

#print_nested_list(nl)

nl.append("x")
nl.append("y")
nl.append("z")

#print_nested_list(nl)

#print(nl)
