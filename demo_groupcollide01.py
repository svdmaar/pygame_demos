import Demo
import pygame
from demo_sprite01 import Sprite01
from pygame.sprite import Group
from demo_sprite02 import Sprite02

# https://stackoverflow.com/questions/44914340/pygame-groupcollide
# https://www.pygame.org/docs/ref/sprite.html#pygame.sprite.groupcollide
class Demo_Groupcollide01(Demo.Demo):
    def setup(self, screen):
        super().setup(screen)
        self.group01 = Group()
        self.allSprites = []
        for yIndex in range(10):
            xCoor = 100
            yCoor = 20 + 60 * yIndex
            coors = (xCoor, yCoor)
            direction = (0.1, 0.0)
            color = (0, 255, 0)
            addedSprite = Sprite02(screen, coors, color, direction)
            addedSprite.orgColor = color
            self.group01.add(addedSprite)
            self.allSprites.append(addedSprite)
        self.group02 = Group()
        for xIndex in range(15):
            xCoor = 20 + 60 * xIndex
            yCoor = 100
            coors = (xCoor, yCoor)
            direction = (0.0, -0.1)
            color = (0, 0, 255)
            addedSprite = Sprite02(screen, coors, color, direction)
            addedSprite.orgColor = color
            self.group02.add(addedSprite)
            self.allSprites.append(addedSprite)

    def render(self):
        self.group01.update()
        self.group02.update()
        for sprite in self.allSprites:
            sprite.color = sprite.orgColor

        doKill01 = False
        doKill02 = False
        collisions = pygame.sprite.groupcollide(self.group01, self.group02, doKill01, doKill02)

        for sprite in collisions.keys():
            sprite.color = (255, 0, 0)
        for sprites in collisions.values():
            for sprite in sprites:
                sprite.color = (255, 0, 0)

        for sprite in self.group01.sprites():
            sprite.draw()
        for sprite in self.group02.sprites():
            sprite.draw()

    def getName(self):
        return "groupcollide01"
