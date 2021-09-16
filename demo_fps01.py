import Demo
import pygame
from pygame.sprite import Group
from demo_sprite02 import Sprite02
from random import randint

class Demo_Fps01(Demo.Demo):
    def setup(self, screen):
        super().setup(screen)
        self.clock = pygame.time.Clock()
        defaultFontName = pygame.font.get_default_font()
        fontSize = 30
        self.font01 = pygame.font.SysFont(defaultFontName, fontSize)
        self.spriteGroup = Group()

    def addSprite(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        xCoor = mouse_x - 25
        yCoor = mouse_y - 25
        coors = (xCoor, yCoor)
        direction = (float(randint(-20, 20)) / 30.0, float(randint(-20, 20)) / 30.0)
        color = (randint(128, 255), randint(128, 255), randint(128, 255))
        addedSprite = Sprite02(self.screen, coors, color, direction)
        self.spriteGroup.add(addedSprite)

    def render(self):
        self.clock.tick()
        fps = int(self.clock.get_fps())
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.addSprite()
        self.spriteGroup.update()
        for sprite in self.spriteGroup.sprites():
            sprite.draw()
        textSurface = self.font01.render(str(fps), False, (0, 0, 0))
        self.screen.blit(textSurface, (0, 0))
        spriteCount = len(self.spriteGroup.sprites())
        textSurface = self.font01.render(str(spriteCount), False, (0, 0, 0))
        self.screen.blit(textSurface, (0, 20))

    def processEvent(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.addSprite()

    def getName(self):
        return "fps01: click or hold SPACE to add squares"
