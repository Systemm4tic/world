import engine
import images
from sprite import Sprite

class Panel():

    def __init__(self, position):
        width = engine.bSize * 3
        height = engine.resolution[1]
        self.posX = 0
        if position == POS_RIGHT:
            self.posX = engine.resolution[0] - width

        self.background = Sprite((self.posX, 0), (width, height), images.background_50)

    def draw(self):
        self.drawBackground()

    def tick(self):
        pass

    def drawBackground(self):
        # Draw grey background
        self.background.draw()

POS_LEFT = 1
POS_RIGHT = 2