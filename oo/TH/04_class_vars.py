class Dog:
	# shared by all instances of Dog
	__tricks = []

	def __init__(self, name):
		self.__name = name
		#self.__tricks = []

	def addTrick(self, trick):
		self.__tricks.append(trick)

	def __repr__(self):
		rv = "Dog(" + self.__name
		rv += ", " + str(self.__tricks)
		rv += ")"

		return rv

class Cat:
	__tricks = []

	def __init__(self, name):
		self.__name = name
		#self.__tricks = []

	def addTrick(self, trick):
		self.__tricks.append(trick)

	def __repr__(self):
		rv = "Cat(" + self.__name
		rv += ", " + str(self.__tricks)
		rv += ")"

		return rv

b = Dog("Buddy")
b.addTrick("stay")

f = Dog("Fido")
f.addTrick("sit")

print(repr(b))
print(repr(f))

l = Dog("Lassie")
print(repr(l))

k = Cat("Kitty")
print(repr(k))
