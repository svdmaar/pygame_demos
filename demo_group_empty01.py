import Demo
import pygame
from demo_sprite02 import Sprite02
from pygame.sprite import Sprite
from random import randint
from pygame.sprite import Group
import time

# https://www.pygame.org/docs/ref/sprite.html#pygame.sprite.Group.empty
class Demo_Group_Empty01(Demo.Demo):
    def setup(self, screen):
        super().setup(screen)
        self.spriteGroup = Group()
        for i in range(20):
            coors = (randint(100, 400), randint(100, 400))
            direction = (float(randint(10, 20)) / 30.0, float(randint(10, 20)) / 30.0)
            color = (randint(128, 255), randint(128, 255), randint(128, 255))
            addedSprite = Sprite02(screen, coors, color, direction)
            self.spriteGroup.add(addedSprite)
        self.startTime = int(time.time())
        self.emptiedGroup = False

    def render(self):
        if not self.emptiedGroup:
            currentTime = int(time.time())
            if currentTime > self.startTime + 5:
                self.spriteGroup.empty()
                self.emptiedGroup = True

        self.spriteGroup.update()
        for sprite in self.spriteGroup.sprites():
            sprite.draw()

    def getName(self):
        return "group_empty01: will empty the sprite group five seconds after start"
