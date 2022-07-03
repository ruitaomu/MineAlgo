from mcpi.minecraft import Minecraft

import time
import random
import sys


def bubbleSort(arr):
    n = len(arr)
    steps = 0
 
    # 遍历所有数组元素
    for i in range(n):
 
        # Last i elements are already in place
        for j in range(0, n-i-1):
 
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
                steps += 1
    return steps

initBlocks = [22, 41, 48, 57, 133, 169, 173, 201]
shuffledBlocks = []
sortedBlocks = []
blockPoints = [(2961, 63, -36),(2961, 63, -38),(2961, 63, -40),(2963, 63, -40),(2965, 63, -40),(2966, 63, -39),(2966, 63, -37),(2966, 63, -35)]
buttonPoints = [(2961, 63, -37),(2961, 63, -39),(2962, 63, -40),(2964, 63, -40),(2966, 63, -40),(2966, 63, -38),(2966, 63, -36)]

def doorAction(blockEvent, isClosing):
    i = 0
    blocks = list(mc.getBlocks(blockEvent.pos.x, blockEvent.pos.y, blockEvent.pos.z-5, blockEvent.pos.x+7, blockEvent.pos.y, blockEvent.pos.z+5))
    print(blocks)
    found = False
    for x in range(blockEvent.pos.x, blockEvent.pos.x+8):
        for z in range(blockEvent.pos.z-5, blockEvent.pos.z+6):
            if blocks[i] == 214 and isClosing == False:
                print("214 found at:"+str(x)+",y,"+str(z))
                mc.setBlock(x, blockEvent.pos.y, z, 152)
                found = True
            elif blocks[i] == 152 and isClosing == True:
                print("152 found at:"+str(x)+",y,"+str(z))
                mc.setBlock(x, blockEvent.pos.y, z, 214)
                found = True

            i = i+1
        #214 Nether Wart Block
        #152 Redstone
    
    if found == True:
        return

    blocks = list(mc.getBlocks(blockEvent.pos.x+8, blockEvent.pos.y, blockEvent.pos.z-5, blockEvent.pos.x+8, blockEvent.pos.y, blockEvent.pos.z+5))
    print(blocks)
    i = 0
    x = blockEvent.pos.x+8
    for z in range(blockEvent.pos.z-5, blockEvent.pos.z+6):
        if blocks[i] == 214 and isClosing == False:
            print("214 found at:"+str(x)+",y,"+str(z))
            mc.setBlock(x, blockEvent.pos.y, z, 152)
        elif blocks[i] == 152 and isClosing == True:
            print("152 found at:"+str(x)+",y,"+str(z))
            mc.setBlock(x, blockEvent.pos.y, z, 214)

        i = i+1
        #214 Nether Wart Block
        #152 Redstone

def closeDoor(blockEvent):
    doorAction(blockEvent, True)

def openDoor(blockEvent):
    doorAction(blockEvent, False)

def swapBlocks(x, y, z):
    global userSteps

    btList = [item for item in buttonPoints if item == (x, y, z)]
    if len(btList) > 0:
        i = buttonPoints.index((x, y, z))
        b1p = blockPoints[i]
        b2p = blockPoints[i+1]
        sortedBlocks[i], sortedBlocks[i+1] = sortedBlocks[i+1], sortedBlocks[i]
    else:
        return

    b1 = mc.getBlock(b1p[0], b1p[1], b1p[2])
    b2 = mc.getBlock(b2p[0], b2p[1], b2p[2])
    mc.setBlock(b1p[0], b1p[1], b1p[2], b2)
    mc.setBlock(b2p[0], b2p[1], b2p[2], b1)
    userSteps = userSteps + 1

def shuffleBlocks(blocks):
    temp = []
    i = 0
    while i < len(blocks):
        i += 1
        while True:
            block = random.choice(blocks)
            if block in temp:
                continue
            else:
                temp.append(block);
                break;
    return temp            
    
def resetBlocks():    
    global sortedBlocks, userSteps

    sortedBlocks = shuffledBlocks[:]
    stepsGoal = bubbleSort(sortedBlocks)
    userSteps = 0
    #sortedBlocks = shuffledBlocks[:]
    #stepsGoal2 = insertionSort(sortedBlocks)
    i = 0
    for pos in blockPoints:
        mc.setBlock(pos[0], pos[1], pos[2], shuffledBlocks[i])
        print("put block "+str(i)+":"+str(shuffledBlocks[i]))
        i = i + 1

    sortedBlocks = shuffledBlocks
    return stepsGoal

def checkSucceed():
    global userSteps
    if sortedBlocks == initBlocks:
        return userSteps
    else:
        return -1

mc = Minecraft.create()

mc.postToChat("Start quiz")

shuffledBlocks = shuffleBlocks(initBlocks)
targetSteps = resetBlocks()

mc.postToChat("Your target steps: "+str(targetSteps))

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
            swapBlocks(blockEvent.pos.x, blockEvent.pos.y, blockEvent.pos.z)
            steps = checkSucceed()
            if steps < 0 :
                pass
            elif steps <= targetSteps:
                mc.postToChat("Well done!")
                flagFinished = True
                openDoor(blockEvent)
            else:
                mc.postToChat("Your target steps: "+str(targetSteps))
                mc.postToChat("You've used more steps than expected. Try again!")
                targetSteps = resetBlocks()
                flagFinished = True
                closeDoor(blockEvent)
                


                