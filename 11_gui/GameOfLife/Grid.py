import Block
import random
import pygame
class Grid(pygame.sprite.Sprite):
    def __init__(self, row=25, column=25):
        pygame.sprite.Sprite.__init__(self)
        self.row = row
        self.column = column
        self.grid = [[Block.Block() for i in range(self.row)] for i in range(self.column)]
        y = 0
        self.blocks_group = pygame.sprite.Group()
        for i in self.grid:
            x = 0
            for j in i:
                j.x = x
                j.y = y
                x += j.size
            y += j.size
            self.blocks_group.add(i)
        self.image = pygame.Surface((self.row*self.grid[0][0].size, self.column*self.grid[0][0].size))
        self.rect = self.image.get_rect()

    def initRandom(self, seed):
        for i in self.grid:
            for j in i:
                if(random.randrange(seed) == 0):
                    j.live = True
    def update(self):
        self.blocks_group.update()


    def printGrid(self):
        for i in self.grid:
            print("|", end="", sep="")
            for j in i:
                if(j.live):
                    print("X", end="", sep="")
                else:
                    print(" ", end="", sep="")
            print("|")
