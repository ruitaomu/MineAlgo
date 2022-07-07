from pythoncraft.stage import Spot
import pythoncraft.world

class SpotLavaBridge(Spot):
    def __init__(self):
        super().__init__(False, True, True)
        self.setRegion(-4, 0, 1, 4, 0, 10)

    def reset(self, blockId=0):
        pythoncraft.world.pcMinecraft.setBlocks(self.x + self.minDeltaX, self.y + self.minDeltaY, self.z + self.minDeltaZ, 
                                                self.x + self.maxDeltaX, self.y + self.maxDeltaY, self.z + self.maxDeltaZ, blockId)
