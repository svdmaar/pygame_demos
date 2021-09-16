import Demo
import pygame

# https://www.pygame.org/docs/ref/draw.html#pygame.draw.ellipse
# https://www.pygame.org/docs/ref/draw.html#pygame.draw.arc
class Demo_Ellipse01(Demo.Demo):
    def setup(self, screen):
        super().setup(screen)

    def render(self):
        color = (0, 0, 0)
        rect = (20, 40, 250, 200)
        width = 2
        pygame.draw.ellipse(self.screen, color, rect, width)
        color = (0, 100, 0)
        rect = (420, 40, 250, 200)
        pygame.draw.arc(self.screen, color, rect, 3.14 / 2.0, 3.14, width)

    def getName(self):
        return "ellipse01"
