#coding: utf8
import random 
import time
import curses
import sys
import readchar
from Player import *
from Table import *

class Game():
	def __init__(self):
		self.cards = []
		self.create_pack_of_cards()
		self.create_players()
		self.deal_cards()
		self.turn = None

	def __unicode__(self, a):
		return a

	def check_cards(self):
		if not self.cards:
			self.create_pack_of_cards()

	def __str__(self):
		output = '\n'
		
		if self.turn == self.croupier:
			output += 'Croupier {0}\n'.format(self.croupier.count_result())
			for c in self.croupier.show_cards():
				output += str(c)
				if c != self.croupier.show_cards()[-1]:
					output += ' | '
				else:
					output += '\n'
		else:
			output += 'Croupier {0}\n'.format(self.croupier.cards[0].value)
			output += "{0} | X".format(self.croupier.cards[0])
		output += '\n\n'
		output += 'Player {0}\n'.format(self.player.count_result())
		for c in self.player.show_cards():
			output += str(c)
			if c != self.player.show_cards()[-1]:
				output += ' | '
			else:
				output += '\n'
		output += '\n'
		return output

	def create_pack_of_cards(self):
		colors = ['\xe2\x99\xa5', '\xe2\x99\xa6', '\xe2\x99\xa0', '\xe2\x99\xa3']
		figures = [
		'2', '3', '4', '5',
		'6', '7', '8', '9',
		'10', 'J', 'Q', 'K',
		'A'
		]
		for f in figures:
			for c in colors:
				self.cards.append(Card(f, c))

	def create_players(self):
		self.player = Player()
		self.croupier = Player()

	def deal_cards(self):
		self.player.cards = []
		self.croupier.cards = []
		for i in range(2):
			self.get_card(self.player)
		for i in range(2):
			self.get_card(self.croupier)

	def get_card(self, turn):
		self.check_cards()
		card = random.choice(self.cards)
		self.cards.remove(card)
		turn.cards.append(card)

	def show_table(self):
		print('Let\'s show who is winning...')
		#print(chr(27) + "[2J")	# clear screen
		print(self)

	def check_score(self):
		if self.player.count_result() == self.croupier.count_result():
			print('DRAW')
		elif self.player.count_result() > self.croupier.count_result():
			print('YOU WIN!')
		elif self.player.count_result() < self.croupier.count_result():
			print('YOU LOSE')

	def check_player_21(self):
		if self.player.count_result() == 21:
			return True
		return False

	def next_round(self):
		print('Next round started...')
		self.player.cards, self.croupier.cards = [], []
		self.deal_cards()
		self.turn = self.player

	def restart_game(self):
		self.next_round()

	def game_loop(self):
		responses = ['q', 'y', 'n']
		while True:
			self.show_table()
			print('\nDo You wanna get card? {0}'.format(responses))
			get_response = raw_input()

			if get_response == 'y':
				self.get_card(self.player)
				if self.check_player_21():
					print('Player Wins.')
				if self.player.count_result() > 21:
					print('Player loses.')
					self.next_round()
			elif get_response == 'n':
				self.turn = self.croupier
				if self.croupier.count_result() > 17:
					self.check_score()
				else:
					while self.croupier.count_result() < 17:
						self.get_card(self.croupier)
						time.sleep(1)
						self.show_table()
					self.check_score()
					self.show_table()
					self.next_round()
			elif get_response == 'q':
				print('Exiting now...Bye bye!')
				return False
				#exit()
			elif get_response == 'r':
				self.restart_game()
			else:
				print('Wrong answer...')

game = Game()
game.game_loop()