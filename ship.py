import pygame 

class Ship():
    def __init__(self,settings,screen):
        self.screen = screen
        self.image = pygame.image.load("images/alien_ship.png")
        self.settings = settings

        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
        
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.default_posx = self.screen_rect.centerx
        self.default_posy = self.screen_rect.bottom

        self.center = float(self.rect.centerx)
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
    
    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += self.settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.rect.centerx -= self.settings.ship_speed_factor
        if self.moving_up and self.rect.top > 0:
            self.rect.bottom -= self.settings.ship_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.bottom += self.settings.ship_speed_factor
        
    def to_default_position(self):
        self.rect.centerx = self.default_posx
        self.rect.bottom = self.default_posy

    def blitme(self):
        self.screen.blit(self.image,self.rect)

    def center_ship(self):
        self.center=self.screen_rect.centerx