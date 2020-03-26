from person import Person

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

def main():
	print("testing student class")
	c = Student("Charlie", 23)
	print(repr(c))
	print(c)

if __name__ == "__main__":
	main()
