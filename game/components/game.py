import pygame

from game.utils.constants import BG, ICON,PLAYER_DESTROY , SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEFAULT_TYPE, FONT_STYLE, FONT_STYLE2

from game.components.spaceship import Spaceship
from game.components.enemies.enemy_manager import EnemyManager
from game.components.bullets.bullet_manager import BulletManager
from game.components.menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode( (SCREEN_WIDTH, SCREEN_HEIGHT) )
        self.clock = pygame.time.Clock()

        self.playing = False
        self.game_speed = 10 

        self.x_pos_bg = 0
        self.y_pos_bg = 0
        self.player = Spaceship()
        self.enemy_manager = EnemyManager()
        self.bullet_manager = BulletManager()
        self.running = False
        self.score = 0
        self.death_count = 0
        self.menu = Menu("Press any key to start...", self.screen)
        
        

    def execute(self):
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()
        pygame.display.quit()
        pygame.quit()
        
    def run(self):
        self.enemy_manager.reset()
        self.score = 0
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
            
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False


    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input,self)

        self.enemy_manager.update(self)
        self.bullet_manager.update(self)

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))

        self.draw_background()
        self.player.draw(self.screen)
        self.enemy_manager.draw(self.screen)
        self.bullet_manager.draw(self.screen)
        self.draw_score()

        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))
        image_height = image.get_height()
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))


        if self.y_pos_bg >= SCREEN_HEIGHT:
            self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
            self.y_pos_bg = 0
        self.y_pos_bg = self.y_pos_bg + self.game_speed


    def show_death_info(self):
        self.menu_death_info.update_message("Score: {}".format(self.score), 50, (255, 255, 255))
        self.menu_death_info.draw(self.screen)
        pygame.display.update()

    def add_message(self):
        self.font = pygame.font.Font(FONT_STYLE2, 10)
        self.text = self.font.render("Score: {}".format(self.score),True,(255, 255, 255))
        self.text_rect = self.text.get_rect()
        self.text_rect.center =(SCREEN_WIDTH // 2, (SCREEN_HEIGHT // 2 ) - 50)

    def show_menu(self):



        #self.menu.reset_screen_color(self.screen)
        half_screen_hight = SCREEN_HEIGHT // 2
        half_screen_width = SCREEN_WIDTH // 2
        
        info_muerte = "GAME" + "    " + "OVER" 
        info_inicio = "Press any key to start"

        if self.death_count == 0:
            self.menu.update_message(info_inicio, 30, (255,255,255))
            self.menu.draw(self.screen)
            icon = pygame.transform.scale(ICON, (200,200))
        else:
            self.menu.update_message(info_muerte, 90, (255,255,255))
            self.add_message()
            self.menu.draw(self.screen)
            icon = pygame.transform.scale(PLAYER_DESTROY, (200,200))
            
        
        self.screen.blit(icon, (half_screen_width - 100, half_screen_hight - 150 ))
        self.menu.update(self)


    def update_score(self):
        self.score +=1

    def draw_score(self):
        font = pygame.font.Font(FONT_STYLE2,30)
        text =font.render(f'Score: {self.score}',True,(255,255,255))
        text_rect = text.get_rect()
        text_rect.center = (100,50)
        self.screen.blit(text,text_rect)

    

