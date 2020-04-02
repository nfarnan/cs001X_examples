# assume valid suits are "C", "D", "H", "S"
class Card:
	def __init__(self, value, suit):
		self.value = value
		self.suit = suit

		#if self.suit == "D" or self.suit == "H":
		#	self.color = "red"
		#else:
		#	self.color = "black"

	def getColor(self):
		if self.suit == "D" or self.suit == "H":
			return "red"
		else:
			return "black"

	def getValue(self):
		return self.value

	def __str__(self):
		return str(self.value) + self.suit

	def __repr__(self):
		rv =  "Card(" + str(self.value)
		rv += ", " + self.suit + ")"
		return rv

def main():
	a = Card("A", "S")
	print(a)
	print(repr(a))
	print(a.getColor())

	t = Card(10, "H")
	print(t)
	print(repr(t))
	print(t.getColor())

if __name__ == "__main__":
	main()
