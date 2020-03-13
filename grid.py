import const as cons
import pygame

class Grid:
    def __init__(self, iniX, iniY, rows, cols, width, height, margin=5):
        self.iniX = iniX
        self.iniY = iniY
        self.rows = rows
        self.cols = cols
        self.width = width
        self.height = height
        self.margin = margin
        self.boxes = {}
        self.current_row = 0
        #self.paint_evt = pygame.USEREVENT + 1

    def draw_grid(self, surface):
        """
        Draws the initial grid.
        """
        y = self.iniY
        for r in range(self.rows):
            x = self.iniX
            for c in range(self.cols):
                self.boxes.update({(x, y): 0})
                pygame.draw.rect(surface, cons.WHITE, (x, y, self.width, self.height))
                x += self.width + self.margin
            y += self.height + self.margin
        pygame.display.update()

    def repaint_box(self, surface, i, color_key):
        """
        Repaints a single box of the grid.
        """
        x = (i+1)*self.width + (i+1)*self.margin
        y = (self.current_row+1)*self.height + (self.current_row+1)*self.margin
        pygame.draw.rect(surface, cons.color_keys[color_key], (x, y, self.width, self.height))
        pygame.display.update((x, y, self.width, self.height))
        i += 1
        return i

    def repaint_row(self, surface, color_key_list):
        """
        Repaints a row of the grid.

        Parameters
        ----------
        surface: pygame.display
            The target surface to paint.

        color_key_list: list
            The list which has the color keys to paint each box.

        Returns
        -------
        None.

        """
        for i in range(len(color_key_list)):
            x = (i+1)*self.width + (i+1)*self.margin
            y = (self.current_row+1)*self.height + (self.current_row+1)*self.margin
            color_key = color_key_list[i]
            color = cons.color_keys[color_key]
            pygame.draw.rect(surface, color, (x, y, self.width, self.height))
            pygame.display.update()
        self.current_row += 1