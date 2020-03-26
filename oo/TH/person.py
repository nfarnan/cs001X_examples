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

def display_person(a_person):
	a_person.display()

def main():
	print("test the person class")

	b = Person("Bob", 30)
	print(b)
	print(repr(b))

if __name__ == "__main__":
	main()
