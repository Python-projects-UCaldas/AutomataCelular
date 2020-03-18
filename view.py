import const as c
from automata import Automata
from grid import Grid
import pygame
import sound
import sys

class pygWindow:
    def __init__(self, timer, base, rule, state1, state2, state3, instruments, limit):
        pygame.init()
        pygame.display.set_caption('Automata')
        self.surface = pygame.display.set_mode((c.WIDTH, c.HEIGHT))
        self.surface.fill(c.BLACK)        

        self.grid = Grid(20, 20, 40, 10, 15, 15)
        self.grid2 = Grid(300, 20, 40, 10, 15, 15)
        self.grid3 = Grid(580, 20, 40, 10, 15, 15)

        self.instruments = instruments

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
            i2 = self.automata2.phrase[self.iterator]
            i3 = self.automata3.phrase[self.iterator]
        else:
            i1 = i2 = i3 = 0

        print(i1, i2, i3)
        aux1 = False #if i1 was used
        aux2 = False #if i2 was used
        aux3 = False #if i3 was used
        if 'Bamboo' in self.instruments:
            pygame.mixer.Channel(0).play(sound.bamboo[i1])
            aux1 = True
        if 'Bass' in self.instruments:
            if not aux1:
                pygame.mixer.Channel(1).play(sound.bass[i1])
                aux1 = True
            elif not aux2:
                pygame.mixer.Channel(1).play(sound.bass[i2])
                aux2 = True
            elif not aux3:
                pygame.mixer.Channel(1).play(sound.bass[i3])
                aux3 = True
        if 'Bell' in self.instruments:
            if not aux1:
                pygame.mixer.Channel(2).play(sound.bell[i1])
                aux1 = True
            elif not aux1:
                pygame.mixer.Channel(2).play(sound.bell[i2])
                aux2 = True
            elif not aux1:
                pygame.mixer.Channel(2).play(sound.bell[i3])
                aux3 = True
        if 'Flute' in self.instruments:
            if not aux1:
                pygame.mixer.Channel(3).play(sound.flute[i1])
                aux1 = True
            elif not aux2:
                pygame.mixer.Channel(3).play(sound.flute[i2])
                aux2 = True
            elif not aux3:
                pygame.mixer.Channel(3).play(sound.flute[i3])
                aux3 = True
        if 'Guitar' in self.instruments:
            if not aux1:
                pygame.mixer.Channel(4).play(sound.guitar[i1])
                aux1 = True
            elif not aux2:
                pygame.mixer.Channel(4).play(sound.guitar[i2])
                aux2 = True
            elif not aux3:
                pygame.mixer.Channel(4).play(sound.guitar[i3])
                aux3 = True
        if 'MusicBox' in self.instruments:
            if not aux1:
                pygame.mixer.Channel(5).play(sound.musicBox[i1])
                aux1 = True
            elif not aux2:
                pygame.mixer.Channel(5).play(sound.musicBox[i2])
                aux2 = True
            elif not aux3:
                pygame.mixer.Channel(5).play(sound.musicBox[i3])
                aux3 = True
        if 'Synthesizer' in self.instruments:
            if not aux1:
                pygame.mixer.Channel(6).play(sound.synthesizer[i1])
                aux1 = True
            elif not aux2:
                pygame.mixer.Channel(6).play(sound.synthesizer[i2])
                aux2 = True
            elif not aux3:
                pygame.mixer.Channel(6).play(sound.synthesizer[i3])
                aux3 = True
        if 'Triangles' in self.instruments:
            if not aux1:
                pygame.mixer.Channel(7).play(sound.triangles[i1])
                aux1 = True
            elif not aux2:
                pygame.mixer.Channel(7).play(sound.triangles[i2])
                aux2 = True
            elif not aux3:
                pygame.mixer.Channel(7).play(sound.triangles[i3])
                aux3 = True
        if 'Violin' in self.instruments:
            if not aux1:
                pygame.mixer.Channel(8).play(sound.violin[i1])    
                aux1 = True
            elif not aux2:
                pygame.mixer.Channel(8).play(sound.violin[i2])
                aux2 = True
            elif not aux3:
                pygame.mixer.Channel(8).play(sound.violin[i3])
                aux3 = True
        if 'Voice' in self.instruments:
            if not aux1:
                pygame.mixer.Channel(9).play(sound.voice[i1])
                aux1 = True
            elif not aux2:
                pygame.mixer.Channel(9).play(sound.voice[i2])
                aux2 = True
            elif not aux3:
                pygame.mixer.Channel(9).play(sound.voice[i3])
                aux3 = True
