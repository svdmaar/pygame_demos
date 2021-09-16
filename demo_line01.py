import Demo
import pygame

class Demo_Line01(Demo.Demo):
    def setup(self, screen):
        super().setup(screen)

    def render(self):
        color = (0, 255, 0)
        start_pos = (0, 0)
        end_pos = (100, 100)
        width = 5
        pygame.draw.line(self.screen, color, start_pos, end_pos, width)
        color = (0, 0, 255)
        start_pos = (20, 100)
        end_pos = (200, 400)
        pygame.draw.line(self.screen, color, start_pos, end_pos, width)

    def getName(self):
        return "line01"
