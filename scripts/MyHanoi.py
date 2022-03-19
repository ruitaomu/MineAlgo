import PythonClass

a = 3
b = 0
c = 0

def move(poleFrom, poleTo, poleIdle, num):
    global a
    global b
    global c

    if num > 1:
        move(poleFrom, poleIdle, poleTo, num - 1)
        move(poleFrom, poleTo, poleIdle, 1)
        move(poleIdle, poleTo, poleFrom, num - 1)
    else:
        pyc_hanoi.postToChat("Moving from "+str(poleFrom)+" to "+str(poleTo))

        pyc_hanoi.move(poleFrom, poleTo)
        
        if poleFrom == 1:
            a -= 1
        elif poleFrom == 2:
            b -= 1
        else:
            c -= 1

        if poleTo == 1:
            a += 1
        elif poleTo == 2:
            b += 1
        else:
            c += 1

#Program starts from here:
pyc_hanoi = PythonClass.Hanoi()

#Move dishes from Pole #1 to Pole #2, via Pole #3, total 3 dishes
move(1, 2, 3, 3)

pyc_hanoi.postToChat("Done!")
