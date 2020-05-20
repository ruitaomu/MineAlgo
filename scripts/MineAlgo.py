from mcpi.minecraft import Minecraft
import hanoi
import sort

import time
import random

mc = Minecraft.create()

hanoi.init(mc)
sort.init(mc)

while True:
    flagFinished = False
    while flagFinished == False:
        blockEvents = mc.events.pollBlockHits()
        for blockEvent in blockEvents:
            print(blockEvent)
            if sort.onSortMachineEvent(mc, blockEvent) == True:
                pass
            elif hanoi.onHanoiMachineEvent(mc, blockEvent) == True:
                pass
