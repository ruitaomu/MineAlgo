from mcpi.minecraft import Vec3
import time

blockSand = 12
blockBase = 100
blockBottom = 24
blockBeacon = 138
distance = 8
dishes = 3
zPole = []
xPole = 0
yPole = 0
fromPole = -1
toPole = -1

resetButtonX = 2940
resetButtonY = 51
resetButtonZ = -156

hanoiButtonX = resetButtonX + 2
hanoiButtonY = resetButtonY - 1

def clearWholeSpace(mc, centerPos):
    x0 = centerPos.x - 4
    y0 = centerPos.y - 1
    z0 = centerPos.z - 13
    x1 = centerPos.x + 4
    y1 = centerPos.y + 4 - 1
    z1 = centerPos.z + 13

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
    print("pole "+str(poleFrom)+"has "+str(y-y0)+" dishes")
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

    pos.y = pos.y - 1
    originPos.y = originPos.y - 1

    pos.x += distance

    clearWholeSpace(mc, pos)

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



# def tryMove(mc, fromPole, toPole, num):
    
#     if fromPole == 0 and toPole == 1:
#         otherPole = 2
#     if fromPole == 0 and toPole == 2:
#         otherPole = 1
#     if fromPole == 1 and toPole == 0:
#         otherPole = 2
#     if fromPole == 1 and toPole == 2:
#         otherPole = 0
#     if fromPole == 2 and toPole == 0:
#         otherPole = 1
#     if fromPole == 2 and toPole == 1:
#         otherPole = 0
        
#     if num == 1:
#         move(mc, fromPole, toPole)
#     else:
#         tryMove(mc, fromPole, otherPole, num-1)
#         move(mc, fromPole, toPole)
#         tryMove(mc, otherPole, toPole, num-1)

def init(mc, num):
    global dishes
    dishes = num
    resetHanoi(mc)