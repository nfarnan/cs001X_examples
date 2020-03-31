class Participant:
	def __init__(self):
		self.hand = []

	def addToHand(self, new_card):
		self.hand.append(new_card)

	def __str__(self):
		return "Cards in hand: \n" + str(self.hand)

	def __repr__(self):
		return self.__str__()
