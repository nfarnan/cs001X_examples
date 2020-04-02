from participant import Participant
from card import Card

class Player(Participant):
	def __init__(self, name):
		Participant.__init__(self, name)
		self.money = 100

	def getMoney(self):
		return self.money

	def changeMoney(self, change):
		self.money += change

	def isBroke(self):
		# Approach1
		#if self.money <= 0:
		#	return True
		#else
		#	return False

		# Approach2
		return self.money <= 0

def main():
	a = Player("Alice")
	a.addToHand(Card("A", "S"))
	a.addToHand(Card("J", "S"))
	print(a.countAces())
	print(a.getHandValue())
	print(a)
	print(a.getMoney())
	print(a.isBroke())
	a.changeMoney(100)
	print(a.getMoney())	
	print(a.isBroke())
	a.changeMoney(-50)
	print(a.getMoney())
	print(a.isBroke())
	a.changeMoney(-200)
	print(a.getMoney())
	print(a.isBroke())

if __name__ == "__main__":
	main()
