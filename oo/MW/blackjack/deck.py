import random
from card import Card
import util

class Deck:
	def __init__(self):
		self.cards = []
		for suit in util.SUITS:
			for val in util.VALS:
				self.cards.append(Card(val, suit))

	def getLength(self):
		return len(self.cards)

	def shuffle(self):
		random.shuffle(self.cards)

	def draw(self):
		# approach 1
		#rv = self.cards[0]
		#self.cards = self.cards[1:]
		#return rv

		# approach 2
		return self.cards.pop()

	def __str__(self):
		return str(self.cards)

def main():
	d = Deck()
	print("Has", d.getLength(), "cards")
	print(d)

	print("Shuffling...")
	d.shuffle()
	print(d)

	print("Drawing...")
	print(d.draw())
	print(d)

if __name__ == "__main__":
	main()
