from mcpi.minecraft import Minecraft
from mcpi.vec3 import Vec3
from pythoncraft import status
from pythoncraft.spots.spot_helloworld import SpotHelloworld
from pythoncraft.spots.spot_invalid import SpotInvalid
from pythoncraft.spots.spot_megajump import SpotMegaJump
from pythoncraft.spots.spot_lavabridge import SpotLavaBridge
from pythoncraft.spots import MakeStairs
from pythoncraft.spots import PutGlass
from pythoncraft.spots import Pyramid
from pythoncraft.spots import Maze
from pythoncraft.spots import RailMaze

spotList = {(1, 24, 89, 1, 24, 89, 1, 0, 89) : SpotHelloworld(),
            (0, 43, 1, 0, 1, 0, 0, 43, 0) : SpotMegaJump(),
            (20, 20, 20, 155, 155, 155, 24, 24, 24) : SpotLavaBridge(),
            (24, 128, 0, 24, 24, 128, 24, 128, 0) : MakeStairs.MagicSpot(),
            (24, 95, 24, 24, 24, 24, 95, 24, 95) : PutGlass.MagicSpot(),
            (11, 11, 11, 24, 24, 24, 97, 97, 97) : Pyramid.MagicSpot(),
            (24, 24, 24, 24, 42, 169, 24, 24, 24) : Maze.MagicSpot(),
            (24, 9, 24, 24, 24, 24, 9, 9, 24) : RailMaze.MagicSpot()}

_currentSpot = None

def connect(username = "", address = "localhost", port = 4711):
    global pcMinecraft
    global _currentSpot
    if status.pcWorldCreated == False:
        if username == "":
            pcMinecraft = Minecraft.create(address, port)
        else:
            pcMinecraft = Minecraft.createMP(username, address, port)
        status.pcWorldCreated = True
        _currentSpot = None

def getStageSpot(x, y, z):
    global _currentSpot
    if _currentSpot != None:
        return _currentSpot

    spotCenter = calibrateSpotCenter(x, y, z)
    x = spotCenter.x
    y = spotCenter.y
    z = spotCenter.z

    print("Calibrated to: "+str(spotCenter))
    
    if (pcMinecraft.getBlock(x,y,z) == 120):
        spotFeature = (pcMinecraft.getBlock(x-1,y-1,z-1), pcMinecraft.getBlock(x,y-1,z-1), pcMinecraft.getBlock(x+1,y-1,z-1),
                   pcMinecraft.getBlock(x-1,y-1,z),   pcMinecraft.getBlock(x,y-1,z),   pcMinecraft.getBlock(x+1,y-1,z),
                   pcMinecraft.getBlock(x-1,y-1,z+1), pcMinecraft.getBlock(x,y-1,z+1), pcMinecraft.getBlock(x+1,y-1,z+1))

        
        print(spotFeature)
        #spot = SpotInvalid()
        spot = spotList[spotFeature]
    else:
        spot = SpotInvalid()
    spot.setPos(x, y, z)
    _currentSpot = spot
    return spot

def calibrateSpotCenter(x, y, z):
    blocks = list(pcMinecraft.getBlocks(x-1, y-1, z-1, x+1, y, z+1))
    print(blocks)
    for i in range(0, 3):
        for j in range(0, 3):
            if (blocks[i*3 + j] == 120):
                return Vec3(x-1+i, y-1, z-1+j)
            if (blocks[i*3 + j + 9] == 120):
                return Vec3(x-1+i, y, z-1+j)
            

    return Vec3(x, y, z)