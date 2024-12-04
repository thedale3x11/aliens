import pygame 
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self,settings,screen,ship,centerx_factor=0,direction=1,speed_factor=0):
        super(Bullet,self).__init__()
        self.screen=screen
        self.direction=direction
        self.rect=pygame.Rect(0,0,settings.bullet_width,settings.bullet_height) 
        self.rect.centerx=ship.rect.centerx+centerx_factor  
        self.rect.top=ship.rect.top
        
        self.y=float(self.rect.y)
        print(self.y)
        self.color=settings.bullet_color
        if speed_factor==0:
            self.speed_factor=settings.bullet_speed_factor
        else:
          self.speed_factor=1

    def update(self):
        if self.direction==1:
            self.y-=self.speed_factor
        else:
            self.y+=self.speed_factor
        
        self.rect.y=self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.color,self.rect)