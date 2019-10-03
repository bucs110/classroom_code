import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, direction, x, y):
        #initialize all the Sprite functionality
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('bullet_left.png')
        #get the rectangle for positioning
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.direction = direction
        if(self.direction == "right"):
            self.image = pygame.transform.flip(self.image, True, False)

    def update(self):
        if(self.direction == "left"):
            self.rect.x -= 10
        elif(self.direction == "right"):
            self.rect.x += 10
