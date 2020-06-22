import pygame

#model
class Hero(pygame.sprite.Sprite):
    def __init__(self, name, pos, image):
        #initialize all the Sprite functionality
        pygame.sprite.Sprite.__init__(self)
        pygame.font.init() # you have to call this at the start,
                        # if you want to use this module.
        self.name = name
        self.image = pygame.image.load(image)
        #get the rectangle for positioning
        self.rect = self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]
        self.direction = "right"
        self.strength, self.intel, self.speed = (2,3,5)

#methods to make moving our hero easier
    def move(self, direction):
        if(direction.lower() == "down"):
            self.rect.y += self.speed
        if(direction.lower() == "up"):
            self.rect.y -= self.speed
        if(direction.lower() == "left"):
            self.rect.x -= self.speed
            if(self.direction == "right"):
                self.direction = "left"
                self.image = pygame.transform.flip(self.image, True, False)
        if(direction.lower() == "right"):
            self.rect.x += self.speed
            if(self.direction == "left"):
                self.direction = "right"
                self.image = pygame.transform.flip(self.image, True, False)
                #self.rect = self.image.get_rect()

    def fight(self, opponent):
        return random.choice([True, False])

class Bullet(pygame.sprite.Sprite):
    def __init__(self, direction, x, y):
        #initialize all the Sprite functionality
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('bullet.png')
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

class Controller:
    def __init__(self, width=640, height=480):
        """This is the Main Loop of the Game"""
        #pygame handles the the view and the below sets everything up
        self.screen = pygame.display.set_mode((width, height))
        self.background = pygame.Surface(self.screen.get_size())
        self.width = width
        self.height = height
        #initialize hero object
        self.hero = Hero("Bob", (width/3, height/3), "hero.png")
        self.enemy = Hero("BadGuy", (width-100, height-150), "enemy.png")
        #initialize bullet group
        self.bullets = pygame.sprite.Group()
        self.STATE = "GAME"

    def mainLoop(self):
        while True:
            if(self.STATE == "GAME"):
                self.gameLoop()
            elif(self.STATE == "GAMEOVER"):
                self.gameOver()

    def gameLoop(self):
        """This is the Main Loop of the Game"""
        pygame.key.set_repeat(1,50)
        while self.STATE == "GAME":
            self.background.fill((100, 15, 69))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if(event.key == pygame.K_UP):
                        self.hero.move("up")
                    elif(event.key == pygame.K_DOWN):
                        self.hero.move("down")
                    elif(event.key == pygame.K_LEFT):
                        self.hero.move("left")
                    elif(event.key == pygame.K_RIGHT):
                        self.hero.move("right")
                    elif(event.key == pygame.K_SPACE):
                        b = Bullet(self.hero.direction, self.hero.rect.centerx, self.hero.rect.centery-10)
                        self.bullets.add(b)
            hits = pygame.sprite.spritecollide(self.enemy, self.bullets, True)
            if(hits):
                self.STATE = "GAMEOVER"
            self.bullets.update()
            self.screen.blit(self.background, (0, 0))
            self.bullets.draw(self.screen)
            self.screen.blit(self.hero.image, (self.hero.rect.x, self.hero.rect.y))
            self.screen.blit(self.enemy.image, (self.enemy.rect.x, self.enemy.rect.y))
            pygame.display.flip()

    def gameOver(self):
        self.hero.kill()
        myfont = pygame.font.SysFont(None, 30)
        message = myfont.render('Game Over', False, (0,0,0))
        self.screen.blit(message, (self.width/2,self.height/2))
        pygame.display.flip()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

#driver
def main():
    controller = Controller()
    controller.mainLoop()
main()
