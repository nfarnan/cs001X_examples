class SmallClass:
	def __init__(self, att):
		self.__att = att

	def getAtt(self):
		return self.__att

s = SmallClass("first value")
print(s.getAtt())

# V Don't ever do this V
s.__att = 2

print(s.getAtt())
print(s.__att)
