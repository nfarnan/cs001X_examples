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
		rv = "Student(" + self.getName()
		rv += ", " + str(self.getAge())
		rv += ", " + str(self.__classes)
		rv += ")"

		return rv

def main():
	print("Starting tests of Student class...")
	a = Student("Alice", 25)
	a.display()
	print()
	print(a)
	print()
	print(repr(a))
	print()

	a.addClass("CS001X")
	a.display()
	print()
	print(a)
	print()
	print(repr(a))
	print("DONE testing Student class!")

#print("__name__ is: ", __name__)
if __name__ == "__main__":
	main()
