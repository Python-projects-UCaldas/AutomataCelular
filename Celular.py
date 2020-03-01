import sys
print(sys.path)
import pygame
import itertools
import random
import time
from threading import Thread

iter = [0, 1, 2, 3, 4]
x = itertools.combinations_with_replacement(iter, 3)
x = set(x)
piano = [random.randint(0, 4) for i in range(20)]
bateria = [random.randint(0, 4) for i in range(20)]
d = {valor: random.randint(0, 4) for valor in sorted(x)}

pygame.init()
background_colour = (255,255,255)
(width, height) = (800, 600)

a4 = pygame.mixer.Sound('C:\\Users\\pista\\Desktop\\automatas-master\\Sounds\\Piano-A4.ogg')
c4 = pygame.mixer.Sound('C:\\Users\\pista\\Desktop\\automatas-master\\Sounds\\Piano-C4.ogg')
d4 = pygame.mixer.Sound('C:\\Users\\pista\\Desktop\\automatas-master\\Sounds\\Piano-D#4.ogg')
f4 = pygame.mixer.Sound('C:\\Users\\pista\\Desktop\\automatas-master\\Sounds\\Piano-F#4.ogg')
'''
a7 = pygame.mixer.Sound('C:\\Users\\pista\\Desktop\\automatas-master\\Sounds\\t1.mp3')
c7 = pygame.mixer.Sound('C:\\Users\\pista\\Desktop\\automatas-master\\Sounds\\t2.mp3')
d7 = pygame.mixer.Sound('C:\\Users\\pista\\Desktop\\automatas-master\\Sounds\\t3.mp3')
f7 = pygame.mixer.Sound('C:\\Users\\pista\\Desktop\\automatas-master\\Sounds\\t4.mp3')
'''
def play_piano():
  print("piano")
  if len(piano) > 0:
    note = piano.pop()
    if note == 1:
      print("a4")
      a4.play()
    if note == 2:
      c4.play()
      print("c4")
    if note == 3:
      d4.play()
      print("d4")
    if note == 4:
      f4.play()
      print("f4")
  else:
    note = 0
'''
def play_drums():
  
  if len(bateria) > 0:
    note = bateria.pop()
    if note == 1:
      print("a4")
      a7.play()
    if note == 2:
      c7.play()
      print("c4")
    if note == 3:
      d7.play()
      print("d4")
    if note == 4:
      f7.play()
      print("f4")
  else:
    note = 0
'''
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Tutorial 1')
screen.fill(background_colour)
pygame.display.flip()
running = True
#vec = vec.reverse()
#hilo1 = Thread(target=play_drums)
hilo2 = Thread(target=play_piano)

while running:
  time.sleep(0.5)
  play_piano()
  #play_drums()
  
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

