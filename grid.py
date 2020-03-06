import pygame, random
from box import *

class Grid(object):
	""""""
	def __init__(self, rows, columns, margin, box):
		self.color = box.getColor()
		self.rows = rows
		self.columns = columns
		self.margin = margin
		self.box = Box(box.getLeft(), box.getTop(), 
			box.getHeight(), box.getWidth(), 
			box.getColor(), box.getValue())
		
	def draw_grid(self, surface):
		posx = self.box.getLeft()
		posy = self.box.getTop()
		for r in range(self.rows):
			posx += self.box.getWidth() + self.margin
			posy = self.box.getTop()
			for c in range(self.columns):
				posy += self.box.getHeight() + self.margin
				newBox = Box(posx, posy, self.box.getWidth(), 
					self.box.getHeight(), self.box.getColor(),
					 self.box.getValue())
				pygame.draw.rect(surface, newBox.getColor(), 
					(newBox.getLeft(),newBox.getTop(), 
						newBox.getHeight(), newBox.getWidth()))

	def repaint_grid(self, surface, color, positions, box, value):

		for k, v in positions.items(): 
			if v == value:
				newBox = Box(tuple(k)[0], tuple(k)[1], self.box.getWidth(),
					self.box.getHeight(), color,
					value)
				pygame.draw.rect(surface, newBox.getColor(),
					(newBox.getLeft(),newBox.getTop(),
						newBox.getHeight(), newBox.getWidth()))

	def positions(self, surface):
		positions = {}
		posx = self.box.getLeft()
		posy = self.box.getTop()
		for r in range(self.rows):
			posx += self.box.getWidth() + self.margin
			posy = self.box.getTop()
			for c in range(self.columns):
				posy += self.box.getHeight() + self.margin
				newBox = Box(posx, posy, self.box.getWidth(), 
					self.box.getHeight(), self.box.getColor(),
					 self.box.getValue())
				positions[posx, posy] = random.randint(0,5)
		return positions