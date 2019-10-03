import pygame
#hook

class Bullet:
    def __init__(self):
        self.image = pygame.Surface()
        self.rect = pygame.Rect()
    def update():
        self.rect.x += 1

def main():
    bullets = pygame.sprite.Group()
    for i in range(10):
        bullets.add(Bullet())
    bullets.draw()
    bullets.update()
    collide = bullets.spritecollide(hero)
    for b in collide:
        b.kill()
main()
