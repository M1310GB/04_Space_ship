import random
from pygame.sprite import Sprite
from game.utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT,X_POWER_UP,Y_POWER_UP

class PowerUp(Sprite):
    def __init__(self, image, type):
        self.image = image
        self.type = type
        self.rect = self.image.get_rect()

        self.rect.x = X_POWER_UP
        self.rect.y = Y_POWER_UP

        self.start_time = 0
        
    def update (self, game_speed, power_ups): 
        self.rect.y += game_speed
        if self.rect.y <0 or self.rect.y >= SCREEN_HEIGHT - 20:
            power_ups.remove(self)
            self.rect.x = random.randint (120, SCREEN_WIDTH -120)
            self.rect.y = 0  


    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def reset(self):
        pass
