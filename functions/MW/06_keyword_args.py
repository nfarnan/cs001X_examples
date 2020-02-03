def kw_test(a=1, b=2):
	print(a, b)

kw_test()

kw_test(5, 7)

kw_test(10)

an_int = 17
kw_test(an_int)

kw_test(an_int + 3)

an_int = int(input("enter an integer: "))

kw_test(b=an_int)

kw_test(b=an_int, a=25)
