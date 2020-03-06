import pygame, time
class Grid(object):
	"""

	"""
	def __init__(self, color, width, height):
		self.color = color
		self.width = width
		self.height = height
		self.grid = []


	def create_grid(self, surface, margin, row, column, posX, posY):
		posx = posX
		posy = posY
		for r in range(row):
			posx += self.width + margin
			posy = posY
			self.grid.append([])
			for c in range(column):
				posy += self.height + margin
				box = Box(self.color, posx, posy, self.width, self.height)
				self.grid[r].append(box)
				

	def draw_grid(self, surface):
		for r in range(len(self.grid[0])):
			for c in range(len(self.grid[r])):
				pygame.draw.rect(surface, self.grid[r][c].color,
					(self.grid[r][c].posy, self.grid[r][c].posx, self.grid[r][c].width, self.grid[r][c].height))

	def change_colors(self, color, surface):
		dead = False
		i =  0
		j = 0
		while(not dead):
			if i < len(self.grid):
				if j < len(self.grid[i]):
					self.grid[i][j].color = color
					self.draw_grid(surface)
					pygame.display.update()
					j += 1
				elif j == len(self.grid[i]):
					j = 0
					i += 1
			elif i == len(self.grid):
				dead = True

			pygame.time.delay(5)







class Box(object):

	def __init__(self, color, posx, posy, width, height):
		self.color = color
		self.posx = posx
		self.posy = posy
		self.width = width
		self.height = height