import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf

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
        #alien=Alien(self.settings,screen)
        gf.create_fleet(self.settings,screen,aliens)
        while True:
            gf.check_events(self.settings,screen,ship,bullets)
            ship.update()
            gf.update_bullets(bullets)
            print(len(bullets))
            
            gf.update_screen(self.settings,screen,ship,aliens,bullets)
            
if __name__ == '__main__':    
    ai = AlienInvasion()    
    ai.run_game()
