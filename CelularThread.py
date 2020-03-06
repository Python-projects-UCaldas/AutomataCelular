import sys, pygame, itertools, random, time
from threading import Thread
from PyQt5.QtWidgets import QApplication,QMainWindow,QMessageBox
from PyQt5 import uic, QtCore, Qt
from grid import *

##############################INTERFACE##############################

NEGRO = (0, 0, 0)
MORADO = (255, 0, 255)
BLANCO = (255, 255, 255)
VERDE = ( 0, 255, 0)
ROJO = (255, 0, 0)
LARGO  = 20
ALTO = 20
MARGEN = 5

class Ventana(QMainWindow):
	

	
	def __init__(self):
	
		#iniciar pbjeto QMainWindow
		QMainWindow.__init__(self)
		#Cargar archivo
		uic.loadUi("Automata.ui",self)
		
		self.initUI()


	def initUI(self):
		self.inputRegla.text()
		self.start.clicked.connect(lambda:self.pygameWindow())
	
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

	def pygameWindow(self):
		
		pygame.init()
		
		DIMENSION_VENTANA = [1200, 800]
		pantalla = pygame.display.set_mode(DIMENSION_VENTANA)
		pygame.display.set_caption("Animación Automata Celular")
		hecho = False
		reloj = pygame.time.Clock()
		grid = Grid(BLANCO, 20, 20)
		grid.create_grid(pantalla, 5, 28, 10, 10, 10)
		grid2 = Grid(VERDE, 20, 20)
		grid2.create_grid(pantalla, 5, 28, 10, 10, 295)
		grid3 = Grid(ROJO, 20, 20)
		grid3.create_grid(pantalla, 5, 28, 10, 10, 580)
		grid4 = Grid(MORADO, 20, 20)
		grid4.create_grid(pantalla, 5, 28, 10, 10, 865)

		cambiar = False
		# -------- Bucle Principal del Programa-----------
		while not hecho:
		    for evento in pygame.event.get(): 
		        if evento.type == pygame.QUIT: 
		            hecho = True
		        elif evento.type == pygame.MOUSEBUTTONDOWN:
		        	pos = pygame.mouse.get_pos()
		        	print("Click ", pos)
		        	if cambiar == False:
			        	t1 = Thread(target = grid.change_colors, name = 'thread1', args = (NEGRO, pantalla)) # Create the thread
			        	t1.daemon = True #To kill the thread when the program stops,if False the thread will not stop will not stop at the same time the program does
			        	
			        	t2 = Thread(target = grid2.change_colors, name = 'thread2', args = (NEGRO, pantalla)) # Create the thread
			        	t2.daemon = True #To kill the thread when the program stops,if False the thread will not stop will not stop at the same time the program does
			        	
			        	t3 = Thread(target = grid3.change_colors, name = 'thread3', args = (NEGRO, pantalla)) # Create the thread
			        	t3.daemon = True #To kill the thread when the program stops,if False the thread will not stop will not stop at the same time the program does
			        	
			        	t4 = Thread(target = grid4.change_colors, name = 'thread4', args = (NEGRO, pantalla)) # Create the thread
			        	t4.daemon = True #To kill the thread when the program stops,if False the thread will not stop will not stop at the same time the program does
			        	t1.start() #To initialize the thread
			        	print("Hello1")
			        	t2.start() #To initialize the thread
			        	print("Hello2")
			        	t3.start() #To initialize the thread
			        	print("Hello3")
			        	t4.start() #To initialize the thread
			        	print("Hello4")
			        	print(t1.name)

			        	cambiar = True


		    pantalla.fill(NEGRO)
		    grid.draw_grid(pantalla)
		    grid2.draw_grid(pantalla)
		    grid3.draw_grid(pantalla)
		    grid4.draw_grid(pantalla)

		     
		    reloj.tick(60)

		    pygame.display.flip()

		pygame.quit()

##############################METODOS##############################

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
	

	##############################GRAFICOS##############################

	
#Iniciar Aplicacion
app=QApplication(sys.argv)
#Crear objeto clase
_ventana=Ventana() 
#Mostrar ventana
_ventana.show()
app.exec_() 
