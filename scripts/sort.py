from mcpi.minecraft import Minecraft
import time
import random
import constants

initBlocks = [133, 41, 152, 179, 57, 173, 155]
sortedBlocks = []
shuffledBlocks = []
posPopMachineX = constants.templeBasePosition_x + 7
posPopMachineY = constants.templeBuildingPosition_y + 3
posPopMachineZ = constants.templeBuildingPosition_z + 11
posPosMachineZList = [posPopMachineZ, posPopMachineZ+2, posPopMachineZ+4, posPopMachineZ+6, posPopMachineZ+8, posPopMachineZ+10]

steps = 0
goalSteps = 0

def getShuffledArray():
    return shuffledBlocks.copy()

def insertionSort(arr): 
    steps = 0
    for i in range(1, len(arr)): 

        key = arr[i] 

        j = i-1
        while j >=0 and key < arr[j] : 
                arr[j+1] = arr[j] 
                j -= 1
                steps += 1
        arr[j+1] = key
    return steps
      
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
    
def resetBlocks(mc):
    global sortedBlocks
    
    sortedBlocks = shuffledBlocks[:]
    stepsGoal = bubbleSort(sortedBlocks)
    sortedBlocks = shuffledBlocks[:]
    stepsGoal2 = insertionSort(sortedBlocks)
    i = 0
    for z in posPosMachineZList:
        mc.setBlock(posPopMachineX - 1, posPopMachineY + 2, z - 1, sortedBlocks[i])
        mc.setBlock(posPopMachineX - 1, posPopMachineY, z - 1, shuffledBlocks[i])
        print("put block "+str(i)+":"+str(shuffledBlocks[i]))
        i += 1
    mc.setBlock(posPopMachineX - 1, posPopMachineY + 2, z + 1, sortedBlocks[i])
    mc.setBlock(posPopMachineX - 1, posPopMachineY, z + 1, shuffledBlocks[i])
    
       
    return stepsGoal

def updateBlocks(mc, blocks):
    if (len(blocks) != len(posPosMachineZList)+1):
        return False

    i = 0
    for z in posPosMachineZList:
        mc.setBlock(posPopMachineX - 1, posPopMachineY, z - 1, blocks[i])
        i += 1
    
    mc.setBlock(posPopMachineX - 1, posPopMachineY, z + 1, blocks[i])
    return True
    
def checkBlocks(mc):

    global steps
    global goalSteps
    
    for z in posPosMachineZList:
        t1 = mc.getBlock(posPopMachineX - 1, posPopMachineY, z - 1)
        t2 = mc.getBlock(posPopMachineX - 1, posPopMachineY+2, z - 1)
        if t1 != t2:
            return False
        
    t1 = mc.getBlock(posPopMachineX - 1, posPopMachineY, z + 1)
    t2 = mc.getBlock(posPopMachineX - 1, posPopMachineY+2, z + 1)

    if t1 == t2:
        
        return True
    else:
        return False
    

def changeBlocks(mc, x, y, z):
    t1 = mc.getBlock(x, y, z-1)
    t2 = mc.getBlock(x, y, z+1)
    mc.setBlock(x, y, z-1, t2)
    mc.setBlock(x, y, z+1, t1)

def init(instMinecraft):
    global shuffledBlocks
    global sortedBlocks
    global steps
    global goalSteps

    blocks = initBlocks[:]
    
    mc = instMinecraft

    shuffledBlocks = shuffleBlocks(blocks)
    goalSteps = resetBlocks(mc)

    print("Sorted:")
    print(sortedBlocks)    
    print("Shuffled:")
    print(shuffledBlocks)

    steps = 0

def onSortMachineEvent(mc, blockEvent):
    global steps
    global goalSteps
    global shuffledBlocks
    
    blocks = initBlocks[:]
    
    flagFinished = False
    
    if blockEvent.pos.x == posPopMachineX and blockEvent.pos.y == posPopMachineY:
        if blockEvent.pos.z in posPosMachineZList:
            changeBlocks(mc, blockEvent.pos.x - 1, blockEvent.pos.y, blockEvent.pos.z)
            steps += 1
            flagFinished = checkBlocks(mc)
        elif blockEvent.pos.z == posPopMachineZ - 4:
            steps = 0
            goalSteps = resetBlocks(mc)
        elif blockEvent.pos.z == posPopMachineZ - 6:
            steps = 0
            shuffledBlocks = shuffleBlocks(blocks)
            goalSteps = resetBlocks(mc)
            mc.postToChat("Goal: "+str(goalSteps)+" steps")
        else:
            return False
    else:
        return False

    if flagFinished == True:
    
        if steps <= goalSteps:
            mc.postToChat("Yes!!! Well Done!!! Total steps: "+str(steps)+"/"+str(goalSteps))
        else:
            mc.postToChat("Try again! Try to use no more steps than "+str(goalSteps))

    return True
