import pygame

class Block(pygame.sprite.Sprite):
    def __init__(self, x=0,y=0):
        pygame.sprite.Sprite.__init__(self)
        self.x=x
        self.y=y
        self.size=10
        self.image = pygame.Surface((self.size, self.size))
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.live=False

    def update(self):
        if(self.live):
            self.image.fill((255, 255, 0))
        else:
            self.image.fill((255, 255, 255))

    def __str__(self):
        objstr = "X: " + str(self.x) + ", "
        objstr += "Y: " + str(self.y) + ", "
        objstr += "size: " + str(self.size) + ", "
        objstr += "live?: " + str(self.live) + ", "
        return objstr
