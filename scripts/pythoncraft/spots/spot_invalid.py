from pythoncraft.stage import Spot

class SpotInvalid(Spot):
    def __init__(self):
        super().__init__(False, False, False)

    def setPos(self, x, y, z):
        pass

    def setRegion(self, minDeltaX, minDeltaY, minDeltaZ, maxDeltaX, maxDeltaY, maxDeltaZ):
        pass

    def done(self):
        pass

    def reset(self, blockId):
        pass

    def jump(self, deltaX, deltaY, deltaZ):
        return False

    def say(self, content):
        return False

    def setBlock(self, x, y, z, blockId, face):
        return False

    def isInRegion(self, deltaX, deltaY, deltaZ):
        return False