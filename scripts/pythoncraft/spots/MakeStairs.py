from pythoncraft.stage import Spot

class MagicSpot(Spot):
    def __init__(self):
        super().__init__(False, True, True)
        self.setRegion(-5, 0, 1, 0, 5, 10)