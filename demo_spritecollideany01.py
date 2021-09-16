import Demo
import pygame
from demo_sprite01 import Sprite01
from pygame.sprite import Group
from demo_sprite02 import Sprite02

class Demo_Spritecollideany01(Demo.Demo):
    def setup(self, screen):
        super().setup(screen)
        self.group01 = Group()
        for yIndex in range(10):
            xCoor = 100
            yCoor = 20 + 60 * yIndex
            coors = (xCoor, yCoor)
            direction = (0.1, 0.0)
            color = (0, 255, 0)
            addedSprite = Sprite02(screen, coors, color, direction)
            self.group01.add(addedSprite)
        xCoor = 20 + 60 * 2
        yCoor = 100
        coors = (xCoor, yCoor)
        direction = (0.0, -0.1)
        color = (0, 0, 255)
        self.sprite02 = Sprite02(screen, coors, color, direction)

    def render(self):
        self.group01.update()
        for sprite in self.group01.sprites():
            sprite.draw()
        self.sprite02.update()

        if pygame.sprite.spritecollideany(self.sprite02, self.group01):
            self.sprite02.color = (255, 0, 0)
        else:
            self.sprite02.color = (0, 0, 255)

        self.sprite02.draw()

    def getName(self):
        return "spritecollideany01"
