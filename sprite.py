import pygame
import engine

class Sprite():

    def __init__(self, pos, dim, image):
        self.image = image
        self.angle = 0
        self.rect = pygame.Rect(pos[0], pos[1], dim[0], dim[1])
        self.orig_rect = pygame.Rect(pos[0], pos[1], dim[0], dim[1])
        self.sprite = pygame.image.load(image)
        self.sprite = pygame.transform.scale(self.sprite, (dim[0], dim[1]))
        self.orig_sprite = pygame.image.load(image)
        self.orig_sprite = pygame.transform.scale(self.sprite, (dim[0], dim[1]))

    def loadImage(self, image):
        # Load new image only if image has changed
        if self.image != image:
            self.image = image
            self.orig_sprite = pygame.image.load(image)
            self.orig_sprite = pygame.transform.scale(self.sprite, (self.rect.width, self.rect.height))
            self.rotateCenter()

    def draw(self):
        """ Draw sprite"""
        engine.screen.blit(self.sprite, self.rect)

    def rotate(self, angle):
        # Rotate by angle only if rotation needed
        if angle != 0:
            self.angle += angle
            self.rotateCenter()

    def setAngle(self,angle):
        # Set angle only if angle has changed
        if self.angle != angle:
            self.angle = angle
            self.rotateCenter()

    def moveToAndDraw(self, x, y):
        self.moveTo(x, y)
        self.draw()

    def moveTo(self, x, y):
        """ Move to point x,y """
        self.rect.x = x
        self.rect.y = y
        self.orig_rect.x = x
        self.orig_rect.y = y

    def move(self, x, y):
        """ Move rect by vector x,y """
        self.rect.move_ip(x, y)
        self.orig_rect.move_ip(x, y)

    def rotateCenter(self):
        """ Rotate an image while keeping its center """
        self.sprite = pygame.transform.rotate(self.orig_sprite, self.angle)
        self.rect = self.sprite.get_rect(center=self.orig_rect.center)
