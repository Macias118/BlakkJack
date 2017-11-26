from Card import *
import random

class Table():
	colors = ['s', 'k', 'p', 't']
	figures = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
	
	def __init__(self):
		self.deck = []

	def createDeck(self):
		for f in self.figures:
			for c in self.colors:
				self.deck.append(Card(f, c))

	def show(self, p, d):
		self.draw_table(p, d)

	def deal(self, p, d):
		p.cards.append(self.draw_card())
		p.cards.append(self.draw_card())

		d.cards.append(self.draw_card())
		d.cards.append(self.draw_card())

	def draw_card(self):
		card = random.choice(self.deck)
		self.deck.remove(card)
		return card

	def draw_table(self, p, d):
		print "Dealer"
		for c in d.show_cards():
			print c
		print "Result = {0}".format(d.count_result())

		print "Player"
		for c in p.show_cards():
			print c
		print "Result = {0}".format(p.count_result()) 

	def draw_edge(self):	
		pass
	def draw_row(self):
		pass

