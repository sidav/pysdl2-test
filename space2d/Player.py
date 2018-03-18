

class Player:
    player_ship = None

    def __init__(self, ship):
        self.player_ship = ship

    def get_ship(self):
        return self.player_ship

    def get_coords(self):
        return self.player_ship.get_coords()
