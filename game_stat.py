class GameStats():
    def __init__(self, settings):
        self.restart_stats(settings)

    def update_stats(self, ship, settings):
        self.hp = ship.hp

    def restart_stats(self, settings):
        self.hp = settings.ship_hp
        self.score = 0