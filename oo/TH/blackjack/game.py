from deck import Deck
from card import Card
from participant import Participant

def main():
	d = Deck()
	d.shuffle()

	player = Participant()
	dealer = Participant()

	for i in range(2):
		player.addToHand(d.draw())
		dealer.addToHand(d.draw())

	print(player)
	print(dealer)
	print(d)

if __name__ == "__main__":
	main()
