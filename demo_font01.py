import Demo
import pygame

# https://www.pygame.org/docs/ref/font.html
# https://stackoverflow.com/questions/20842801/how-to-display-text-in-pygame
class Demo_Font01(Demo.Demo):
    def setup(self, screen):
        super().setup(screen)
        defaultFontName = pygame.font.get_default_font()
        fontSize = 30
        self.font01 = pygame.font.SysFont(defaultFontName, fontSize)

    def render(self):
        textSurface = self.font01.render("Some Text", False, (0, 0, 0))
        self.screen.blit(textSurface, (0, 0))

    def getName(self):
        return "font01"

