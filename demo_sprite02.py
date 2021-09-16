import Demo
import pygame
from pygame.sprite import Sprite
from random import randint

class Sprite02(Sprite):
    def __init__(self, screen, coors = (50, 60), color = (0, 255, 0), direction = (0.2, 0.0)):
        super().__init__()
        self.screen = screen
        rectWidth = 50
        rectHeight = 50
        self.rect = pygame.Rect(0, 0, rectWidth, rectHeight)
        self.rect.centerx = coors[0] + rectWidth // 2
        self.rect.top = coors[1]
        self.color = color
        self.centerX = float(coors[0] + rectWidth // 2)
        self.centerY = float(coors[1] + rectHeight // 2)
        self.minCenterX = self.centerX
        self.direction = list(direction)
        self.screenRect = screen.get_rect()
        self.halfWidth = float(rectWidth // 2)
        self.halfHeight = float(rectHeight // 2)

    def update(self, vFactor = 1.0):
        # X
        self.centerX += vFactor * self.direction[0]
        if (self.centerX + self.halfWidth) > self.screenRect.width:
            self.centerX = float(self.screenRect.width) - self.halfWidth
            self.direction[0] *= -1.0
        if (self.centerX - self.halfWidth) < 0.0:
            self.centerX = self.halfWidth
            self.direction[0] *= -1.0
        self.rect.centerx = int(self.centerX)

        # Y
        self.centerY += vFactor * self.direction[1]
        if (self.centerY + self.halfHeight) > self.screenRect.height:
            self.centerY = float(self.screenRect.height) - self.halfHeight
            self.direction[1] *= -1.0
        if (self.centerY - self.halfHeight) < 0.0:
            self.centerY = self.halfHeight
            self.direction[1] *= -1.0
        self.rect.centery = int(self.centerY)

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

class Demo_Sprite02(Demo.Demo):
    def setup(self, screen):
        super().setup(screen)
        self.sprites = []
        for i in range(20):
            coors = (randint(100, 400), randint(100, 400))
            direction = (float(randint(10, 20)) / 30.0, float(randint(10, 20)) / 30.0)
            color = (randint(128, 255), randint(128, 255), randint(128, 255))
            addedSprite = Sprite02(screen, coors, color, direction)
            self.sprites.append(addedSprite)

    def render(self):
        for sprite in self.sprites:
            sprite.update()
            sprite.draw()

    def getName(self):
        return "sprite02"
