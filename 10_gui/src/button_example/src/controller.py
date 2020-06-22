import pygame
import src.button

class Controller:
    def __init__(self):
        self.display = pygame.display.set_mode((500, 500))
        self.background = pygame.Surface(self.display.get_size())
        self.button = src.button.Button((250, 250), "assets/button.png")
        self.STATE = "game"

    def mainloop(self):
        while True:
            if self.STATE == "game":
                self.gameloop()
            elif self.STATE == "exit":
                self.exitloop()

    def gameloop(self):
        while self.STATE == "game":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.STATE = "exit"
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.button.rect.x = 250
                        self.button.rect.y = 250
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if(self.button.rect.collidepoint(event.pos)):
                        self.STATE = "exit"
            self.button.update()
            self.display.fill((100, 15, 69))
            self.display.blit(self.button.image, (self.button.rect.x, self.button.rect.y))
            pygame.display.flip()

    def exitloop(self):
        pygame.quit()
        exit()
