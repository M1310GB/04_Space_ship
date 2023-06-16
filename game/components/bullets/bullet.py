import pygame
from pygame.sprite import Sprite

from game.utils.constants import BULLET_PLAYER, BULLET_ENEMY, SCREEN_HEIGHT

class Bullet(Sprite):
    X_POS = 80
    Y_POS = 310
    SPEED = 10
    BULLET_SIZE = pygame.transform.scale(BULLET_PLAYER, (15,40))
    BULLET_SIZE_ENEMY = pygame.transform.scale(BULLET_ENEMY, (15,40))
    BULLETS = { "player": BULLET_SIZE,
               "enemy": BULLET_SIZE_ENEMY}
    
    def __init__(self, spaceship):
        self.image = self.BULLETS[spaceship.type]
        self.rect = self.image.get_rect()
        self.rect.center = spaceship.rect.center
        self.owner = spaceship.type


    def update(self, bullets):

        if self.owner == "player":
            self.rect.y -= self.SPEED 
        else:
            self.rect.y += self.SPEED

        if self.rect.y <= 0 or self.rect.y >= SCREEN_HEIGHT or self.rect.y < 0:
            bullets.remove(self)

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))