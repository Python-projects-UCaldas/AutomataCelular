import pygame
class Grid(object):
	"""

	"""
	def __init__(self, color, width, height):
		self.color = color
		self.width = width
		self.height = height

	def draw_grid(self, surface, margin, row, column, posX, posY):
		posx = posX
		posy = posY
		for r in range(row):
			posx += self.width + margin
			posy = posY
			for c in range(column):
				posy += self.height + margin
				pygame.draw.rect(surface, self.color,
					(posy, posx, self.width, self.height))