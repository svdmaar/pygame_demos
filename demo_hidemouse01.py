import Demo
import pygame

class Demo_Hidemouse01(Demo.Demo):
    def setup(self, screen):
        super().setup(screen)
        self.mouseVisible = True

    def render(self):
        pass

    def processEvent(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.mouseVisible = not self.mouseVisible
            pygame.mouse.set_visible(self.mouseVisible)

    def getName(self):
        return "hidemouse01: click to hide/show mouse"
