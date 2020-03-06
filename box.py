import pygame

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

"""

"""