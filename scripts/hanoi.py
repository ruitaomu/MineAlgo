from mcpi.minecraft import Minecraft
from mcpi.minecraft import Vec3
import time
import constants

blockSand = 12
blockBase = 100
blockBottom = 24
blockBeacon = 138
blockRedStone = 179
distance = 12
dishes = 3
zPole = []
xPole = 0
yPole = 0
fromPole = -1
toPole = -1

resetButtonX = constants.templeBasePosition_x + 30
resetButtonY = constants.templeBasePosition_y + 1
resetButtonZ = constants.templeBasePosition_z

def clearBase(mc, position, halfLength, height):
    x0 = position.x - halfLength
    y0 = position.y - 1
    z0 = position.z - halfLength
    x1 = position.x + halfLength
    y1 = position.y + height - 1
    z1 = position.z + halfLength

    x = x0
    y = y1
    z = z0
    
    while y>=y0:
        while z<=z1:
            while x<=x1:
                if y == y0:
                    mc.setBlock(x, y, z, blockBottom)
                else:
                    mc.setBlock(x, y, z, 0)
                x += 1
            else:
                x = x0
                z += 1
        else:
            z = z0
            x = x0
            y -= 1

def createDish(mc, xCenter, yCenter, zCenter, size, type):
    x0 = xCenter - (size - 1)
    x1 = xCenter + (size - 1)
    z0 = zCenter - (size - 1)
    z1 = zCenter + (size - 1)

    z = z0
    x = x0
    y = yCenter
    
    while z<=z1:
        while x<=x1:
            mc.setBlock(x, y, z, type)
            x += 1
        else:
            x = x0
            z += 1

def createBase(mc, xCenter, yCenter, zCenter, size):
    createDish(mc, xCenter, yCenter-1, zCenter, size, blockBase)

def getDishSize(mc, poleFrom, y):
    x0 = xPole - (dishes - 1)
    x1 = xPole
    z0 = zPole[poleFrom]

    size = 0
    x = x0
    while x <= x1:
        if mc.getBlock(x, y, z0) != 0:
            size += 1
        x += 1

    return size

    
def removeDish(mc, poleFrom, y):
    global xPole
    
    z0 = zPole[poleFrom]
    x0 = xPole
    size = getDishSize(mc, poleFrom, y)
    createDish(mc, x0, y, z0, size, 0)
    return size
    
def putDish(mc, poleTo, size):
    global xPole
    global yPole
    global zPole
    createDish(mc, xPole, yPole+dishes, zPole[poleTo], size, blockSand)

    
def getPiledHeight(mc, poleFrom):
    global yPole
    global xPole
    
    y0 = yPole
    z0 = zPole[poleFrom]
    x0 = xPole

    y1 = y0 + dishes - 1
    y = y0
    while y<=y1 and mc.getBlock(x0, y, z0) != 0:
        y += 1
#    print("pole "+str(poleFrom)+"has "+str(y-y0)+" dishes")
    return y - y0

def move(mc, poleFrom, poleTo):
     y = yPole + getPiledHeight(mc, poleFrom) - 1
     y1 = yPole + getPiledHeight(mc, poleTo) - 1
     if getPiledHeight(mc, poleTo) > 0 and getDishSize(mc, poleFrom, y) > getDishSize(mc, poleTo, y1):
         print("Can't move!")
         mc.postToChat("Can't move!")
     else:
         size = removeDish(mc, poleFrom, y)
         putDish(mc, poleTo, size)
     time.sleep(3)
     
def resetHanoi(instMinecraft):
    global xPole
    global yPole

    mc = instMinecraft
    
    size = dishes
    pos = Vec3(resetButtonX, resetButtonY, resetButtonZ)
    originPos = Vec3(resetButtonX, resetButtonY, resetButtonZ)
    pos.x += distance
    clearBase(mc, pos, size, dishes)
    pos.z -= size*2 + 1
    clearBase(mc, pos, size, dishes)
    pos.z += 2*(size*2 + 1)
    clearBase(mc, pos, size, dishes)
    xPole = pos.x
    pos.z -= 2*(size*2 + 1) 

    s = size

    yPole = pos.y
    num = 1
    

    while num <= 3:
        zPole.append(pos.z)
        while s >= 1:
            if s == size:
                createBase(mc, pos.x, pos.y, pos.z, size)
            if num == 1:
                createDish(mc, pos.x, pos.y, pos.z, s, blockSand)
            pos.y += 1
            s -= 1
        num += 1
        pos.z += (size*2+1)
        s = size
        pos.y = yPole

    mc.setBlock(originPos.x, originPos.y-1, originPos.z, blockRedStone)
##    mc.setBlock(39, 70, 76, 0)

def waitUntilStandingOnRedSandStone(mc):
    print("Go to the Red Stone to start!")
    while True:
        pos = mc.player.getTilePos()
        if mc.getBlock(pos.x, pos.y-1, pos.z) == blockRedStone:
            break;
    print(pos)

def tryMove(fromPole, toPole, num):
    mc = Minecraft.create()
    
    if fromPole == 0 and toPole == 1:
        otherPole = 2
    if fromPole == 0 and toPole == 2:
        otherPole = 1
    if fromPole == 1 and toPole == 0:
        otherPole = 2
    if fromPole == 1 and toPole == 2:
        otherPole = 0
    if fromPole == 2 and toPole == 0:
        otherPole = 1
    if fromPole == 2 and toPole == 1:
        otherPole = 0
        
    if num == 1:
        move(mc, fromPole, toPole)
    else:
        tryMove(fromPole, otherPole, num-1)
        move(fromPole, toPole)
        tryMove(otherPole, toPole, num-1)
        
def onHanoiMachineEvent(mc, blockEvent):
    global fromPole
    global toPole
    
    x = blockEvent.pos.x
    y = blockEvent.pos.y
    z = blockEvent.pos.z

    clicked = -1

    if x == resetButtonX and y == resetButtonY and z == resetButtonZ:
        resetHanoi(mc)
    elif x == resetButtonX + 6 and y == resetButtonY:
        print("hanoi button")
        if z == resetButtonZ - 7:
            clicked = 0
        elif z == resetButtonZ:
            clicked = 1
        elif z == resetButtonZ + 7:
            clicked = 2
        else:
            return False
    else:
        return False

    if clicked != -1:
        if fromPole == -1:
            fromPole = clicked
        else:
            toPole = clicked

        if fromPole != -1 and toPole != -1:
            move(mc, fromPole, toPole)
            fromPole = -1
            toPole = -1
            if getPiledHeight(mc, 1) == dishes:
                mc.postToChat("Congratulations!!!")
            
    return True

def init(mc):
    resetHanoi(mc)
        
##mc = Minecraft.create()
##
##notEnd = True
##
##while notEnd:
##    waitUntilStandingOnRedSandStone()
##    print("OK! Ready to start!")
##    init()
##
###    tryMove(0, 1, 3)
##
###    mc.setBlock(39, 70, 76, blockBeacon)
##
##    while True:
##        try:
##            fromPole = int(input("from(input 0~2, -1 to quit):"))
##            if fromPole == -1:
##                notEnd = False
##                break;
##            toPole = int(input("to(input 0~2:"))
##            if fromPole < 0 or fromPole > 2 or toPole < 0 or toPole > 2:
##                print("Number must be 0, 1 or 2!")
##                continue
##            move(fromPole, toPole)
##            if getPiledHeight(1) == 3:
##                mc.setBlock(39, 70, 76, blockBeacon)
##                mc.postToChat("Congratulations!!!")
##        except:
##            print("Invalid input: please enter a number (0-2)");
##
