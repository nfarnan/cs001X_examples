class Person:
	def __init__(self, l_name, l_age=20):
		self.names = [l_name]
		self.age = l_age
	
	def display(self):
		print("Names:", self.names)
		print("Age:", self.age)

	def setAge(self, new_age):
		self.age = new_age

	def addAlias(self, alias):
		self.names.append(alias)

	def becomeStudent(self):
		self.isStudent = True

	def __str__(self):
		return self.names[0]

	def __repr__(self):
		rv = "Person("
		rv += str(self.names)
		rv += ", "
		rv += str(self.age)
		rv += ")"

		return rv

a = Person("Alice", 30)

print(a.names)
a.isStudent = False

print(a.isStudent)

#a_string = str(a)
#print(a.__str__())
#print(repr(a))
#a_representation = a.__repr__()
#print(a)
#print(a_string)
#print()
#print(a_representation)

