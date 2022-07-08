from pythoncraft.stage import Spot
import pythoncraft.world

class MagicSpot(Spot):
    def __init__(self):
        super().__init__(False, True, True)
        self.setRegion(0, 0, 1, 3, 4, 3)
        super().setAllowedBlocks([24])

    def reset(self, blockId=0):
        pythoncraft.world.pcMinecraft.setBlocks(self.x, self.y, self.z+1, self.x+3, self.y+4, self.z+3, blockId)