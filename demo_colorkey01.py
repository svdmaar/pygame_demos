import Demo
import pygame

# https://www.pygame.org/docs/ref/surface.html#pygame.Surface.convert
# https://www.pygame.org/docs/ref/image.html#pygame.image.load
# https://www.pygame.org/docs/ref/surface.html#pygame.Surface.copy
class Demo_Colorkey01(Demo.Demo):
    def setup(self, screen):
        super().setup(screen)
        self.image = pygame.image.load("assets/xy01.bmp")

        # Convert it, so blitting is done optimally
        self.image = self.image.convert()

        upperRightX = self.image.get_rect().width - 1
        upperRightColor = self.image.get_at((upperRightX, 0))[:3]

        self.image2 = self.image.copy()
        self.image2.set_colorkey(upperRightColor)

    def render(self):
        self.screen.blit(self.image, (10, 10))
        self.screen.blit(self.image2, (40, 10))

    def getName(self):
        return "colorkey01"
