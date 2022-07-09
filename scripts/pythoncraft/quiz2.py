from mcpi.minecraft import Minecraft
import pythoncraft.hanoi as hanoi
        
def onHanoiMachineEvent(mc, blockEvent):
    
    x = blockEvent.pos.x
    y = blockEvent.pos.y
    z = blockEvent.pos.z

    clicked = -1

    if x == hanoi.resetButtonX and y == hanoi.resetButtonY and z == hanoi.resetButtonZ:
        hanoi.resetHanoi(mc)
    elif x == hanoi.hanoiButtonX and y == hanoi.hanoiButtonY:
        if z == hanoi.resetButtonZ - 7:
            clicked = 0
        elif z == hanoi.resetButtonZ:
            clicked = 1
        elif z == hanoi.resetButtonZ + 7:
            clicked = 2
        else:
            return False
    else:
        return False

    if clicked != -1:
        if hanoi.fromPole == -1:
            hanoi.fromPole = clicked
        else:
            hanoi.toPole = clicked

        if hanoi.fromPole != -1 and hanoi.toPole != -1:
            hanoi.move(mc, hanoi.fromPole, hanoi.toPole)
            hanoi.fromPole = -1
            hanoi.toPole = -1
            if hanoi.getPiledHeight(mc, 1) == hanoi.dishes:
                mc.postToChat("Congratulations!!!")
                return True
            
    return False

def start(num = 3):

    if num != 3 and num != 4:
        return

    mc = Minecraft.create()

    dishes = num

    hanoi.init(mc, dishes)
    flagFinished = False
    while flagFinished == False:
        blockEvents = mc.player.pollBlockHits()
        for blockEvent in blockEvents:
            if onHanoiMachineEvent(mc, blockEvent) == True:
                flagFinished = True
                break