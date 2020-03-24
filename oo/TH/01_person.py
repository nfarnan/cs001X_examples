class Person:
	def __init__(self, l_name, l_height="tall", l_age=20):
		self.__name = l_name
		self.__height = l_height
		self.__age = l_age

		self.__hair_color = None

	def display(self):
		print("Name:", self.__name)
		print("Age:", self.__age)

	def __str__(self):
		return self.__name + "!"

	def __repr__(self):
		rv = "Person("
		rv += self.__name
		rv += ", "
		rv += self.__height
		rv += ", "		
		rv += str(self.__age)
		rv += ")"

		return rv

	def hadBirthday(self):
		self.__age += 1

	def getAge(self):
		return self.__age

	def setMarried(self, is_married):
		self.__married = is_married

	def getMarried(self):
		return self.__married

a = Person("Alice", 30)

b = Person("Bob")

#print(a) # really the same as print(str(a))
#print(b)

a.display()
b.display()

b.hadBirthday()
b.display()

print(b.getAge())

# this will error
#print(getAge(b))

b.__age = 45
b.display()

b.isMarried(True)

#str_a1 = str(a)
#str_a2 = a.__str__()

#print(str_a1)
#print(str_a2)

#str_a3 = a.__repr__()
#print(str_a3)
