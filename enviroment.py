<<<<<<< HEAD
import engine
import images
from maps import Maps
from sprite import Sprite


class Enviroment():

    def __init__(self, player):
        self.player = player
        self.mapGround = Maps()

        self.grounds = []
        self.loadImages()

    def tick(self):
        pass

    def draw(self):
        self.drawGround()

    def drawGround(self):
        for i in range(0,engine.noX):
            for j in range(0, engine.noY):
                mapX = int(self.player.pos.x + i)
                mapY = int(self.player.pos.y + j)
                scrX = (i-1) * engine.bSize         # i-1 to avoid displaying blanco space
                scrY = (j-1) * engine.bSize         # j-1 to avoid displaying blanco space
                self.grounds[self.mapGround.map[mapX][mapY]-1].moveToAndDraw(scrX, scrY)

    def loadImages(self):
        # Load all ground images
        for gr in images.grounds:
            self.grounds.append(Sprite((0, 0), (engine.bSize, engine.bSize), gr))
=======
import engine
import images
from maps import Maps
from sprite import Sprite


class Enviroment():

    def __init__(self, player):
        self.player = player
        self.mapGround = Maps()

        self.grounds = []
        self.loadImages()

    def tick(self):
        pass

    def draw(self):
        self.drawGround()

    def drawGround(self):
        for i in range(0,engine.noX):
            for j in range(0, engine.noY):
                mapX = int(self.player.pos.x + i)
                mapY = int(self.player.pos.y + j)
                scrX = (i-1) * engine.bSize         # i-1 to avoid displaying blanco space
                scrY = (j-1) * engine.bSize         # j-1 to avoid displaying blanco space
                self.grounds[self.mapGround.map[mapX][mapY]-1].moveToAndDraw(scrX, scrY)

    def loadImages(self):
        # Load all ground images
        for gr in images.grounds:
            self.grounds.append(Sprite((0, 0), (engine.bSize, engine.bSize), gr))
>>>>>>> c9577c66061b7a0bcf414469536be6821967ec0a
