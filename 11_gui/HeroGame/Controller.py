import pygame
import Hero
import Bullet

class GUI:
    def __init__(self, width=640, height=480):
        """This is the Main Loop of the Game"""
        #pygame handles the the view and the below sets everything up
        self.screen = pygame.display.set_mode((width, height))
        self.background = pygame.Surface(self.screen.get_size()).convert()
        self.hero = Hero.Hero()
        self.sprites = pygame.sprite.Group((self.hero,))
        self.bullets = pygame.sprite.Group()
        self.done = False
        self.STATE = "menu"

    def mainloop(self):
        while (not done):
            if self.STATE == "menu":
                self.menuloop()
            elif self.STATE == "instructions":
                self.instructionsloop()
            else:
                self.gameloop()

    def menuloop(self):
        #initialization
        while self.STATE == "menu":
            for event in pygame.event.get():
                if event.type == "click instructions event":
                    self.STATE = "instructions"
                if event.type == "click game event":
                    self.STATE = "game"
                ...additional logic
            pygame.display.flip()

    def instructionsloop(self):
        #initialization
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type == pygame.KEYDOWN:
                    if(event.key == pygame.K_UP):
                        self.hero.move_up()
                    elif(event.key == pygame.K_DOWN):
                        self.hero.move_down()
                    elif(event.key == pygame.K_LEFT):
                        self.hero.move_left()
                    elif(event.key == pygame.K_RIGHT):
                        self.hero.move_right()
                    elif(event.key == pygame.K_SPACE):
                        b = Bullet.Bullet(self.hero.direction, self.hero.rect.centerx, self.hero.rect.centery)
                        self.bullets.add(b)
                        self.sprites.add(b)
            self.bullets.update()
            #redraw the entire screen
            self.screen.blit(self.background, (0, 0))
            self.sprites.draw(self.screen)
            1

    def gameloop(self):
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type == pygame.KEYDOWN:
                    if(event.key == pygame.K_UP):
                        self.hero.move_up()
                    elif(event.key == pygame.K_DOWN):
                        self.hero.move_down()
                    elif(event.key == pygame.K_LEFT):
                        self.hero.move_left()
                    elif(event.key == pygame.K_RIGHT):
                        self.hero.move_right()
                    elif(event.key == pygame.K_SPACE):
                        b = Bullet.Bullet(self.hero.direction, self.hero.rect.centerx, self.hero.rect.centery)
                        self.bullets.add(b)
                        self.sprites.add(b)
            self.bullets.update()
            #redraw the entire screen
            self.screen.blit(self.background, (0, 0))
            self.sprites.draw(self.screen)
            pygame.display.flip()
