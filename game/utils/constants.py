import pygame
import os
from pygame import mixer
import random

pygame.init()
pygame.mixer.init()

# Global Constants
TITLE = "WAR IN THE SKIES"
SCREEN_HEIGHT = 800
SCREEN_WIDTH = 1100
FPS = 50
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/player_plane.png"))

SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield_1.png'))
FUEL = pygame.image.load(os.path.join(IMG_DIR, 'Other/fuel.png'))

BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/Fondo_ciudad.jpg'))
BG_2 = pygame.image.load(os.path.join(IMG_DIR, 'Other/pista_17.jpg'))

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))

DEFAULT_TYPE = "default"
SHIELD_TYPE = 'shield'
SPEED_TYPE = 'SPEED'

SPACESHIP = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/player_plane.png"))
SPACESHIP_LEFT = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/player_plane_left.png"))
SPACESHIP_RIGHT = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/player_plane_right.png"))

SPACESHIP_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/player_plane_shield.png"))
SPACESHIP_SHIELD_RIGHT = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/player_plane_right_shield.png"))
SPACESHIP_SHIELD_LEFT = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/player_plane_left_shield.png"))

SPACESHIP_SPEED = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/player_plane_speed.png"))
SPACESHIP_SPEED_LEFT = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/player_plane_left_speed.png"))
SPACESHIP_SPEED_RIGHT = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/player_plane_right_speed.png"))


BULLET_ENEMY = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_enemy_1.png"))
BULLET_PLAYER = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_player_1.png"))

PLAYER_DESTROY = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/player_plane_destroy.png"))

ENEMY_2 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_2.png"))
ENEMY_3 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_3.png"))
ENEMY_4 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_4.png"))
ENEMY_5 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_5.png"))
#ENEMY_1 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_1.png"))

EXPLOSION = pygame.image.load(os.path.join(IMG_DIR, "Enemy/explosion.png"))

FONT_STYLE = 'freesansbold.ttf'
FONT_STYLE2 = 'ARCADE_R.ttf'

#sounds
BULLET_SOUND = pygame.mixer.Sound("game/assets/Other/bullet.mp3")
LASER = pygame.mixer.Sound("game/assets/Other/laser.mp3")
START_SOUND = pygame.mixer.Sound("game/assets/Other/start.mp3")
MUSIC = pygame.mixer.Sound("game/assets/Other/music.mp3")
DEFEAT_SOUND = pygame.mixer.Sound("game/assets/Other/defeat.mp3")
SPEED_EFFECT = pygame.mixer.Sound("game/assets/Other/speed_effect.mp3")
SHIELD_EFFECT = pygame.mixer.Sound("game/assets/Other/shield.mp3")
KILL = pygame.mixer.Sound("game/assets/Other/kill.mp3")
SCORE_SOUND = pygame.mixer.Sound("game/assets/Other/score.mp3")

BG_DEFEAT = pygame.image.load(os.path.join(IMG_DIR, "Other/soldiers2.png"))
SKULL = pygame.image.load(os.path.join(IMG_DIR, "Other/skull.png"))
KEYS = pygame.image.load(os.path.join(IMG_DIR, "Other/keys.png"))
SPACEBAR = pygame.image.load(os.path.join(IMG_DIR, "Other/spacebar.png"))

X_POWER_UP = random.randint(120, SCREEN_WIDTH -120)    
Y_POWER_UP = 0