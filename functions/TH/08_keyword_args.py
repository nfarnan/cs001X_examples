def kw_test(a=1, b=2):
	print(a, b)

kw_test()

kw_test(5, 10)

kw_test(5)

kw_test(b=10)

# this will error
#kw_test(5, 10, 20)
