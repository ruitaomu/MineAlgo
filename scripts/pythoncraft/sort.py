import random

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


def closeDoor(mc):
    mc.setBlock(2969, 63, -40, 214)
    mc.setBlock(2969, 63, -35, 214)

def openDoor(mc):
    mc.setBlock(2969, 63, -40, 152)
    mc.setBlock(2969, 63, -35, 152)

def swapBlocks(x, y, z):
    global userSteps, mc

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
                break
    return temp            
    
def resetBlocks():    
    global sortedBlocks, userSteps
    global mc

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

    sortedBlocks = shuffledBlocks[:]
    mc.postToChat("Your new target steps: "+str(stepsGoal))
    return stepsGoal

def checkSucceed():
    global userSteps
    if sortedBlocks == initBlocks:
        return userSteps
    else:
        return -1

def updateBlocks(mc, blocks):

    if (len(blocks) != len(blockPoints)):
        return False

    i = 0
    for pos in blockPoints:
        mc.setBlock(pos[0], pos[1], pos[2], blocks[i])
        i += 1

    return True

def getShuffledBlocks():
    global shuffledBlocks
    return shuffledBlocks[:]

def init(minecraft):
    global initBlocks, shuffledBlocks, sortedBlocks, blockPoints, buttonPoints, targetSteps
    global mc 

    mc = minecraft
    initBlocks = [22, 41, 48, 57, 133, 169, 173, 201]
    shuffledBlocks = []
    sortedBlocks = []
    blockPoints = [(2961, 63, -36),(2961, 63, -38),(2961, 63, -40),(2963, 63, -40),(2965, 63, -40),(2966, 63, -39),(2966, 63, -37),(2966, 63, -35)]
    buttonPoints = [(2961, 63, -37),(2961, 63, -39),(2962, 63, -40),(2964, 63, -40),(2966, 63, -40),(2966, 63, -38),(2966, 63, -36)]

    shuffledBlocks = shuffleBlocks(initBlocks)
    targetSteps = resetBlocks()

                
                


                