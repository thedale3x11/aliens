class Settings:
    def __init__(self):
        self.bg_color=(0,0,0)
        self.screen_width=1200
        self.screen_height=700
        self.mode=(self.screen_width,self.screen_height)
        
        self.bullet_width=3
        self.bullet_height=15
        self.bullet_color=255, 255, 0
        self.bullets_allowed=6

        self.fleet_drop_speed=10
        self.speedup_scale=1.1
        self.score_scale=1.5
        self.initialize_dynamic_settngs()
        self.fleet_direction=1

        self.ship_limit=3
        self.ship_image_name="images/alien_ship.png"
        self.ship_score_image_name="images/alien_ship_score.png"
    

    def initialize_dynamic_settngs(self):
        self.ship_speed_factor=1.5
        self.bullet_speed_factor=3
        self.alien_speed_factor=1
        self.alien_points=50


    def incraese_speed(self):
        self.ship_speed_factor*=self.speedup_scale
        self.bullet_speed_factor*=self.speedup_scale
        self.alien_speed_factor*=1
        self.alien_points=int(self.alien_points*self.score_scale)
        print(self.alien_points)