import pygame
import os

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
SPACESHIP_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/player_plane_shield.png"))
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

BG_DEFEAT = pygame.image.load(os.path.join(IMG_DIR, "Other/soldiers2.png"))
SKULL = pygame.image.load(os.path.join(IMG_DIR, "Other/skull.png"))
KEYS = pygame.image.load(os.path.join(IMG_DIR, "Other/keys.png"))
SPACEBAR = pygame.image.load(os.path.join(IMG_DIR, "Other/spacebar.png"))