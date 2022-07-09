from mcpi.minecraft import Minecraft
import pythoncraft.sort as sort

def start():

    mc = Minecraft.create()


    sort.closeDoor(mc)
    mc.postToChat("Start quiz")

    sort.init(mc)
    mc.setBlocks(2942, 62, -37, 2946, 62, -37, 24)
    mc.setBlocks(2942, 63, -37, 2946, 63, -37, 0)

    flagFinished = False
    while flagFinished == False:
        # pos = mc.player.getTilePos()
        # if Temp2ndFloorMaze.isInsideTemple2ndFloorMaze(pos) == True:
        #    if mc.getBlock(pos.x, pos.y-1, pos.z) == 206: # End Stone Brick(id:end_bricks)
        #        mc.setBlock(pos.x, pos.y-1, pos.z, 89)   # Glowstone
        blockEvents = mc.player.pollBlockHits()
        for blockEvent in blockEvents:
            print(blockEvent)
            block = mc.getBlock(blockEvent.pos.x, blockEvent.pos.y, blockEvent.pos.z)
            print("Block id: "+str(block))
            if block == 143:
                sort.swapBlocks(blockEvent.pos.x, blockEvent.pos.y, blockEvent.pos.z)
                steps = sort.checkSucceed()
                if steps >= 0 and steps <= sort.targetSteps:                
                    mc.postToChat("Well done!")
                    flagFinished = True
                    sort.openDoor(mc)
                    for xrail in range(2942, 2947):
                        mc.setBlock(xrail, 63, -37, 66)
                elif sort.userSteps >= sort.targetSteps:
                    mc.postToChat("You've used more steps than expected. Try again!")
                    targetSteps = sort.resetBlocks()
                    
                    


                    