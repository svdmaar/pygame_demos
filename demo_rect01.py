import Demo
import pygame

# https://www.pygame.org/docs/ref/draw.html
# https://www.pygame.org/docs/ref/rect.html
class Demo_Rect01(Demo.Demo):
    def setup(self, screen):
        super().setup(screen)
        rectWidth = 100
        rectHeight = 50
        self.rect = pygame.Rect(0, 0, rectWidth, rectHeight)
        self.rect.centerx = 100
        self.rect.top = 60
        self.color = (255, 0, 0)

    def render(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

    def getName(self):
        return "rect01"
