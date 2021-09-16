import Demo
import pygame

class Demo_Polygon01(Demo.Demo):
    def setup(self, screen):
        super().setup(screen)

    def render(self):
        color = (0, 0, 0)
        points = ((100, 100), (0, 200), (200, 200))
        width = 5
        pygame.draw.polygon(self.screen, color, points, width)
        color = (0, 100, 0)
        points = ((400, 100), (300, 200), (500, 200))
        width = 0 # fills
        pygame.draw.polygon(self.screen, color, points, width)

    def getName(self):
        return "polygon01"
