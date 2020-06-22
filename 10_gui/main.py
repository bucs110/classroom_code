import pygame

#models
class Button(pygame.sprite.Sprite):
    def __init__(self, pos, fn):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(fn)
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.range = 300

    def update(self):
        if(self.range > 0):
            self.rect.x += 1
            self.range -= 1
        else:
            self.rect.x -= 1
            self.range += 1

class Controller:
    def __init__(self):
        self.screen = pygame.display.set_mode((500, 500))
        self.background = pygame.Surface(self.screen.get_size())
        self.button = Button()

    def mainloop(self):
        while True:
            if self.STATE == "game":
                self.gameloop()
            elif self.STATE == "exit":
                self.exitloop()

    def gameloop(self):
        pygame.key.set_repeat(1, 50)
        while self.STATE == "game":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.hero.move("up")
                    elif event.key == pygame.K_DOWN:
                        self.hero.move("down")
                    elif event.key == pygame.K_LEFT:
                        self.hero.move("left")
                    elif event.key == pygame.K_RIGHT:
                        self.hero.move("right")
                    elif event.key == pygame.K_SPACE:
                        b = Bullet(self.hero.direction, self.hero.rect.centerx, self.hero.rect.centery)
                        self.bullets.add(b)
