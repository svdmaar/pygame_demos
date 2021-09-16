import Demo
import pygame

class Demo_Blit02(Demo.Demo):
    def setup(self, screen):
        self.image = pygame.image.load("assets/four01.bmp")
        super().setup(screen)

    def render(self):
        self.screen.blit(self.image, (10, 10))
        self.screen.blit(self.image, (110, 10), (0, 0, 16, 16))
        self.screen.blit(self.image, (130, 10), (16, 0, 16, 16))
        self.screen.blit(self.image, (110, 30), (0, 16, 16, 16))
        self.screen.blit(self.image, (130, 30), (16, 16, 16, 16))

    def getName(self):
        return "blit02"
