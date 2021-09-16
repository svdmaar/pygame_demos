import Demo
import pygame

class Demo_Key01(Demo.Demo):
    def setup(self, screen):
        super().setup(screen)
        self.up = False
        self.down = False
        self.left = False
        self.right = False
        defaultFontName = pygame.font.get_default_font()
        fontSize = 30
        self.font01 = pygame.font.SysFont(defaultFontName, fontSize)

    def render(self):
        renderedString = ""
        if self.up:
            renderedString += "up "
        if self.down:
            renderedString += "down "
        if self.left:
            renderedString += "left "
        if self.right:
            renderedString += "right "
        renderedString = renderedString.strip()
        textSurface = self.font01.render(renderedString, False, (0, 0, 0))
        self.screen.blit(textSurface, (0, 0))

    def getName(self):
        return "key01: shows which arrow keys are pressed"

    def processEvent(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.up = True
            elif event.key == pygame.K_DOWN:
                self.down = True
            elif event.key == pygame.K_LEFT:
                self.left = True
            elif event.key == pygame.K_RIGHT:
                self.right = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                self.up = False
            elif event.key == pygame.K_DOWN:
                self.down = False
            elif event.key == pygame.K_LEFT:
                self.left = False
            elif event.key == pygame.K_RIGHT:
                self.right = False

