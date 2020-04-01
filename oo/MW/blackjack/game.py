from deck import Deck
from hand import Hand

def main():
	d = Deck()
	d.shuffle()

	player_hand = Hand()
	dealer_hand = Hand()

	for i in range(2):
		player_hand.add(d.draw())
		dealer_hand.add(d.draw())

	print("Player's hand:")
	print(player_hand)
	print("Dealer's hand:")
	print(dealer_hand)

	while player_hand.getValue() < 21:
		choice = input("Would you like hit or stay? ")
		if choice == "hit":
			player_hand.add(d.draw())
			print("Player's hand:")
			print(player_hand)
		elif choice == "stay":
			break
		else:
			print("Invalid choice!")

	if player_hand.getValue() > 21:
		print("You lose! busted.")
	else:
		while dealer_hand.getValue() < 17:
			dealer_hand.add(d.draw())

		if dealer_hand.getValue() > 21:
			print("You win! Dealer busted.")
		else:
			if dealer_hand.getValue() < player_hand.getValue():
				print("You win!")
			elif dealer_hand.getValue() == player_hand.getValue():
				print("It's a draw!")
			else:
				print("You lose!")

	print("Player's hand:")
	print(player_hand)
	print("Dealer's hand:")
	print(dealer_hand)

if __name__ == "__main__":
	main()
