class Person:
	def __init__(self, l_name, l_age=20):
		self.__name = l_name
		self.__age = l_age
	
	def display(self):
		print("Names:", self.__name)
		print("Age:", self.__age)

	def setAge(self):
		self.__age += 1

	def getAge(self):
		return self.__age

	def becomeStudent(self):
		self.__isStudent = True

	def __str__(self):
		return self.__name

	def __repr__(self):
		rv = "Person("
		rv += str(self.__name)
		rv += ", "
		rv += str(self.__age)
		rv += ")"

		return rv

a = Person("Alice", 30)
a.setAge()

# BAD! creates second, public attribute also named __age
a.__age = 45
# don't do this

print(a.getAge())
print(a.__age)
