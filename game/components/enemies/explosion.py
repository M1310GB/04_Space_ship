import pygame
from pygame.sprite import Sprite
from game.utils.constants import EXPLOSION

class Explosion:
    def __init__(self):
        self.image = EXPLOSION
        self.image = pygame.transform.scale(self.image, (90,90))
        self.rect = self.image.get_rect()
        self.rect.x 
        self.rect.y  
        self.type = "explosion"

    def draw(self, screen):
        screen.blit(self.image,(self.rect.x, self.rect.y))