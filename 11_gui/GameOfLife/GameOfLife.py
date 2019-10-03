import pygame
import Grid

class GameOfLife(pygame.sprite.Sprite):

    def __init__(self):
        self.grid = Grid.Grid()
        pygame.init()
        self.screen = pygame.display.set_mode((640, 480))
        self.background = pygame.Surface(self.screen.get_size()).convert()
        self.mainloop()

    def mainloop(self):
        self.background.fill((250, 250, 250))
         while True:
            #event loop here
            self.screen.blit(self.background, (0, 0))
            self.grid.update()
            pygame.display.flip()
