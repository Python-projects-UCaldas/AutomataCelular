import sys
import pygame
import itertools
import random
import time
from threading import Thread
import sys
import pygame
import itertools
import random
import time
from threading import Thread
from PyQt5.QtWidgets import QApplication,QMainWindow,QMessageBox
from PyQt5 import uic, QtCore, Qt

##############################INTERFACE##############################
global NEGRO, BLANCO, VERDE, ROJO
NEGRO = (0, 0, 0)
BLANCO = (255, 0, 255)
VERDE = ( 0, 255, 0)
ROJO = (255, 0, 0)

class Grid:
	def __init__(self, posX, posY, width, height):
		self.posX = posX
		self.posY = posY
		self.width = width
		self.height = height
		self.grid = []

	def draw_grid(self, pantalla, MARGEN, LARGO, ALTO):
		
		for fila in range(30):
		        for columna in range(10):
		            color = BLANCO
		            if self.grid[fila][columna] == 1:
		                color = VERDE
		            pygame.draw.rect(pantalla,
		                             color,
		                             [(MARGEN+LARGO) * columna + MARGEN,
		                              (MARGEN+ALTO) * fila + MARGEN,
		                              LARGO,
		                              ALTO])

	def create_grid(self, LARGO, ALTO):
		for fila in range(LARGO):
		    # Añadimos un array vacío que contendrá cada celda 
		    # en esta fila
		    self.grid.append([])
		    for columna in range(ALTO):
		        self.grid[fila].append(0) # Añade una celda


class Ventana(QMainWindow):
	

	
	def __init__(self):
	
		#iniciar pbjeto QMainWindow
		QMainWindow.__init__(self)
		#Cargar archivo
		uic.loadUi("Automata.ui",self)
		
		self.initUI()


	def initUI(self):
		self.inputRegla.text()
		self.regla.clicked.connect(lambda:self.pygameWindow())
	
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
		# Definimos algunos colores
		
		 
		# Establecemos el LARGO y ALTO de cada celda de la retícula.
		LARGO  = 20
		ALTO = 20
		 
		# Establecemos el margen entre las celdas.
		MARGEN = 5
		 
		# Creamos un array bidimensional. Un array bidimensional
		# no es más que una lista de listas.

		 
		# Establecemos la fila 1, celda 5 a uno. (Recuerda, los números de las filas y
		# columnas empiezan en cero.)
		#grid[1][5] = 1
		 
		# Inicializamos pygame
		pygame.init()
		  
		# Establecemos el LARGO y ALTO de la pantalla
		DIMENSION_VENTANA = [800, 800]
		pantalla = pygame.display.set_mode(DIMENSION_VENTANA)
		 
		# Establecemos el título de la pantalla.
		pygame.display.set_caption("Animación Automata Celular")
		 
		# Iteramos hasta que el usuario pulse el botón de salir.
		hecho = False
		 
		# Lo usamos para establecer cuán rápido de refresca la pantalla.
		reloj = pygame.time.Clock()
		 
		# -------- Bucle Principal del Programa-----------
		while not hecho:
		    for evento in pygame.event.get(): 
		        if evento.type == pygame.QUIT: 
		            hecho = True
		        elif evento.type == pygame.MOUSEBUTTONDOWN:
		            # El usuario presiona el ratón. Obtiene su posición.
		            pos = pygame.mouse.get_pos()
		            # Cambia las coordenadas x/y de la pantalla por coordenadas reticulares
		            columna = pos[0] // (LARGO + MARGEN)
		            fila = pos[1] // (ALTO + MARGEN)
		            # Establece esa ubicación a cero
		            grid[fila][columna] = 1
		            print("Click ", pos, "Coordenadas de la retícula: ", fila, columna)
		 
		    # Establecemos el fondo de pantalla.
		    pantalla.fill(NEGRO)
		 
		    # Dibujamos la retícula
		    grid1 = Grid(0, 30, 10, 50)
		    grid2 = Grid(300, 30, 10, 50)
		    grid3 = Grid(600, 30, 10, 50)
		    
		    grid1.draw_grid(pantalla, MARGEN, LARGO, ALTO)
		    grid2.draw_grid(pantalla, MARGEN, LARGO, ALTO)
		    grid3.draw_grid(pantalla, MARGEN, LARGO, ALTO)
		     
		    # Limitamos a 60 fotogramas por segundo.
		    reloj.tick(60)
		 
		    # Avanzamos y actualizamos la pantalla con lo que hemos dibujado.
		    pygame.display.flip()
		     
		# Pórtate bien con el IDLE.
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
