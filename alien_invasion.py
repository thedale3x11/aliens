import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf

class AlienInvasion:
    def __init__(self):
        self.settings=Settings()

    def run_game(self):
        pygame.init()
        
        screen = pygame.display.set_mode(self.settings.mode)
        pygame.display.set_caption("Alien Invasion by Daryna")
        ship=Ship(self.settings,screen)
        while True:
            gf.check_events(self.settings,ship)
            ship.update()
            gf.update_screen(self.settings,screen,ship)

if __name__ == '__main__':    
    ai = AlienInvasion()    
    ai.run_game()