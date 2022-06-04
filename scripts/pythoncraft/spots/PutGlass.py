from pythoncraft.stage import Spot

class MagicSpot(Spot):
    def __init__(self):
        super().__init__(False, True, True)
        self.setRegion(-2, 1, -2, 2, 1, 2)

    def say(self, content):
        super().say(content)
        self.done()