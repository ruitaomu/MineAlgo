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

# <Maze>
def maze():
    x = 1
    y = 0
    z = 0
    while player.getBlock(x, y-1, z) != 57: #Check if it's diamond. Stop when reach diamond block
        player.setBlock(x, y, z, 41) # Gold
        if player.getBlock(x+1, y, z) == 0:
            x = x + 1
        elif player.getBlock(x-1, y, z) == 0:
            x = x -1
        elif player.getBlock(x, y, z+1) == 0:
            z = z + 1
        elif player.getBlock(x, y, z-1) == 0:
            z = z - 1
        else:
            player.say("I can't find the way!")
            return

    player.setBlock(x, y, z, 41) # Gold

    player.say("Done")

def stepMaze(x, z):
    if player.getBlock(x, 0, z) == 57: #Check if it's diamond. Stop when reach diamond block
        player.setBlock(x, 0, z, 66)
        return True

    block = player.getBlock(x, 0, z)
    if block != 0:
        return False
    
    player.setBlock(x, 0, z, 66) #66: Rail
    
    if stepMaze(x-1, z) == True:
        return True

    if stepMaze(x, z-1) == True:
        return True

    if stepMaze(x+1, z) == True:
        return True

    if stepMaze(x, z+1) == True:
        return True

    player.setBlock(x, 0, z, 0)

    return False

def railMaze():
    if (stepMaze(1, 0) == False):
        player.say("I can't find the way out")
    else:
        player.say("Let's go!")

#player.say("Open World")
#util.getStageSpot().reset()
#makeStair()
#lavaBridge()
#pyramid()
#util.getStageSpot().done()
#megaJump()
#putGlass()
#maze()
#railMaze()
