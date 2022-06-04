from pythoncraft.stage import Spot

class SpotLavaBridge(Spot):
    def __init__(self):
        super().__init__(False, True, True)
        self.setRegion(-4, -1, 0, 4, 0, 10)
