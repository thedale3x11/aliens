class GameStats():
    def __init__(self,settings):
        self.high_score=0
        self.level=1
        self.game_active=False
        self.settings=settings
        self.reset_stats()


    def reset_stats(self):
        self.level=1
        self.ship_left=self.settings.ship_limit
        self.score=0