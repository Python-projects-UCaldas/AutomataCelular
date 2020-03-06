##############################IMPORTS##############################

import sys, pygame, itertools, random, time
from threading import Thread
from PyQt5.QtWidgets import QApplication,QMainWindow,QMessageBox
from pygame.locals import *
from PyQt5 import uic, QtCore, Qt
from grid import *
from box import *

##############################GLOBALS##############################

black = (0, 0, 0)
purple = (255, 0, 255)
white = (255, 255, 255)
green = ( 0, 255, 0)
red = (255, 0, 0)

##############################INTERFACE##############################

class WindowPQ(QMainWindow):	
	
	def __init__(self):
	
		#iniciar pbjeto QMainWindow
		QMainWindow.__init__(self)
		#Cargar archivo
		uic.loadUi("Automata.ui",self)
		
		self.initUI()


	def initUI(self):
		self.inputRegla.text()
		self.start.clicked.connect(lambda:self.pygameWindow())	
	

	def pygameWindow(self):
		
		pygame.init()
		
		pygameWindowSize = [1200, 800]
		pygameScreen = pygame.display.set_mode(pygameWindowSize)
		pygame.display.set_caption("Animación Automata Celular")
		done = False
		clock = pygame.time.Clock()
		box1 = Box(10, 10, 20, 20, white, 2)
		box2 = Box(350, 10, 20, 20, red, 2)
		grid1 = Grid(10, 28, 5, box1)
		grid2 = Grid(10, 28, 5, box2)
		grid1.draw_grid(pygameScreen)
		grid2.draw_grid(pygameScreen)
		box_list1 = grid1.positions(pygameScreen)
		box_list2 = grid2.positions(pygameScreen)
		print('positions grid1: ','\n',
			box_list1, '\n', '\n','\n',
			'positions grid2: ','\n', box_list2)

		################# PYGAME MAIN LOOP #################

		while not done:
		    for event in pygame.event.get(): 
		        if event.type == pygame.QUIT: 
		            done = True
		        elif event.type == pygame.MOUSEBUTTONDOWN:
		        	pos = pygame.mouse.get_pos()
		        	print("Click ", pos)
		        elif event.type == pygame.KEYDOWN:
		        	if event.key == K_r:
		        		t1 = Thread(target = grid1.repaint_grid, name = 'thread1', 
		        		args = (pygameScreen, green, box_list1, box1, 3)) # Create the thread
			        	t1.daemon = True
			        	t1.start() #To initialize the thread
			        	"""To kill the thread when the program stops,
			        	 False the thread will not stop will not stop at the same time the program does"""
			        	'''t2 = Thread(target = grid1.draw_grid, name = 'thread2', 
		        		args = (pygameScreen))
			        	t2.daemon = True
			        	t2.start()'''
		        		 
		    clock.tick(60)

		    pygame.display.flip()

		pygame.quit()

##############################METHODS##############################

	def initProblem(self, limit, rule, base):
		"""

		"""
		iter = [i for i in range(base)]
		if rule is None:
			rule = [random.randint(0, len(iter)-1) for i in (range(0, limit))]
		states = itertools.product(iter, repeat=3)
		states = set(x)
		instrument1 = [[]]
		instrument2 = [[]]
		instrument3 = [[]]
		next_states = dict(zip(sorted(states),rule))	
'''
def convertTobase (num, base):
    if num == 0:
        return '0'
    nums = []
    while num:
        num, r = divmod(num, base)
        nums.append(str(r))
    return  ''.join(reversed(nums))

regla = convertTobase(25,5)
´'''

app=QApplication(sys.argv)
_window=WindowPQ() 
_window.show()
app.exec_() 
