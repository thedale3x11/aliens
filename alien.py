import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self,settings,screen,name):
        super(Alien,self).__init__()
        self.name=name
        self.screen = screen
        self.settings=settings

        self.image=pygame.image.load('images/alien.bmp')
        self.rect=self.image.get_rect()

        self.rect.x=self.rect.width
        self.rect.y=self.rect.height

    def blitme(self):
        self.screen.blit(self.image,self.rect)

    def update(self):
        self.rect.x+=(self.settings.alien_speed_factor*self.settings.fleet_direction)

    def check_edges(self):
        screen_rect=self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True