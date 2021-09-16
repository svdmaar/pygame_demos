import Demo
import pygame
from pygame.sprite import Group
from demo_sprite02 import Sprite02
from random import randint

class Demo_Mouse01(Demo.Demo):
    def setup(self, screen):
        super().setup(screen)
        self.spriteGroup = Group()

    def render(self):
        self.spriteGroup.update()
        for sprite in self.spriteGroup.sprites():
            sprite.draw()

    def processEvent(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            xCoor = mouse_x - 25
            yCoor = mouse_y - 25
            coors = (xCoor, yCoor)
            direction = (float(randint(-20, 20)) / 30.0, float(randint(-20, 20)) / 30.0)
            color = (randint(128, 255), randint(128, 255), randint(128, 255))
            addedSprite = Sprite02(self.screen, coors, color, direction)
            self.spriteGroup.add(addedSprite)

    def getName(self):
        return "mouse01: processes clicks"
