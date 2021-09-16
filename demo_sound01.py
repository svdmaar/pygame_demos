import Demo
import pygame

class Demo_Sound01(Demo.Demo):
    def setup(self, screen):
        super().setup(screen)
        self.click_sound = pygame.mixer.Sound("assets/laser5.ogg")

    def render(self):
        pass

    def processEvent(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.click_sound.play()

    def getName(self):
        return "sound01: click to play sound effect"
