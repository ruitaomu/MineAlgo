from pythoncraft.stage import Spot
import pythoncraft.world as World

correctResultList = [24, 24, 24, 24, 24, 24, 24, 24, 0, 0, 0, 0, 0, 24, 24, 0, 0, 0, 0, 0, 24, 24, 0, 0, 0, 0, 0, 24, 24, 0, 0, 0, 0, 0, 24, 24, 0, 0, 0, 0, 0, 24, 24, 24, 24, 24, 24, 24, 24, 0, 0, 0, 0, 0, 0, 0, 0, 24, 24, 24, 24, 24, 0, 0, 24, 0, 0, 0, 24, 0, 0, 24, 0, 0, 0, 24, 0, 0, 24, 0, 0, 0, 24, 0, 0, 24, 24, 24, 24, 24, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 24, 24, 24, 0, 0, 0, 0, 24, 0, 24, 0, 0, 0, 0, 24, 24, 24, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 24, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

class MagicSpot(Spot):
    def __init__(self):
        super().__init__(False, True, True)
        self.setRegion(-3, 0, 1, 3, 3, 7)

    def reset(self, blockId = 0):
        World.pcMinecraft.setBlocks(self.x-3, self.y, self.z+1, self.x+3, self.y+3, self.z+7, blockId)
        World.pcMinecraft.setBlock(self.x , self.y+6, self.z+4, 24)

    def done(self):
        blocks = World.pcMinecraft.getBlocks(self.x-3, self.y, self.z+1, self.x+3, self.y+3, self.z+7)
        if list(blocks) == correctResultList:
            World.pcMinecraft.setBlock(self.x , self.y+6, self.z+4, 0)
            super().say("Done!")
        else:
            super().say("No")
            self.reset()

    def say(self, content):        
        if content == "Done":
            self.done()
        else:
            super().say(content)