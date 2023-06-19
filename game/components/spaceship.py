import pygame
import random
from pygame.sprite import Sprite
from game.utils.constants import SPACESHIP, SCREEN_HEIGHT, SCREEN_WIDTH, DEFAULT_TYPE,BULLET_SOUND,SPACESHIP_LEFT,SPACESHIP_SPEED_LEFT,SPACESHIP_SHIELD_LEFT,SPACESHIP_RIGHT,SPACESHIP_SPEED_RIGHT,SPACESHIP_SHIELD_RIGHT,SPACESHIP_SPEED,SPACESHIP_SHIELD
from game.components.bullets.bullet import Bullet

class Spaceship(Sprite):
    X_POS = ( SCREEN_WIDTH // 2 ) - 40
    Y_POS = 500
    def __init__(self):
        self.image = SPACESHIP
        self.image = pygame.transform.scale(self.image, (90,90))
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.player = Spaceship
        self.type = "player"
        self.has_power_up = False
        self.power_time_up = 0
        self.power_up_speed_active = False
        self.power_up_shield_active = False
        self.ship_speed = 10


    def shoot(self, bullet_manager):
        bullet = Bullet(self)
        bullet_manager.add_bullet(bullet)

    def update(self, user_input, game):
        if game.player.power_up_speed_active == True:
            self.ship_speed = 20
        else:
            self.ship_speed = 10


    #MOVIMIENTO A LA IZQUIERDA
        if user_input[pygame.K_LEFT]:
            game.player.set_image((80,100), SPACESHIP_LEFT)
            self.move_left()
            if game.player.power_up_speed_active == True:
                game.player.set_image((90,100), SPACESHIP_SPEED_LEFT)
            if game.player.power_up_shield_active == True:
                game.player.set_image((90,100), SPACESHIP_SHIELD_LEFT)


    #MOVIMIENTO A LA DERECHA
        elif user_input[pygame.K_RIGHT]:
            game.player.set_image((80,100), SPACESHIP_RIGHT)
            self.move_right()
            if game.player.power_up_speed_active == True:
                game.player.set_image((80,100), SPACESHIP_SPEED_RIGHT)
            if game.player.power_up_shield_active == True:
                game.player.set_image((80,100), SPACESHIP_SHIELD_RIGHT)

    #SPRITE STANDAR CUANDO NO ESTAN MOVIENDOSE A LOS LADOS           
        else:
            if game.player.power_up_speed_active == True:
                game.player.set_image((90,90), SPACESHIP_SPEED)
            elif game.player.power_up_shield_active == True:
                game.player.set_image((90,90), SPACESHIP_SHIELD)
            else:
                game.player.set_image((90,90), SPACESHIP)



        if user_input[pygame.K_UP]:
            self.move_up()
        if user_input[pygame.K_DOWN]:
            self.move_down()
        if user_input[pygame.K_SPACE]:
            self.shoot(game.bullet_manager)
            
            

    def move_left(self):
        if self.rect.left > 0:
            self.rect.x = self.rect.x - self.ship_speed
        while self.rect.left == 0:
            self.rect.x = SCREEN_WIDTH - 60

    def move_right(self):
        if self.rect.right < SCREEN_WIDTH + 1:
            self.rect.x = self.rect.x + self.ship_speed
        while self.rect.right == SCREEN_WIDTH + 10:
            self.rect.x = 40

    def move_up(self):
        if self.rect.y > SCREEN_HEIGHT // 2:
            self.rect.y = self.rect.y - self.ship_speed

    def move_down(self):
        if self.rect.y < SCREEN_HEIGHT - 70:
            self.rect.y = self.rect.y + self.ship_speed


    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))    

    def reset(self):
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS

    def set_image(self, size = (40,60), image = SPACESHIP):
        self.image = image
        self.image = pygame.transform.scale(self.image, size)
        
    
    
