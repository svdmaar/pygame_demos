import pygame
import sys
import demo_blit01
import demo_font01
import demo_key01
import demo_rect01
import demo_sprite01
import demo_group01
import demo_groupcollide01
import demo_sprite02
import demo_group_empty01
import demo_spritecollideany01
import demo_font02
import demo_mouse01
import demo_hidemouse01
import demo_line01
import demo_ellipse01
import demo_polygon01
import demo_joystick01
import demo_colorkey01
import demo_sound01
import demo_music01
import demo_blit02
import demo_fps01
import demo_fps02
import demo_fps03
import demo_scale_rotate01
# Add extra demo import here

if __name__ == "__main__":
    demos = [
        demo_blit01.Demo_Blit01(),
        demo_key01.Demo_Key01(),
        demo_rect01.Demo_Rect01(),
        demo_sprite01.Demo_Sprite01(),
        demo_group01.Demo_Group01(),
        demo_sprite02.Demo_Sprite02(),
        demo_groupcollide01.Demo_Groupcollide01(),
        demo_group_empty01.Demo_Group_Empty01(),
        demo_spritecollideany01.Demo_Spritecollideany01(),
        demo_font01.Demo_Font01(),
        demo_font02.Demo_Font02(),
        demo_mouse01.Demo_Mouse01(),
        demo_hidemouse01.Demo_Hidemouse01(),
        demo_line01.Demo_Line01(),
        demo_ellipse01.Demo_Ellipse01(),
        demo_polygon01.Demo_Polygon01(),
        demo_joystick01.Demo_Joystick01(),
        demo_colorkey01.Demo_Colorkey01(),
        demo_sound01.Demo_Sound01(),
        demo_music01.Demo_Music01(),
        demo_blit02.Demo_Blit02(),
        demo_fps01.Demo_Fps01(),
        demo_fps02.Demo_Fps02(),
        demo_fps03.Demo_Fps03(),
        demo_scale_rotate01.Demo_Scale_Rotate01(),
        # Add extra demo instantiation here
    ]

    currentDemoIndex = 0
    currentDemo = demos[currentDemoIndex]
    pygame.init()

    display = pygame.display
    screen = display.set_mode((1200, 800))

    display.set_caption("pygame02 - " + currentDemo.getName() + " - press TAB to cycle through demos")

    # TODO: black
    backgroundColor = (230, 230, 230)

    currentDemo.setup(screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            elif (event.type == pygame.KEYDOWN or event.type == pygame.KEYDOWN) and event.key == pygame.K_TAB:
                if event.type == pygame.KEYDOWN:
                    currentDemo.cleanup()
                    currentDemoIndex = (currentDemoIndex + 1) % len(demos)
                    currentDemo = demos[currentDemoIndex]
                    currentDemo.setup(screen)
                    display.set_caption("pygame02 - " + currentDemo.getName())
            else:
                currentDemo.processEvent(event)

        screen.fill(backgroundColor)

        currentDemo.render()

        display.flip()
