class Card():
	def __init__(self, f, c):
		self.figure = f
		self.color = c
		tenValues = ['10', 'J', 'Q', 'K']
		if self.figure in tenValues:
			self.value = 10
		elif self.figure == 'A':
			self.value = 11
		else:
			self.value = int(self.figure)

	def __str__(self):
		return "{0}{1}".format(self.figure, self.color)
