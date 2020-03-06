import pygame
from box import *

class Grid(object):
	""""""
	def __init__(self, color, rows, columns, box):
		self.color = color
		self.rows = rows
		self.columns = columns
		self.box = Box(box.getLeft(), box.getTop(), box.getHeight(), box.getWidth(), box.getColor(), box.getValue())
		
	def draw_grid(self, surface, margin):
		posx = self.box.getLeft()
		posy = self.box.getTop()
		box_list = {}
		for r in range(self.rows):
			posx += self.box.getWidth() + margin
			posy = self.box.getTop()
			for c in range(self.columns):
				posy += self.box.getHeight() + margin
				newBox = Box(posx, posy, self.box.getWidth(), self.box.getHeight(), self.box.getColor(), self.box.getValue())
				pygame.draw.rect(surface, newBox.getColor(), (newBox.getLeft(),newBox.getTop(), newBox.getHeight(), newBox.getWidth()))
				box_list[(posx, posy)] = 0
		return box_list


	def positions(self, row, column, margin):
		positions = {}
		posx = self.left
		posy = self.top
		for r in range(row):
			posx += self.width + margin
			posy = self.top
			for c in range(column):
				posy += self.height + margin
				positions[posx, posy] = 0
		return positions