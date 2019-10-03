import pygame
#model
class Hero:
    def __init__(self, attr):
        self.image = Surface('hero.png')
        #get the rectangle for positioning
        self.rect = Rectangle()
        self.strength, self.intel, self.speed = attr

#methods to make moving our hero easier
    def move(self):
        pass

    def fight(self, opponent):
        return random.choice([True, False])
