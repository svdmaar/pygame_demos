import Demo
import pygame

# https://www.pygame.org/docs/ref/rect.html
# https://www.pygame.org/docs/ref/surface.html
class Demo_Blit01(Demo.Demo):
    def setup(self, screen):
        super().setup(screen)
        self.image = pygame.image.load("assets/xy01.bmp")
        self.imageRect = self.image.get_rect()

        # https://stackoverflow.com/questions/20002242/how-to-scale-images-to-screen-size-in-pygame
        image2Size = (2 * self.imageRect.width, 2 * self.imageRect.height) 
        self.biggerImage = pygame.transform.scale(self.image, image2Size)
        self.imageRect2 = self.biggerImage.get_rect()

    def render(self):
        # Upper left.
        y = 20

        blitLocation = (10, y)
        blitSize = (self.imageRect.width, self.imageRect.height)
        y += 10 + blitSize[1]
        blitRect = pygame.Rect(blitLocation, blitSize)
        self.screen.blit(self.image, blitRect)

        blitLocation = (10, y)
        blitSize = (self.imageRect2.width, self.imageRect2.height)
        y += 10 + blitSize[1]
        blitRect = pygame.Rect(blitLocation, blitSize)
        self.screen.blit(self.biggerImage, blitRect)

    def getName(self):
        return "blit01"
