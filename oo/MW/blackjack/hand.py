from card import Card

class Hand:
	def __init__(self):
		self.cards = []

	def add(self, new_card):
		self.cards.append(new_card)

	def countAces(self):
		count = 0
		for card in self.cards:
			if card.getValue() == "A":
				count += 1

		return count

	def getValue(self):
		total = 0

		points = {}
		for i in range(2, 11):
			points[i] = i
		for i in ["J", "Q", "K"]:
			points[i] = 10
		points["A"] = 11

		for card in self.cards:
			total += points[card.getValue()]

		aces = self.countAces()
		while total > 21 and aces > 0:
			total -= 10
			aces -= 1

		return total

	def __str__(self):
		rv = "Hand: (" + str(self.getValue()) + ")["
		for card in self.cards:
			rv += str(card)
			rv += ", "

		rv = rv.strip(", ")
		rv += "]"

		return rv

	def __repr__(self):
		return self.__str__()

def main():
	print("Initialinzing Hand object...")
	h = Hand()
	print(h)
	print("DONE")

	print("Adding cards to Hand...")
	h.add(Card(4, "H"))
	h.add(Card("Q", "S"))
	print(h)
	print("DONE")
	
if __name__ == "__main__":
	main()
