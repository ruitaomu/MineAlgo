from mcpi.minecraft import Minecraft
import hanoi
import sort
import time

class Hanoi:
    def __init__(self, name = "", address = "mc.muruitao.cn"):
        self.minecraft = Minecraft.createMP("bot_asteacher", address)
        self.name = name
        self.reset()

    def move(self, poleFrom, poleTo):
        if (poleFrom < 1 or poleFrom > 3 or poleTo < 1 or poleTo > 3):
            return
        hanoi.move(self.minecraft, poleFrom-1, poleTo-1)

    def reset(self):
        hanoi.init(self.minecraft)
    
    def postToChat(self, message):
        self.minecraft.postToChat("[Hanoi - "+self.name+"]"+message)

class Sort:
    def __init__(self, name = "", address = "mc.muruitao.cn"):
        self.minecraft = Minecraft.createMP("bot_asteacher", address)
        self.name = name
        self.reset()
        self.arr = sort.getShuffledArray()
        self.postToChat("Start sorting, target steps: "+str(sort.bubbleSort(self.arr.copy())))

    def postToChat(self, message):
        self.minecraft.postToChat("[Sort - "+self.name+"]"+message)

    def array(self):
        return self.arr

    def reset(self):
        sort.init(self.minecraft)

    def update(self, arr):
        sort.updateBlocks(self.minecraft, arr)
        time.sleep(1)