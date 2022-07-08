from pythoncraft.stage import Spot
import pythoncraft.world as World

correctResultList = [0, 41, 41, 41, 41, 41, 0, 0, 41, 0, 0, 41, 0, 0, 0, 41, 0, 0, 41, 0, 0, 41, 41, 41, 41]

class MagicSpot(Spot):
    def __init__(self):
        super().__init__(False, True, True)
        self.setRegion(-2, 1, -2, 2, 1, 2)
        super().setAllowedBlocks([41])

    def reset(self, blockId=0):
        super().reset(1)
        World.pcMinecraft.setBlocks(self.x-2, self.y+1, self.z-2, self.x+2, self.y+1, self.z+2, blockId)

    def done(self):
        blocks = World.pcMinecraft.getBlocks(self.x-2, self.y+1, self.z-2, self.x+2, self.y+1, self.z+2)
        if list(blocks) == correctResultList:
            super().say("Done!")
            super().done()
        else:
            super().say("No")
            self.reset()        

    def say(self, content):
        print(list(World.pcMinecraft.getBlocks(self.x-2, self.y+1, self.z-2, self.x+2, self.y+1, self.z+2)))
        if content == "Done":
            self.done()
        else:
            super().say(content)