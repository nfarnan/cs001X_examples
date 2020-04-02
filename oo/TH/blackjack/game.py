from deck import Deck
from card import Card
from participant import Participant
from player import Player

def main():
	player = Player("Player")
	dealer = Participant("Dealer")

	playagain = "y"

	while not player.isBroke() and playagain == "y":
		print("You have $", player.getMoney(), sep="")
		bet = int(input("How much to bet? "))
		while bet > player.getMoney():
			print("Not enough to make that bet!")
			print("You have $", player.getMoney(), sep="")
			bet = int(input("How much to bet? "))

		d = Deck()
		d.shuffle()

		player.clearHand()
		dealer.clearHand()

		for i in range(2):
			player.addToHand(d.draw())
			dealer.addToHand(d.draw())

		print("Dealer's first card:")
		print(dealer.getFirstCard())
		print()
		print(player)
		print()

		choice = input("Would you like to hit or stay? ")
		while choice == "hit":
			player.addToHand(d.draw())
			print(player)

			if player.getHandValue() > 21:
				player.changeMoney(-bet)
				print()
				print("You lose! busted...")
				print()
				print(dealer)
				break
			elif player.getHandValue() == 21:
				break
			else:
				print()
				choice = input("Would you like to hit or stay? ")

		if player.getHandValue() <= 21:
			while dealer.getHandValue() <= 16:
				dealer.addToHand(d.draw())

			print()
			print(dealer)
			if dealer.getHandValue() > 21:
				player.changeMoney(bet)
				print()
				print("You won! Dealer busted...")
			else:
				if player.getHandValue() > dealer.getHandValue():
					player.changeMoney(bet)
					print()
					print("You won!")
				elif dealer.getHandValue() > player.getHandValue():
					player.changeMoney(-bet)
					print()
					print("You lost...")
				else:
					print()
					print("Its a draw!")

		playagain = input("Would you like to play again(y/n)? ")

if __name__ == "__main__":
	main()
