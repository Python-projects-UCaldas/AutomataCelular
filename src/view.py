import sys, pygame, random, time
from pygame.locals import *

from threading import Thread

from PyQt5.QtWidgets import QApplication,QMainWindow,QMessageBox
from PyQt5 import uic, QtCore, Qt

from grid import *

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
		self.inputRule.text()
		self.start.clicked.connect(lambda:self.pygameWindow())	
	

	def pygameWindow(self):
		
		pygame.init()
		
		pygameWindowSize = [1200, 800]
		pygameScreen = pygame.display.set_mode(pygameWindowSize)
		pygame.display.set_caption("Animación Automata Celular")
		done = False
		clock = pygame.time.Clock()
		box1 = Box(10, 10, 20, 20, white, 2)
		box2 = Box(295, 10, 20, 20, red, 2)
		box3 = Box(580, 10, 20, 20, green, 2)
		box4 = Box(875, 10, 20, 20, purple, 2)

		grid1 = Grid(10, 28, 5, box1)
		grid2 = Grid(10, 28, 5, box2)
		grid3 = Grid(10, 28, 5, box3)
		grid4 = Grid(10, 28, 5, box4)

		box_list1 = grid1.positions(pygameScreen)
		box_list2 = grid2.positions(pygameScreen)
		box_list3 = grid3.positions(pygameScreen)
		box_list4 = grid4.positions(pygameScreen)

		'''print('positions grid1: ','\n',
			box_list1, '\n', '\n','\n',
			'positions grid2: ','\n', box_list2)'''

		################# PYGAME MAIN LOOP #################

		while not done:
			grid1.draw_grid(pygameScreen)
			pygame.display.update()
			t1 = Thread(target = grid1.repaint_grid, name = 'thread1',
			args = (pygameScreen, green, box_list1, box1, 3)) # Create the thread
			t1.daemon = True
			t1.start()
			grid2.draw_grid(pygameScreen)
			pygame.display.update()
			t2 = Thread(target = grid2.repaint_grid, name = 'thread2',
			args = (pygameScreen, purple, box_list2, box2, 3)) # Create the thread
			t2.daemon = True
			t2.start()
			grid3.draw_grid(pygameScreen)
			pygame.display.update()
			t3 = Thread(target = grid3.repaint_grid, name = 'thread3',
			args = (pygameScreen, white, box_list3, box3, 3)) # Create the thread
			t3.daemon = True
			t3.start()
			grid4.draw_grid(pygameScreen)
			pygame.display.update()
			t4 = Thread(target = grid4.repaint_grid, name = 'thread4',
			args = (pygameScreen, red, box_list4, box4, 3)) # Create the thread
			t4.daemon = True
			t4.start()
			t1.join()
			t2.join()
			t3.join()
			t4.join()
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					done = True
				elif event.type == pygame.MOUSEBUTTONDOWN:
					pos = pygame.mouse.get_pos()
					print("Click ", pos)
			clock.tick(60)
			pygame.display.flip()

		pygame.quit()


app=QApplication(sys.argv)
_window=WindowPQ() 
_window.show()
app.exec_()
