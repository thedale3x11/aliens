import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

class AlienInvasion:
    def __init__(self):
        self.settings=Settings()


    def run_game(self):
        pygame.init()
        
        screen = pygame.display.set_mode(self.settings.mode)
        pygame.display.set_caption("Alien Invasion")
        ship=Ship(self.settings,screen)
        bullets=Group()
        aliens=Group()
        stats=GameStats(self.settings)
        sb=Scoreboard(self.settings,screen,stats)
        

        gf.create_fleet(self.settings,screen,ship,aliens)
        play_button=Button(self.settings,screen,"Play")

        while True:
            gf.check_events(self.settings,stats,screen,sb,play_button,ship,aliens,bullets)
            if stats.game_active:
                ship.update()
                gf.update_bullets(self.settings,screen,stats,sb,ship,aliens,bullets)
                gf.update_aliens(self.settings,stats,sb,screen,ship,aliens,bullets)
            gf.update_screen(self.settings,screen,stats,sb,ship,aliens,bullets,play_button)
            
if __name__ == '__main__':
    ai = AlienInvasion()    
    ai.run_game()