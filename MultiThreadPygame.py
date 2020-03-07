import pygame,sys, random
from threading import Thread
from pygame.locals import *

pygame.init()
surface = pygame.display.set_mode((800,600))
pygame.display.set_caption("Threads test")

#COLORES
WHITE = (255,255,255)
BLACK = (0,0,0)

threads = [] #Lista que contiene todos los hilos creados en el ciclo
balls = [] #Lista que contiene las bolas creadas en el ciclo
killnum = 0 #Numero que indica cual es la bola que quiere detener
running = True #Estado de la ventana


#Bola que se ve moverse en la ventana
class Ball():
	def __init__(self, color, x, y, height, width, speedX, speedY):
		self.color = color
		self.x = x
		self.y = y
		self.height = height
		self.width = width
		self.speedX = speedX
		self.speedY = speedY
		self.dead = False

	"""	
	Método que será ejecutado como hilo para hacer el moviemiento de la ventana, el atributo dead indica cuando 
	queremos matar al hilo, el delay se representa en milisegundos
	"""
	def move(self, surface):
		self.dead = False
		while (not self.dead):
			if (self.x > 800) or (self.x < 0):
				self.speedX = self.speedX * -1
			if (self.y > 600) or (self.y < 0):
				self.speedY = self.speedY * -1
			self.x += self.speedX
			self.y += self.speedY
			#pygame.time.delay(0)

	#Método que dibuja la bola
	def draw(self, surface):
		pygame.draw.rect(surface, self.color, (self.x, self.y, self.height, self.width))


"""
Método que crea bolas la cantidad de bolas que desee, y las ubica aleatoriamente en un punto dentro de la ventana y
le asigna una velocidad en x y y entre -1 y 1. Crea un hilo con cada una de estas bolas y los hace mover.
"""
def createBalls(numBalls):
	for i in range(0, numBalls):
		ball = Ball(WHITE, random.randint(50,750), random.randint(50,550), 10, 10, random.choice([1,-1]), random.choice([1,-1]))
		balls.append(ball)
		#target: metodo que sera el hilo, name: nombre del hilo, args: argumentos del método
		process = Thread(target = ball.move, name = "Thread #"+str(i), args = (surface,))
		#daemon: indica si quiero que los hilos mueran cuando el programa se cierre
		process.daemon = True
		process.start()
		print(process.name+" created")
		threads.append(process)


createBalls(10)


while running:
	for event in pygame.event.get():
		if event.type == QUIT:
			running = False
			pygame.quit()
			sys.exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE: #Con el espacio mato los hilos en orden de creacion
				if killnum < len(balls):
					balls[killnum].dead = True
					killnum += 1

	surface.fill(BLACK)
	for ball in balls:
		ball.draw(surface) #Dibujamos las bolas creadas
	pygame.display.update()