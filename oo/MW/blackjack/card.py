# valid suits: "H", "D", "S", "C"
class Card:
	def __init__(self, suit, value):
		self.suit = suit
		self.value = value

	def getColor(self):
		if self.suit == "H" or self.suit == "D":
			return "red"
		else:
			return "black"

	def __str__(self):
		return self.suit + str(self.value)

	def __repr__(self):
		rv = "Card(\"" + self.suit + "\", "
		rv += str(self.value) + ")"
		return rv
