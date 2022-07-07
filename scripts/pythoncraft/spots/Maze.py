from pythoncraft.stage import Spot
import pythoncraft.world as World

correctResultList = [24, 120, 24, 41, 41, 41, 41, 41, 24, 41, 41, 41, 24, 24, 24, 41, 24, 24, 24, 24, 0, 0, 24, 41, 24, 0, 0,  0, 22, 29, 24, 41, 0, 0, 24, 24, 24, 24, 24, 41, 24, 24, 24, 41, 41, 41, 24, 41, 24, 41, 41, 41, 24, 41, 24, 41, 24, 41, 24, 24, 24, 41, 24, 41, 24, 41, 41, 41, 24, 41, 41, 41, 24, 24, 24, 24, 24, 24, 24, 24]
resetBlocksList   = [24, 120, 24, 41, 41, 41, 41, 41, 24, 41, 41, 41, 24, 24, 24, 41, 24, 24, 24, 24, 0, 0, 24, 41, 24, 0, 0, -1, -1, -1, 24, 41, 0, 0, 24, 24, 24, 24, 24, 41, 24, 24, 24, 41, 41, 41, 24, 41, 24, 41, 41, 41, 24, 41, 24, 41, 24, 41, 24, 24, 24, 41, 24, 41, 24, 41, 41, 41, 24, 41, 41, 41, 24, 24, 24, 24, 24, 24, 24, 24]


class MagicSpot(Spot):
    def __init__(self):
        super().__init__(False, True, True)
        self.setRegion(0, 0, -1, 8, 0, 6)

    def setBlock(self, x, y, z, blockId, face):
        block = super().getBlock(x, y, z)
        if  block == 0 :
            super().setBlock(x, y, z, blockId, face)

    def reset(self, blockId = 24):
        super().reset(blockId)
        x = self.x
        y = self.y
        z = self.z - 1
        for block in resetBlocksList:
            if block == 41:
                World.pcMinecraft.setBlock(x, y, z, 0)
            elif block == -1:
                pass #piston set, don't touch
            else:
                World.pcMinecraft.setBlock(x, y, z, block)

            z = z + 1
            if z > (self.z+6):
                z = self.z - 1
                x = x + 1
                
    def done(self):
        blocks = World.pcMinecraft.getBlocks(self.x, self.y, self.z-1, self.x+9, self.y, self.z+6)
        if list(blocks) == correctResultList:
            super().say("Done!")
            super().done()
        else:
            super().say("No")
            self.reset(24)

    def say(self, content):        
        if content == "Done":
            self.done()
        else:
            super().say(content)