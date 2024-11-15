class Settings:
    def __init__(self):
        #self.ship_speed_factor=1.5
        self.bg_color=(0,0,0)
        self.screen_width=800
        self.screen_height=600
        self.mode=(self.screen_width,self.screen_height)
        
        #self.bullet_speed_factor=2
        self.bullet_width=3
        self.bullet_height=15
        self.bullet_color=255, 255, 0
        self.bullets_allowed=6

        #self.alien_speed_factor=1
        self.fleet_drop_speed=10
        self.speedup_scale=1.1
        self.initialize_dynamic_settngs()
        self.fleet_direction=1

        self.ship_limit=6
    
    def initialize_dynamic_settngs(self):
        self.ship_speed_factor=1.5
        self.bullet_speed_factor=3
        self.alien_speed_factor=1

    def incraese_speed(self):
        self.ship_speed_factor*=self.speedup_scale
        self.bullet_speed_factor*=self.speedup_scale
        self.alien_speed_factor*=self.speedup_scale