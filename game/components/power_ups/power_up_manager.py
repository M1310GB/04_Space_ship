import pygame
import random
from game.components.power_ups.shield import Shield
from game.components.power_ups.speed_up import Speed
from game.utils.constants import SPACESHIP_SHIELD, SPACESHIP,FUEL, SPEED_TYPE,SCREEN_WIDTH,SPEED_EFFECT,SHIELD_EFFECT,FONT_STYLE2,SCREEN_HEIGHT

power_up_speed = Speed() 
power_up_shield = Shield()

class PowerUpManager:
    def __init__(self):
        self.power_ups = []
        self.when_appears = random.randint (5000, 10000)
        self.duration = random.randint (3,5)
        # self.power_up_speed = Speed() 
        # self.power_up_shield = Shield()


    def generate_power_up(self):

        self.when_appears += random.randint (5000, 10000)
        power_spawn = random.randint(1,2)
        if power_spawn == 1:
            self.power_ups.append(power_up_shield)
        elif power_spawn == 2:
            self.power_ups.append(power_up_speed)

    def update (self, game):
        current_time = pygame.time.get_ticks()

        if len(self.power_ups) == 0 and current_time >= self.when_appears:
            self.generate_power_up()

        for power_up in self.power_ups:
            power_up.update(game.game_speed, self.power_ups)

            if game.player.rect.colliderect(power_up) and power_up == power_up_shield:
                self.power_ups.remove(power_up)
                SHIELD_EFFECT.play()
                power_up.start_time = pygame.time.get_ticks()
                game.player.power_up_shield_active = True
                game.player.power_time_up = power_up.start_time + (self.duration * 1000)
                game.player.set_image((110,110), SPACESHIP_SHIELD)
                
                
            else:
                game.player.set_image((90,90), SPACESHIP)
                game.player.power_up_shield_active = False
                

            if game.player.rect.colliderect(power_up) and power_up == power_up_speed:
                self.power_ups.remove(power_up)
                SPEED_EFFECT.play()
                power_up.start_time = pygame.time.get_ticks()
                game.player.power_up_speed_active = True
                game.player.power_time_up = power_up.start_time + (self.duration * 1000)
                
                
            else: 
                game.player.power_up_speed_active = False

        

    def draw(self, screen,game):
        for power_up in self.power_ups:
            power_up.draw(screen)

        if game.player.power_up_speed_active == True:
            font = pygame.font.Font(FONT_STYLE2, 25)
            text =font.render("SPEED UP ACTIVATED",True,(255,255,255))
            text_rect = text.get_rect()
            text_rect.center = (SCREEN_WIDTH-250,50)
            game.screen.blit(text,text_rect)

        elif game.player.power_up_shield_active == True:
            font = pygame.font.Font(FONT_STYLE2, 25)
            text =font.render("PLASMA SHIELD ACTIVATED",True,(255,255,255))
            text_rect = text.get_rect()
            text_rect.center = (SCREEN_WIDTH-250,50)
            game.screen.blit(text,text_rect)

    def reset(self):
        now = pygame.time.get_ticks()
        self.power_ups = []
        self.when_appears = random.randint(5000, 10000)

        
        
        