from mcpi.minecraft import Minecraft
import hanoi
import sort
import Temp2ndFloorMaze

mc = Minecraft.createMP("bot_asteacher", "mc.muruitao.cn")

hanoi.init(mc)
sort.init(mc)
Temp2ndFloorMaze.init(mc)

mc.postToChat("Your AlgoWorld has been initialized")