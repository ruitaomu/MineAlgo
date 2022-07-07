from mcpi.minecraft import Minecraft
import pythoncraft.sort as sort
import pythoncraft.hanoi as hanoi

import time

class Sort:
    def __init__(self):
        self.minecraft = Minecraft.create()
        self.reset()
        self.arr = sort.getShuffledBlocks()
        self.postToChat("Start sorting, target steps: "+str(sort.bubbleSort(self.arr.copy())))

    def postToChat(self, message):
        self.minecraft.postToChat("[Sort]"+message)

    def array(self):
        return self.arr

    def reset(self):
        sort.init(self.minecraft)

    def update(self, arr):
        sort.updateBlocks(self.minecraft, arr)
        time.sleep(1)

class Hanoi:
    def __init__(self, dishes):
        self.minecraft = Minecraft.create()
        self.reset(dishes)

    def move(self, poleFrom, poleTo):
        if (poleFrom < 1 or poleFrom > 3 or poleTo < 1 or poleTo > 3):
            return
        hanoi.move(self.minecraft, poleFrom-1, poleTo-1)

    def reset(self, dishes):
        hanoi.init(self.minecraft, dishes)
    
    def postToChat(self, message):
        self.minecraft.postToChat("[Hanoi]"+message)
