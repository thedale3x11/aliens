import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf
from game_stats import GameStats

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
        gf.create_fleet(self.settings,screen,ship,aliens)
        print()
        while True:
            gf.check_events(self.settings,screen,ship,bullets)
            if stats.game_active:
                ship.update()
                gf.update_bullets(self.settings,screen,ship,aliens,bullets)
                gf.update_aliens(self.settings,stats,screen,ship,aliens,bullets)
                gf.update_screen(self.settings,screen,ship,aliens,bullets)
            
if __name__ == '__main__':
    ai = AlienInvasion()    
    ai.run_game()