<<<<<<< HEAD
import pygame
import panel
from enviroment import Enviroment
from player import Player
from panel import Panel

class Renderer():

    def __init__(self):
        self.player = Player()
        self.enviroment = Enviroment(self.player)
        self.lPanel = Panel(panel.POS_RIGHT)

    def tick(self):
        self.player.tick()
        self.enviroment.tick()

    def draw(self):
        self.enviroment.draw()
        self.player.draw()
        self.lPanel.draw()
=======
import pygame
import panel
from enviroment import Enviroment
from player import Player
from panel import Panel

class Renderer():

    def __init__(self):
        self.player = Player()
        self.enviroment = Enviroment(self.player)
        self.lPanel = Panel(panel.POS_RIGHT)

    def tick(self):
        self.player.tick()
        self.enviroment.tick()

    def draw(self):
        self.enviroment.draw()
        self.player.draw()
        self.lPanel.draw()
>>>>>>> c9577c66061b7a0bcf414469536be6821967ec0a
