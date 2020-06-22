import LEDLib
import pygame
#model
class Light(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("ledoff.jpg") #surface object
        self.rect = self.image.get_rect()

        self.led = LEDLib.LED()
        self.state = "off"

    def toggle(self):
        if self.state == "off":
            self.led.on()
            self.state = "on"
        else:
            self.led.off()
            self.state = "off"

    def update(self):
        if(self.state == "on"):
            self.image = pygame.image.load("ledon.jpg")
        else:
            self.image = pygame.image.load("ledoff.jpg")

#Controller
class GUI:
    def __init__(self):
        self.led1 = Light()
        self.led2 = Light()

        self.leds = pygame.sprite.Group( (self.led1, self.led2) )
        #self.leds.add(self.led3)
        self.screen = pygame.display.set_mode((width, height))
        self.status = "RUN"
        #...

    def mainloop(self):
        while self.status == "RUN":

            for event in pygame.event.get():
                if event == pygame.QUIT:
                    self.status = "EXIT"
                elif event == pygame.MOUSEBUTTONDOWN:
                    if self.led1.collide(event.pos):
                        self.led1.toggle()
                    elif self.led2.collide(event.pos):
                        self.led2.toggle()
            leds.update()
            self.screen.update()
