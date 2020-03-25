class Dog:
	# class var, shared by all Dog instances
	tricks = []

	def __init__(self, name):
		self.__name = name
		# different tricks for each Dog instance
		#self.__tricks = []
	
	def add_trick(self, trick):
		self.tricks.append(trick)

	def __repr__(self):
		rv = "Dog(" + self.__name + ", "
		rv += str(self.tricks)
		rv += ")"

		return rv

class Cat:
	# class var, shared by all Cat instances
	tricks = []

	def __init__(self, name):
		self.__name = name
		# different tricks for each Cat instance
		#self.__tricks = []
	
	def add_trick(self, trick):
		self.tricks.append(trick)

	def __repr__(self):
		rv = "Cat(" + self.__name + ", "
		rv += str(self.tricks)
		rv += ")"

		return rv


b = Dog("Buddy")
b.add_trick("stay")

w = Cat("Whiskers")
t = Cat("Tails")
t.add_trick("fly")

f = Dog("Fido")
f.add_trick("sit")

print(repr(b))
print(repr(f))

c = Dog("Charlie")
print(repr(c))

print(repr(w))
print(repr(t))
