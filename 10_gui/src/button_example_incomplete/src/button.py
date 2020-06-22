import pygame

class Button(pygame.sprite.Sprite):
    def __init__(self, pos, fn):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(fn)
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[0]
        self.direction = 'l'

    def reset(self):
        self.rect.x = 250
        self.rect.y = 250

    def update(self):
        if self.rect.x > 350:
            self.direction = 'r'
        elif self.rect.x < 50:
            self.direction = 'l'

        if(self.direction == 'l'):
            self.rect.x += 1
        else:
            self.rect.x -= 1
