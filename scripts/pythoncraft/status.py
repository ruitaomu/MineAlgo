from pythoncraft import world

pcWorldCreated = False
pcWorldUsername = ""
pcWorldAddress = "localhost"
pcWorldPort = 4711

def ensureWorldCreated():
    world.connect(pcWorldUsername, pcWorldAddress, pcWorldPort)