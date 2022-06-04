from pythoncraft.stage import Spot

class SpotMegaJump(Spot):
    def __init__(self):
        super().__init__(True, False, False)
        self.setRegion(-20, 0, -20, 0, 20, 20)

    def jump(self, deltaX, deltaY, deltaZ):
        super().jump(deltaX, deltaY, deltaZ)
        if deltaY >= 18 and deltaX == 0 and deltaZ == 0:
            self.done()