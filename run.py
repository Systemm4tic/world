import ctypes
import engine
import pygame
import sys

from renderer import Renderer

class Game(object):

    def __init__(self):
        # Config
        tps_max = 1

        # Initialization
        pygame.init()
        engine.screen = self.set_screen_prop()
        tps_clock = pygame.time.Clock()
        engine.delta = 0.0
        self.renderer = Renderer()

        while True:
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    sys.exit(0)
                elif event.type == pygame.VIDEORESIZE:
                    engine.screen = self.set_screen_prop()

            # Ticking
            engine.delta += tps_clock.tick() / 1000.0
            while engine.delta > 1 / tps_max:
                self.tick()
                engine.delta -= 1 / tps_max

            # Drawing
            engine.screen.fill((255, 255, 255))
            self.draw()
            pygame.display.flip()

        pygame.quit()

    def tick(self):
        self.renderer.tick()

    def draw(self):
        self.renderer.draw()

    def set_screen_prop(self):
        """returns pygame screen with display resolution"""
        user32 = ctypes.windll.user32
        engine.resolution = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
        pygame.display.set_caption("World "+ engine.version)
        self.setBlockDimensions()
        return pygame.display.set_mode(engine.resolution, pygame.RESIZABLE)

    def setBlockDimensions(self):
        engine.bSize = int(engine.resolution[1] / engine.startY)

        # Add 2 or 3 blocks to avoid black spaces on sides of screen
        engine.noY = int(engine.resolution[1] / engine.bSize)
        if engine.noY * engine.bSize < engine.resolution[1]:
            engine.noY += 3
        else:
            engine.noY += 2

        engine.noX = int(engine.resolution[0] / engine.bSize)
        if engine.noX * engine.bSize < engine.resolution[0]:
            engine.noX += 3
        else:
            engine.noX += 2

        print("Block side size: " + str(engine.bSize))
        print("Number of blocks in X: " + str(engine.noX))
        print("Number of blocks in Y: " + str(engine.noY))

if __name__ == "__main__":
    Game()