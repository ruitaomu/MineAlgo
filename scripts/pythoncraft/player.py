from pythoncraft import util

def say(content):
    spot = util.getStageSpot()
    spot.say(content)

def setBlock(x, y, z, type, face = 0):
    spot = util.getStageSpot()
    spot.setBlock(x, y, z, type, face)

def jump(deltaX, deltaY, deltaZ):
    spot = util.getStageSpot()
    spot.jump(deltaX, deltaY, deltaZ)
