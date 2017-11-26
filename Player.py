class Player():
	def __init__(self):
		self.result = 0
		self.cards = []
		self.turn = False

	def count_result(self):
		self.result = 0
		for c in self.cards:
			self.result += c.value
		return self.result

	def show_cards(self):
		return self.cards

	def show_result(self):
		currect_result = 0
		for c in self.cards:
			currect_result += c.value
		return self.result

	def pickUpCard(self, card):
		self.cards.append(card)

	def show_turn(self):
		return self.turn
