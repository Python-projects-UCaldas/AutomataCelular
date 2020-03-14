import const as c
from automata import Automata
from grid import Grid
import pygame
import sound
import sys

class pygWindow:
    def __init__(self, timer, base, rule, state1, state2, state3, instrument1, instrument2, instrument3, limit):
        pygame.init()
        pygame.display.set_caption('Automata')
        self.surface = pygame.display.set_mode((c.WIDTH, c.HEIGHT))
        self.surface.fill(c.BLACK)        

        self.grid = Grid(20, 20, 40, 10, 15, 15)
        self.grid2 = Grid(300, 20, 40, 10, 15, 15)
        self.grid3 = Grid(580, 20, 40, 10, 15, 15)

        self.clock = pygame.time.Clock()
        self.timer = timer
        self.repaint_evt = pygame.USEREVENT + 1
        self.sound_evt = pygame.USEREVENT + 2
        self.automata1 = Automata(rule, base, limit, state1)
        self.automata2 = Automata(rule, base, limit, state2)
        self.automata3 = Automata(rule, base, limit, state3)
        self.iterator = 0
        self.iterator2 = 14
        self.iterator3 = 28
        self.j = 0

        pygame.time.set_timer(self.repaint_evt, timer)
        pygame.time.set_timer(self.sound_evt, timer+2)

    def handle_events(self):
        """
        Handles all needed pygame events.
        """
        for evt in pygame.event.get():
            if evt.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evt.type == self.repaint_evt:
                self.draw_stuff()
            elif evt.type == self.sound_evt:
                self.play_sounds()
            else:
                pass
              
    def draw_stuff(self):
        """
        """
        if self.iterator < self.grid.cols:
            if self.iterator < len(self.automata1.phrase):
                box_value = self.automata1.phrase[self.iterator]
                self.iterator = self.grid.repaint_box(self.surface, self.iterator, box_value)
                self.iterator2 = self.grid2.repaint_box(self.surface, self.iterator2, box_value)
                self.iterator3 = self.grid3.repaint_box(self.surface, self.iterator3, box_value)
                #print(i1, i2, i3)
                #self.play_sounds(i1, i2, i3)

            if self.iterator == self.grid.cols:
                self.grid.current_row += 1
                self.grid2.current_row += 1
                self.grid3.current_row += 1
            
        else:
            self.iterator = 0
            self.iterator2 = 14
            self.iterator3 = 28
            self.automata1.phrase = self.automata1.get_next_phrase(self.automata1.phrase)
            self.automata2.phrase = self.automata1.get_next_phrase(self.automata2.phrase)
            self.automata3.phrase = self.automata1.get_next_phrase(self.automata3.phrase)

    def play_sounds(self):
        """
        """
        if self.iterator < len(self.automata1.phrase):
            i1 = self.automata1.phrase[self.iterator]
            i2 = self.automata1.phrase[self.iterator]
            i3 = self.automata1.phrase[self.iterator]
        else:
            i1 = i2 = i3 = 0
        pygame.mixer.Channel(0).play(sound.xilofone[i1])
        pygame.mixer.Channel(1).play(sound.guitar[i2])
        pygame.mixer.Channel(2).play(sound.maracas[i3])