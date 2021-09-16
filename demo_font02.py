import Demo
import pygame

class Demo_Font02(Demo.Demo):
    def setup(self, screen):
        super().setup(screen)
        defaultFontName = pygame.font.get_default_font()
        fontSize = 100
        self.font01 = pygame.font.SysFont(defaultFontName, fontSize)
        self.textSurface = self.font01.render("Green Text in a Blue Box", False, (0, 255, 0))
        textWidth = self.textSurface.get_rect().width
        textHeight = self.textSurface.get_rect().height
        screenWidth = screen.get_rect().width
        screenHeight = screen.get_rect().height
        self.textUpperLeft = ((screenWidth - textWidth) // 2, (screenHeight - textHeight) // 2)
        self.boxRect = pygame.Rect(self.textUpperLeft[0], self.textUpperLeft[1], textWidth, textHeight)
        #self.textSize = ()

    def render(self):
        pygame.draw.rect(self.screen, (0, 0, 255), self.boxRect)
        self.screen.blit(self.textSurface, self.textUpperLeft)

    def getName(self):
        return "font02"
