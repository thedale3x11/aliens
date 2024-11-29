import pygame.font
from pygame.sprite import Group
from ship import Ship

class Scoreboard():
    def __init__(self,settings,screen,stats,ship):
        self.screen=screen
        self.screen_rect=screen.get_rect()
        self.settings=settings
        self.stats=stats

        self.text_color=(180,180,180)
        self.font=pygame.font.SysFont(None,30)

        self.prep_score()
        self.prep_ships()


    def prep_score(self):

        score_str=f"h.score: {self.stats.high_score} score: {self.stats.score} level: {self.stats.level}"
        self.score_image=self.font.render(score_str,True,self.text_color,self.settings.bg_color)
        
        self.score_rect=self.score_image.get_rect()
        self.score_rect.right=self.screen_rect.right-20
        self.score_rect.top=10


    def show_score(self):
        self.screen.blit(self.score_image,self.score_rect)
        self.ships.draw(self.screen)
    

    def reset_level(self):
        self.stats.level=1
        self.prep_score()

    
    def prep_ships(self):
        self.ships=Group()
        for ship_number in range(self.stats.ship_left):
            ship=Ship(self.settings,self.screen,self.settings.ship_score_image_name)
            ship.rect.x=10+ship_number*ship.rect.width
            ship.rect.y=10
            self.ships.add(ship)