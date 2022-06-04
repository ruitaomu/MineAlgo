from pythoncraft.stage import Spot

class SpotHelloworld(Spot):
    def __init__(self):
        super().__init__(False, True, False)

    def say(self, content):
        super().say(content)
        if content == "hello":
            self.done()