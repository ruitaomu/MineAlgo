from pythoncraft import world
from pythoncraft import status

def getStageSpot():
    status.ensureWorldCreated()
    pos = world.pcMinecraft.player.getTilePos()
    x = pos.x
    y = pos.y
    z = pos.z
    spot = world.getStageSpot(x, y, z)
    return spot

def printBlock(x, y, z):
    status.ensureWorldCreated()
    print(world.pcMinecraft.getBlock(x,y,z))

def printStandingBlock():
    status.ensureWorldCreated()
    pos = world.pcMinecraft.player.getTilePos()
    printBlock(pos.x, pos.y - 1, pos.z)

def putBlock(blockId):
    status.ensureWorldCreated()
    pos = world.pcMinecraft.player.getTilePos()
    world.pcMinecraft.setBlock(pos.x, pos.y - 1, pos.z, blockId)