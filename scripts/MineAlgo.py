from mcpi.minecraft import Minecraft
import hanoi
import sort
import Temp2ndFloorMaze

import time
import random



mc = Minecraft.create()

hanoi.init(mc)
sort.init(mc)
Temp2ndFloorMaze.init(mc)

mc.postToChat("Your AlgoWorld has been initialized")

while True:
    flagFinished = False
    while flagFinished == False:
        # pos = mc.player.getTilePos()
        # if Temp2ndFloorMaze.isInsideTemple2ndFloorMaze(pos) == True:
        #    if mc.getBlock(pos.x, pos.y-1, pos.z) == 206: # End Stone Brick(id:end_bricks)
        #        mc.setBlock(pos.x, pos.y-1, pos.z, 89)   # Glowstone
        blockEvents = mc.events.pollBlockHits()
        for blockEvent in blockEvents:
            print(blockEvent)
            if sort.onSortMachineEvent(mc, blockEvent) == True:
                pass
            elif hanoi.onHanoiMachineEvent(mc, blockEvent) == True:
                pass
            elif Temp2ndFloorMaze.onTemp2ndFloorMazeEvent(mc, blockEvent) == True:
                pass
