import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
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
        while True:
            gf.check_events(self.settings,screen,ship,bullets)
            ship.update()
            bullets.update()
            for bullet in bullets.copy():
                if bullet.rect.bottom <= 0:
                    bullets.remove(bullet)
            print(len(bullets))
            
            gf.update_screen(self.settings,screen,ship,bullets)
            
if __name__ == '__main__':    
    ai = AlienInvasion()    
    ai.run_game()