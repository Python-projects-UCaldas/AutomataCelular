import pygame, random
#lineas para hallar la ruta relativa
import os, sys
APP_FOLDER = os.path.dirname(os.path.realpath(sys.argv[0]))
os.chdir(APP_FOLDER)

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
	def __init__(self, rows, columns, margin, box,name):
		self.name=name
		self.sonidos={}
		self.loadSounds()
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
		lista = []
		lista2 = []
		for i in positions:
			lista.append(positions[i])
		for i in range(len(lista)):
			lista2.append(lista[0::self.columns])
			lista[self.columns::len(lista)-1]
			#print(lista2)
		for k, v in positions.items(): 
			if v == value:
				newBox = Box(tuple(k)[0], tuple(k)[1], self.box.getWidth(),
					self.box.getHeight(), color,
					random.randint(0,5))
				pygame.draw.rect(surface, newBox.getColor(),
					(newBox.getLeft(),newBox.getTop(),
						newBox.getHeight(), newBox.getWidth()))
				#aqui va la magia
				instrumento= self.sonidos.get(self.name)
				if instrumento:
					pygame.mixer.Sound(instrumento[random.randint(0,4)]).play()

				pygame.display.update()
				pygame.time.delay(10)
		

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

	def loadSounds(self):
			
			xilofone=[]
			xilofone.append(pygame.mixer.Sound("sounds/xilofone/A1.ogg"))
			xilofone.append(pygame.mixer.Sound("sounds/xilofone/B1.ogg"))
			xilofone.append(pygame.mixer.Sound("sounds/xilofone/C1.ogg"))
			xilofone.append(pygame.mixer.Sound("sounds/xilofone/D1.ogg"))
			xilofone.append(pygame.mixer.Sound("sounds/silence.ogg"))
			self.sonidos["xilofone"]=xilofone
			
			
			guitar=[]  
			guitar.append(pygame.mixer.Sound("sounds/guitar/130624_095333-[5].wav"))
			guitar.append(pygame.mixer.Sound("sounds/guitar/130624_095823-[4].wav"))
			guitar.append(pygame.mixer.Sound("sounds/guitar/130624_095938-[3].wav"))
			guitar.append(pygame.mixer.Sound("sounds/guitar/130624_100353-[5].wav"))
			guitar.append(pygame.mixer.Sound("sounds/silence.ogg"))
			self.sonidos["guitar"]=guitar
			
			saxo=[]
			saxo.append(pygame.mixer.Sound("sounds/saxo/316898__jaz-the-man-2__do.wav"))
			saxo.append(pygame.mixer.Sound("sounds/saxo/316902__jaz-the-man-2__la.wav"))
			saxo.append(pygame.mixer.Sound("sounds/saxo/316906__jaz-the-man-2__mi.wav"))
			saxo.append(pygame.mixer.Sound("sounds/saxo/316908__jaz-the-man-2__re.wav"))
			saxo.append(pygame.mixer.Sound("sounds/silence.ogg"))
			self.sonidos["saxo"]=saxo

			maracas=[]
			maracas.append(pygame.mixer.Sound("sounds/Maracas/LPSP_MARACAS_01.wav"))
			maracas.append(pygame.mixer.Sound("sounds/Maracas/LPSP_MARACAS_02.wav"))
			maracas.append(pygame.mixer.Sound("sounds/Maracas/LPSP_MARACAS_03.wav"))
			maracas.append(pygame.mixer.Sound("sounds/Maracas/LPSP_MARACAS_04.wav"))
			maracas.append(pygame.mixer.Sound("sounds/silence.ogg"))
			self.sonidos["maracas"]=maracas

