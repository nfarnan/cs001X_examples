class Person:
	def __init__(self, name, age=20):
		self.__name = name
		self.__age = age

	def display(self):
		print("Name:", self.__name)
		print("Age:", self.__age)

	def __str__(self):
		return self.__name + "!"

	def __repr__(self):
		rv = "Person("
		rv += self.__name
		rv += ", "
		rv += str(self.__age)
		rv += ")"

		return rv

	def hadBirthday(self):
		self.__age += 1

	def getAge(self):
		return self.__age

	def getName(self):
		return self.__name

def display_person(a_person):
	a_person.display()

def main():
	print("test the person class")

	b = Person("Bob", 30)
	print(b)
	print(repr(b))

if __name__ == "__main__":
	main()
