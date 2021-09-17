import Demo
import pygame

class Demo_Scale_Rotate01(Demo.Demo):
    def setup(self, screen):
        super().setup(screen)
        self.image = pygame.image.load("assets/xy01.bmp")
        self.transImage = self.image.copy()
        upperRightX = self.image.get_rect().width - 1
        upperRightColor = self.image.get_at((upperRightX, 0))[:3]
        self.transImage.set_colorkey(upperRightColor)
        self.scaleFactor = 1.0
        self.rotation = 0.0
        self.x = 10
        self.y = 10
        self.orgWidth = self.image.get_rect().width
        self.orgHeight = self.image.get_rect().height
        self.transparent = False

    def render(self):
        scaleFactor = 1.001
        rotationSpeed = 0.1
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.scaleFactor *= scaleFactor
        if keys[pygame.K_z]:
            self.scaleFactor /= scaleFactor
        if keys[pygame.K_UP]:
            self.y -= 1
        if keys[pygame.K_DOWN]:
            self.y += 1
        if keys[pygame.K_LEFT]:
            self.x -= 1
        if keys[pygame.K_RIGHT]:
            self.x += 1
        if keys[pygame.K_q]:
            self.rotation -= rotationSpeed
        if keys[pygame.K_w]:
            self.rotation += rotationSpeed
        newWidth = int(self.scaleFactor * self.orgWidth)
        newHeight = int(self.scaleFactor * self.orgHeight)
        drawnImage = self.image
        if self.transparent:
            drawnImage = self.transImage
        scaledImage = pygame.transform.scale(drawnImage, (newWidth, newHeight))
        rotatedImage = pygame.transform.rotate(scaledImage, self.rotation)
        self.screen.blit(rotatedImage, (self.x, self.y, newWidth, newHeight))

    def processEvent(self, event):
        if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_e):
            self.transparent = not self.transparent

    def getName(self):
        return "scale_rotate01: Arrow keys to move, A/Z to scale, Q/W to rotate, E to change transparency"
