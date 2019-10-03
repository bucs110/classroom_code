import pygame
#model
class Hero(pygame.sprite.Sprite):
    def __init__(self):
        #initialize all the Sprite functionality
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('hero.png')
        #get the rectangle for positioning
        self.rect = self.image.get_rect()
        self.direction = "right"
        self.strength, self.intel, self.speed = (2,3,5)

#methods to make moving our hero easier
    def move_up(self):
        self.rect.y -= 3
    def move_down(self):
        self.rect.y += 3
    def move_left(self):
        self.rect.x -= 3
        if(self.direction == "right"):
            self.direction = "left"
            self.image = pygame.transform.flip(self.image, True, False)
            #self.rect = self.image.get_rect()
    def move_right(self):
        self.rect.x += 3
        if(self.direction == "left"):
            self.direction = "right"
            self.image = pygame.transform.flip(self.image, True, False)
            #self.rect = self.image.get_rect()
    def fight(self, opponent):
        return random.choice([True, False])
