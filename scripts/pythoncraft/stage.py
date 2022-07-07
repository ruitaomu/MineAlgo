import pythoncraft.world

class Spot:
    def __init__(self, isJumpEnabled, isSayEnabled, isSetBlockEnabled):
        self.isJumpEnabled = isJumpEnabled
        self.isSayEnabled = isSayEnabled
        self.isSetBlockEnabled = isSetBlockEnabled
        self.setRegion(0, 0, 0, -1, -1, -1)

    def setPos(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def setRegion(self, minDeltaX, minDeltaY, minDeltaZ, maxDeltaX, maxDeltaY, maxDeltaZ):
        self.minDeltaX = minDeltaX
        self.minDeltaY = minDeltaY
        self.minDeltaZ = minDeltaZ
        self.maxDeltaX = maxDeltaX
        self.maxDeltaY = maxDeltaY
        self.maxDeltaZ = maxDeltaZ

    def done(self):
        pythoncraft.world.pcMinecraft.setBlock(self.x, self.y-2, self.z, 152)

    def reset(self, blockId = 1):
        pythoncraft.world.pcMinecraft.setBlock(self.x, self.y-2, self.z, blockId)

    def jump(self, deltaX, deltaY, deltaZ):
        if (self.isJumpEnabled and self.isInRegion(deltaX, deltaY, deltaZ)):
            pythoncraft.world.pcMinecraft.player.setTilePos(self.x + deltaX, self.y + deltaY, self.z + deltaZ)
            return True
        else:
            return False

    def say(self, content):
        if (self.isSayEnabled):
            pythoncraft.world.pcMinecraft.postToChat(content)
            return True
        else:
            return False

    def setBlock(self, x, y, z, blockId, face):
        if (self.isSetBlockEnabled and self.isInRegion(x, y, z)):
            pythoncraft.world.pcMinecraft.setBlock(self.x + x, self.y + y, self.z + z, blockId, face)
            return True
        else:
            return False

    def getBlock(self, x, y, z):
        return pythoncraft.world.pcMinecraft.getBlock(self.x + x, self.y + y, self.z + z)

    def isInRegion(self, deltaX, deltaY, deltaZ):
        if (deltaX >= self.minDeltaX and deltaX <= self.maxDeltaX
            and deltaY >= self.minDeltaY and deltaY <= self.maxDeltaY
            and deltaZ >= self.minDeltaZ and deltaZ <= self.maxDeltaZ):
            return True

        else:
            return False
