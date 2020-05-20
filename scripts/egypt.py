from mcpi.minecraft import Minecraft
import time

def createPyra(r, meterial):
    
    pos = mc.player.getTilePos()

    y = pos.y

    print ("Player is at"+str(pos.x)+","+str(pos.y)+","+str(pos.z))
    while r >= 1:
        x0 = pos.x - r
        x1 = pos.x + r
        z0 = pos.z - r
        z1 = pos.z + r

        z = z0
        while z <= z1:
            mc.setBlock(x0, y, z, meterial)
            if r == 18:
                mc.setBlock(x0, y - 1, z, 89)
            mc.setBlock(x1, y, z, meterial)
            if r == 18:
                mc.setBlock(x1, y - 1, z, 89)
            if r == 5 and z == pos.z:
                createStairs(x, y, z, y - pos.y)
                
            z += 1

        x = x0
        while x <= x1:
            mc.setBlock(x, y, z0, meterial)
            if r == 18:
                mc.setBlock(x, y - 1, z0, 89)
            mc.setBlock(x, y, z1, meterial)
            if r == 18:
                mc.setBlock(x, y - 1, z1, 89)

            
            x += 1

        y += 1
        r -= 1

def createStairs(x0, y0, z0, height):    
    
    x = x0 - 1
    y = y0 - 1
    z = z0

    print("Creating stairs from ("+str(x0)+","+str(y0)+","+str(z0)+"), height "+str(height))


    while height >= 0:
        mc.setBlock(x, y, z, 128)
        x -= 1
        y -= 1
        height -= 1
        
def clearBase(position, halfLength, height):
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
                    mc.setBlock(x, y, z, 24)
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


mc = Minecraft.create()

size = 25
# mc.player.setTilePos(-76,64,-9)
clearBase(mc.player.getTilePos(), size+1, size+1)
createPyra(size, 179)



