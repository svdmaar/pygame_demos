import Demo
import pygame
from demo_sprite01 import Sprite01
from pygame.sprite import Group
import time

# https://stackoverflow.com/questions/13851051/how-to-use-sprite-groups-in-pygame
# https://stackoverflow.com/questions/4548684/how-to-get-the-seconds-since-epoch-from-the-time-date-output-of-gmtime
class Demo_Group01(Demo.Demo):
    def setup(self, screen):
        super().setup(screen)
        self.group01 = Group()
        self.spriteCount = 4
        yStep = 60
        xStep = 50
        for i in range(self.spriteCount):
            spriteCoors = (100 + i * xStep, 120 + i * yStep)
            spriteColor = [0, 0, 255]
            if i < 2:
                spriteColor[0] = 255
            if i % 2 == 0:
                spriteColor[1] = 255
            addedSprite = Sprite01(screen, spriteCoors, spriteColor)
            self.group01.add(addedSprite)
        self.startTime = int(time.time())
        self.removedSprite = False

    def render(self):
        if not self.removedSprite:
            currentTime = int(time.time())
            if currentTime > self.startTime + 5:
                lastSprite = self.group01.sprites()[self.spriteCount - 1]
                self.group01.remove(lastSprite)
                self.removedSprite = True

        self.group01.update()
        for sprite01 in self.group01.sprites():
            sprite01.draw()

    def getName(self):
        return "group01"
