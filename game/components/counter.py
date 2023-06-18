import pygame
from game.utils.constants import FONT_STYLE
class Counter:
    def __init__(self):
        self.count = 0
    def update (self):
        self.count +=1

    def draw(self, screem):
        font = pygame.font.Font(FONT_STYLE, 30)
        text = font.render(f"Score: ") 