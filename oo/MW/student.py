from person import Person
from person import print_person

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

a = Student("Alice", 25)
print_person(a)
