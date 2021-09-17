import Demo
import pygame

# https://www.pygame.org/docs/ref/joystick.html
# TODO: "hats"
class Demo_Joystick01(Demo.Demo):
    def setup(self, screen):
        super().setup(screen)
        self.joystickCount = pygame.joystick.get_count()
        defaultFontName = pygame.font.get_default_font()
        fontSize = 30
        self.font01 = pygame.font.SysFont(defaultFontName, fontSize)
        self.countSurface = self.font01.render("Joystick count: " + str(self.joystickCount), False, (0, 0, 0))
        if self.joystickCount > 0:
            self.joystick0 = pygame.joystick.Joystick(0)
            self.joystickNameSurface0 = self.font01.render(self.joystick0.get_name(), False, (0, 0, 0))
            self.axisCount0 = self.joystick0.get_numaxes()
            self.axisSurface0 = self.font01.render("Axis count: " + str(self.axisCount0), False, (0, 0, 0))
            self.buttonCount0 = self.joystick0.get_numbuttons()
            self.buttonSurface0 = self.font01.render("Button count: " + str(self.buttonCount0), False, (0, 0, 0))

    def render(self):
        # TODO: do we need to free these font surfaces?
        textY = 0
        self.screen.blit(self.countSurface, (0, 0))

        if self.joystickCount == 0:
            return

        textY += 30
        self.screen.blit(self.joystickNameSurface0, (0, textY))
        textY += 30
        self.screen.blit(self.axisSurface0, (0, textY))

        for i in range(self.axisCount0):
            axisStr = str(self.joystick0.get_axis(i))
            axisTextSurface = self.font01.render(axisStr, False, (0, 0, 0))
            textY += 30
            self.screen.blit(axisTextSurface, (0, textY))

        textY += 30
        self.screen.blit(self.buttonSurface0, (0, textY))
        for i in range(self.buttonCount0):
            buttonStr = str(self.joystick0.get_button(i))
            buttonTextSurface = self.font01.render(buttonStr, False, (0, 0, 0))
            textY += 30
            self.screen.blit(buttonTextSurface, (0, textY))

    def getName(self):
        return "joystick01: shows input of first joystick (if available)"
