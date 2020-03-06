import pygame, random

class Box(object):
	"""
	"""
	def __init__(self, left, top, width, height, color, value):
		self.color = color
		self.value = value
		self.rect = pygame.rect.Rect(left, top, width, height)

	def getRect(self):
		return self.rect

	def setRect(self, left, top, width, height):
		self.rect = pygame.rect.Rect(left, top, width, height)

	def getLeft(self):
		return self.rect.left

	def getTop(self):
		return self.rect.top

	def getWidth(self):
		return self.rect.width

	def getHeight(self):
		return self.rect.height

	def getColor(self):
		return self.color

	def getValue(self):
		return self.value

	def setLeft(self, left):
		self.left = left

	def setTop(self, top):
		self.top = top

	def setWidth(self, width):
		self.width = width

	def setHeight(self, height):
		self.height = height

	def setColor(self, color):
		self.color = color

	def setValue(self, value):
		self.value = value

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
