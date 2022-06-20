import pythoncraft.player as player
import pythoncraft.util as util

# <MegaJump>
def megaJump():
    player.jump(0, 18, 0)

# <MakeStair>
def makeStair():
    player.setBlock(0, 1, 1, 24)
    player.setBlock(0, 2, 2, 24)
    player.setBlock(0, 3, 3, 24)

# <LavaBridge>
def lavaBridge():
    for z in range(1, 11):
        player.setBlock(0, 0, z, 24)

# <PutGlass>
def putGlass():
    for x in range(-2, 3):
        for z in range(-2, 3):
            if player.getBlock(x, 0, z) == 95:
                player.setBlock(x, 1, z, 41)
    player.say("Done")

# <Pyramid>
def pyramid():
    for y in range(0, 4):
        x = y-3
        for z in range(1+y, 8-y):
            player.setBlock(x, y, z, 24)

        x = 3-y
        for z in range(1+y, 8-y):
            player.setBlock(x, y, z, 24)

        z = 1+y
        for x in range(-2+y, 3-y):
            player.setBlock(x, y, z, 24)

        z = 7-y
        for x in range(-2+y, 3-y):
            player.setBlock(x, y, z, 24)
        

    player.say("Done")

util.getStageSpot().reset(1)
megaJump()