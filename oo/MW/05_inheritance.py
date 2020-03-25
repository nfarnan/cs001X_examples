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

	def __str__(self):
		return self.__name

	def __repr__(self):
		rv = "Person("
		rv += str(self.__name)
		rv += ", "
		rv += str(self.__age)
		rv += ")"

		return rv

class Student(Person):
	def __init__(self, name, age):
		Person.__init__(self, name, age)
		self.__classes = []

	def addClass(self, new_class):
		self.__classes.append(new_class)

	def display(self):
		Person.display(self)
		print("Classes:", self.__classes)

	def __repr__(self):
		rv = "Student(" + self.name
		rv += ", " + str(self.age)
		rv += ", " + str(self.__classes)
		rv += ")"

		return rv

a = Student("Alice", 30)
a.display()
a.addClass("CS001X")
a.display()

# testing
print(a)
