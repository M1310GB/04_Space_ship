import pygame
from game.utils.constants import FONT_STYLE, SCREEN_HEIGHT, SCREEN_WIDTH, BG, BG_2, FONT_STYLE2

class Menu:
    HALF_SCREEEN_HEIGHT = SCREEN_HEIGHT // 2
    HALF_SCREEEN_WIDTH = SCREEN_WIDTH // 2

    def __init__(self, message, screen):
        screen.fill((255,255,255))
        self.background_image = pygame.transform.scale(BG_2, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.background_rect = self.background_image.get_rect()
        
        self.font = pygame.font.Font(FONT_STYLE, 30)
        self.text = self.font.render(message, True, (0,0,0))
        self.text_info = self.font.render(message,True,(0,0,0))
        self.text_rect = self.text.get_rect()
        self.text_rect.center =(self.HALF_SCREEEN_WIDTH, self.HALF_SCREEEN_HEIGHT)


    def handle_events_on_menu(self,game):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.running = False
                game.playing = False
            if event.type == pygame.KEYDOWN:
                game.run()

    def update(self,game):
        pygame.display.update()
        self.handle_events_on_menu(game)
 
    def draw(self, screen):

        screen.blit(self.background_image, self.background_rect)
        screen.blit(self.text, self.text_rect)


    def update_message(self, message, font_size,color):
        self.font = pygame.font.Font(FONT_STYLE2, font_size)
        self.text = self.font.render(message,True,color)
        self.text_rect = self.text.get_rect()
        self.text_rect.center =(self.HALF_SCREEEN_WIDTH, self.HALF_SCREEEN_HEIGHT - 250)



    def reset_screen_color(self,screen):
        screen.fill((0,0,255))