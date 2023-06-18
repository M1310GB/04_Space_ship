import random
from pygame.sprite import Sprite
from game.utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT
#from game.components.power_ups.power_up_manager import PowerUpManager

class PowerUp (Sprite):
    def __init__(self, image, type):
        self.image = image
        self.type = type
        self.rect = self.image.get_rect()

        self.y = 0
        self.x = random.randint (120, SCREEN_WIDTH -120) 
        

        self.rect.x = random.randint (120, SCREEN_WIDTH -120)
        self.rect.y = 0

        self.start_time = 0
        
    def update (self, game_speed, power_ups):
        self.rect.y += game_speed
        if self.rect.y <0 or self.rect.y >= SCREEN_HEIGHT:
            power_ups.remove(self)
            self.rect.x = random.randint (120, SCREEN_WIDTH -120)
            self.rect.y = 0  

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def reset_pos(self):
        PowerUp.x = random.randint (120, SCREEN_WIDTH -120)
        PowerUp.y = 0