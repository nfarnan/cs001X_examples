# valid suits: "H", "D", "S", "C"
class Card:
	def __init__(self, value, suit):
		self.value = value
		self.suit = suit

	def getColor(self):
		if self.suit == "H" or self.suit == "D":
			return "red"
		else:
			return "black"

	def getValue(self):
		return self.value

	def __str__(self):
		return str(self.value) + self.suit

	def __repr__(self):
		rv = "Card(\"" + str(self.value) + "\", "
		rv += self.suit + ")"
		return rv
