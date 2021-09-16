import Demo
import pygame
from pygame.sprite import Sprite

# https://www.pygame.org/docs/ref/sprite.html
# https://www.pygame.org/docs/ref/sprite.html#pygame.sprite.Sprite
class Sprite01(Sprite):
    def __init__(self, screen, coors = (50, 60), color = (0, 255, 0), direction = (0.2, 0.0)):
        super().__init__()
        self.screen = screen
        rectWidth = 100
        rectHeight = 50
        self.rect = pygame.Rect(0, 0, rectWidth, rectHeight)
        self.rect.centerx = coors[0] + rectWidth // 2
        self.rect.top = coors[1]
        self.color = color
        self.centerX = float(coors[0] + rectWidth // 2)
        self.maxX = float(self.centerX + 300)
        self.minCenterX = self.centerX
        self.direction = list(direction)

    def update(self):
        # Needs to have this name to be used from a Group
        self.centerX += 0.2
        if self.centerX > self.maxX:
            self.centerX = float(self.minCenterX)
        self.rect.centerx = int(self.centerX)

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

class Demo_Sprite01(Demo.Demo):
    def setup(self, screen):
        super().setup(screen)
        self.sprite01 = Sprite01(screen)

    def render(self):
        self.sprite01.update()
        self.sprite01.draw()

    def getName(self):
        return "sprite01"
