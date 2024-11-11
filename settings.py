class Settings:
    def __init__(self):
        self.ship_speed_factor=1.5
        self.bg_color=(0,0,0)
        self.screen_width=800
        self.screen_height=600
        self.mode=(self.screen_width,self.screen_height)
        
        self.bullet_speed_factor=1
        self.bullet_width=3
        self.bullet_height=15
        self.bullet_color=255, 255, 0
        self.bullets_allowed=6

        self.alien_speed_factor=1
        self.fleet_drop_speed=10
        self.fleet_direction=1