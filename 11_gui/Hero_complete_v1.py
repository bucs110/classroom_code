import pygame

class Hero(pygame.sprite.Sprite):
    def __init__(self, name, pos, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.name = name
        self.name = name
        self.rect.x, self.rect.y = pos #(2,3)
        self.strength, self.intel, self.speed = (2,3,5)

    def move(self, direction):
        if(direction.lower() == "down"):
            self.rect.y -= self.speed
        if(direction.lower() == "up"):
            self.rect.y += self.speed
        if(direction.lower() == "left"):
            self.rect.x -= self.speed
        if(direction.lower() == "right"):
            self.rect.x += self.speed

    def fight(self, opponent):
        return random.choice([True, False])
