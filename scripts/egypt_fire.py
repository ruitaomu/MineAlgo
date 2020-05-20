from mcpi.minecraft import Minecraft

mc = Minecraft.create()

while True:
    pos = mc.player.getTilePos()
    if mc.getBlock(pos.x, pos.y - 1, pos.z) == 12:
        mc.setBlock(pos.x, pos.y - 1, pos.z, 51)

