class Person:
	def __init__(self, l_name, l_age=20):
		self.__name = l_name
		self.__age = l_age
	
	def display(self):
		print("Name:", self.__name)
		print("Age:", self.__age)

	def setAge(self):
		self.__age += 1

	def getAge(self):
		return self.__age

	def getName(self):
		return self.__name

	def __str__(self):
		return self.__name

	def __repr__(self):
		rv = "Person("
		rv += str(self.__name)
		rv += ", "
		rv += str(self.__age)
		rv += ")"

		return rv

def print_person(a_person):
	a_person.display()

def main():
	print("Starting tests for Person...")
	a = Person("Alice", 30)
	a.display()
	print()
	print(a.getAge())
	print()
	print(a.getName())
	print()
	print(a)
	print()
	print(repr(a))
	print()

	a.setAge()
	print(repr(a))
	print("DONE testing Person!")

if __name__ == "__main__":
	main()
