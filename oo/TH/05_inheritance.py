class Person:
	def __init__(self, name, age=20):
		self.name = name
		self.age = age

	def display(self):
		print("Name:", self.name)
		print("Age:", self.age)

	def __str__(self):
		return self.name + "!"

	def __repr__(self):
		rv = "Person("
		rv += self.name
		rv += ", "
		rv += str(self.age)
		rv += ")"

		return rv

	def hadBirthday(self):
		self.age += 1

	def getAge(self):
		return self.age

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
		rv = "Student("
		rv += self.name
		rv += ", "
		rv += str(self.age)
		rv += ", "
		rv += str(self.__classes)
		rv += ")"

		return rv


a = Student("Alice", 20)
print(repr(a))

a.display()

print(a)
