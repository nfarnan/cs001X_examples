from card import Card

class Participant:
	def __init__(self, name):
		self.hand = []
		self.name = name

	def addToHand(self, new_card):
		self.hand.append(new_card)

	def clearHand(self):
		self.hand = []

	def getFirstCard(self):
		return self.hand[0]

	def countAces(self):
		count = 0
		for card in self.hand:
			if card.getValue() == "A":
				count += 1

		return count

	def getHandValue(self):
		points = {}

		for i in range(2, 11):
			points[i] = i
		for i in ["J", "Q", "K"]:
			points[i] = 10
		points["A"] = 11

		total = 0
		for card in self.hand:
			total += points[card.getValue()]

		aces = self.countAces()
		while total > 21 and aces > 0:
			total -= 10
			aces -= 1

		return total

	def __str__(self):
		rv = self.name + "'s hand(" + str(self.getHandValue())
		rv += "): \n" + str(self.hand)

		return rv

	def __repr__(self):
		return self.__str__()

def main():
	print("CREATING PARTICIPANT:")
	b = Participant("Bob")
	print(b)
	print("DONE")

	print("ADDING TO HAND:")
	b.addToHand(Card(7, "D"))
	b.addToHand(Card(7, "H"))
	print("Aces:", b.countAces())
	print("Total:", b.getHandValue())
	print(b)
	print("DONE")

	print("ADDING ACE:")
	b.addToHand(Card("A", "S"))
	print("Aces:", b.countAces())
	print("Total:", b.getHandValue())
	print(b)
	print("DONE")

	print("ADDING ANOTHER ACE:")
	b.addToHand(Card("A", "C"))
	print("Aces:", b.countAces())
	print("Total:", b.getHandValue())
	print(b)
	print("DONE")

	print("ANOTHER PARTICIPANT WITH 21:")
	a = Participant("Alice")
	a.addToHand(Card("Q", "D"))
	a.addToHand(Card("A", "D"))
	print("Aces:", a.countAces())
	print("Total:", a.getHandValue())
	print(a)
	print("DONE")

if __name__ == "__main__":
	main()
