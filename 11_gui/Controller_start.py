import pygame
import Hero
import Bullet

class GUI:
    def __init__(self, width=640, height=480):
        """This is the Main Loop of the Game"""
        #pygame handles the the view and the below sets everything up
        self.screen = pygame.display.set_mode((width, height))
        self.background = pygame.Surface(self.screen.get_size()).convert()
        #initialize hero object
        self.hero = Hero.Hero()
        self.sprites = pygame.sprite.Group((self.hero,))
        #initialize bullet group
        self.bullets = pygame.sprite.Group()
        done = False

    def mainloop(self):
        #GUIController continued(a.k.a. the main loop)
        while not done:
            for event in pygame.event.get():
                #event loop

            #update state


            #redraw the entire screen


            pygame.display.flip()
