import pygame
from game.utils.constants import SHIELD_TYPE, SPACESHIP

class BulletManager:
    def __init__(self):
        self.bullets =  []
        self.enemy_bullets = []

    def update(self, game):

        for bullet in self.enemy_bullets:
            bullet.update(self.enemy_bullets)

            if bullet.rect.colliderect(game.player.rect) and bullet.owner == "enemy":
                self.enemy_bullets.remove(bullet)
                if game.player.power_up_shield_active != True:
                    game.playing = False
                    game.death_count += 1
                    pygame.time.delay(500)
                if game.player.power_time_up == 0:
                            game.player.set_image((90,90), SPACESHIP)
                break

            for bullet in self.bullets:
                bullet.update(self.bullets)

            for enemy in game.enemy_manager.enemies:
                if bullet.rect.colliderect(enemy.rect)and bullet.owner != "enemy":
                    game.enemy_manager.enemies.remove(enemy)
                    self.bullets.remove(bullet)
                    game.update_score()
                    break

    def draw(self, screen):

        for bullet in self.enemy_bullets:
            bullet.draw(screen)
        
        for bullet in self.bullets:
            bullet.draw(screen)


    def add_bullet(self, bullet):
        if bullet.owner == "enemy" and len(self.enemy_bullets) < 1:
            self.enemy_bullets.append(bullet)
        elif bullet.owner == "player" and len(self.bullets) < 1:
            self.bullets.append(bullet)

    def reset(self):
        self.bullets = []
        self.enemy_bullets = []