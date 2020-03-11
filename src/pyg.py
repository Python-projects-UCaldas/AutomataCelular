import const as c
from automata import Automata
from grid import Grid
import pygame
import sys

class pygWindow:
    def __init__(self, timer):
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

        self.automata = Automata(None, 5, 10, [0, 2, 0, 1, 0, 2, 3, 1, 4, 1])
        self.iterator = 0
        self.iterator2 = 14
        self.iterator3 = 28
        self.j = 0

        #self.automata = [[0, 1, 2, 4, 3, 4, 1, 1, 2, 0], [1, 1, 0, 4, 0, 3, 2, 1, 2, 1], [0, 1, 1, 1, 4, 4, 3, 2, 1, 0]]
        pygame.time.set_timer(self.repaint_evt, 100)

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
            else:
                pass
              
    def draw_stuff(self):
        if self.iterator < self.grid.cols:
            if self.iterator < len(self.automata.phrase):
                box_value = self.automata.phrase[self.iterator]
                self.iterator = self.grid.repaint_box(self.surface, self.iterator, box_value)
                self.iterator2 = self.grid2.repaint_box(self.surface, self.iterator2, box_value)
                self.iterator3 = self.grid3.repaint_box(self.surface, self.iterator3, box_value)

            if self.iterator == self.grid.cols:
                self.grid.current_row += 1
                self.grid2.current_row += 1
                self.grid3.current_row += 1
            
        else:
            self.iterator = 0
            self.iterator2 = 14
            self.iterator3 = 28
            self.automata.phrase = self.automata.get_next_phrase(self.automata.phrase)

def setup():
    """
    Instances the pygame window and creates the main loop.
    """
    window = pygWindow(0)
    window.grid.draw_grid(window.surface)
    window.grid2.draw_grid(window.surface)
    window.grid3.draw_grid(window.surface)

    while True:
        window.clock.tick(40)
        #window.draw_stuff()
        window.handle_events()

if __name__ == "__main__":
    setup()
