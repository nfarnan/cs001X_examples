from card import Card
import random
#from random import shuffle

VALUES = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
SUITS = ["C", "D", "H", "S"]

class Deck:
	def __init__(self):
		self.cards = []

		for suit in SUITS:
			for value in VALUES:
				self.cards.append(Card(value, suit))

	def shuffle(self):
		random.shuffle(self.cards)
		#shuffle(self.cards)

	def draw(self):
		# approach 1
		#card = self.cards[0]
		#self.cards = self.cards[1:]
		#return card

		# approach 2
		return self.cards.pop(0)

	def __str__(self):
		rv = str(len(self.cards)) + " cards in the deck:"
		rv += "\n" + str(self.cards)
		return rv

	def __repr__(self):
		return self.__str__()

def main():
	print("Initializing a new deck...")
	d = Deck()
	print(d)
	print("DONE!\n")

	print("Shuffling the deck...")
	d.shuffle()
	print(d)
	print("DONE!\n")

	print("Drawing 5 cards...")
	for i in range(5):
		new = d.draw()
		print(new)
	print("DONE!\n")

	print("End state of the deck:")
	print(d)

if __name__ == "__main__":
	main()
