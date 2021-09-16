import Demo
import pygame

# https://file-examples-com.github.io/uploads/2017/11/file_example_MP3_700KB.mp3
# https://stackoverflow.com/questions/43845800/how-do-i-add-background-music-to-my-python-game/43853660
# https://www.pygame.org/docs/ref/mixer.html
# https://www.pygame.org/docs/ref/music.html#module-pygame.mixer.music
class Demo_Music01(Demo.Demo):
    def setup(self, screen):
        super().setup(screen)
        self.playing = False

    def render(self):
        pass

    def processEvent(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if not self.playing:
                pygame.mixer.music.load("music/file_example_MP3_700KB.mp3")
                pygame.mixer.music.play(loops = -1) # loops = -1 : repeats forever
                self.playing = True
            else:
                pygame.mixer.music.stop()
                pygame.mixer.music.unload()
                self.playing = False

    def getName(self):
        return "music01: click to start/stop music, music will restart at end (loops forever)"
