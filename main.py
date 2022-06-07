# import modules
import time
import random
import os
import pygame as pg
import pygame.display

if not pg.font:
    print('Warning, fonts disabled!')
if not pg.mixer:
    print('Warning, sounds disabled!')


# GLOBAL LOADS AND FUNCTIONS HERE ********************************************************************************

main_dir = os.path.split(os.path.abspath(__file__))[0]
data_dir = os.path.join(main_dir, "data")
texture_dir = os.path.join(data_dir, "textures")
sound_dir = os.path.join(data_dir, "sound")


def load_image(name, colorkey=None, scale=1):
    fullname = os.path.join(texture_dir, name)
    image = pg.image.load(fullname)

    image = image.convert_alpha()

    size = image.get_size()
    size = (size[0] * scale, size[1] * scale)
    image = pg.transform.scale(image, size)

    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey, pg.RLEACCEL)
    return image, image.get_rect()


def load_sound(name):
    class NoneSound:
        def plat(self):
            pass

    if not pg.mixer or not pg.mixer.get_init():
        return NoneSound()

    fullname = os.path.join(sound_dir, name)
    sound = pg.mixer.Sound(fullname)

    return sound


# GAME ObJECT CLASSES HERE *********************************************************************************
class Pointer(pg.sprite.Sprite):
    """the mouse pointer class"""

    def __init__(self):
        pg.sprite.Sprite.__init__(self)     # call sprite init
        self.image, self.rect = load_image("pointer.png", -1, .1)
        self.click = False
        pg.event.set_grab(True)

    def update(self):
        """Move the mouse pointer"""
        pos = pg.mouse.get_pos()
        # reset pos tuple to keep mouse pointer in window
        if pos[0] > 1599:
            pos = (1599, pos[1])
            #pg.mouse.set_pos(pos)
        elif pos[0] < 1:
            pos = (1, pos[1])
            #pg.mouse.set_pos(pos)
        if pos[1] > 899:
            pos = (pos[0], 899)
            #pg.mouse.set_pos(pos)
        elif pos[1] < 1:
            pos = (pos[0], 1)
            #pg.mouse.set_pos(pos)
        if pg.mouse.get_pos() != pos:
            pg.mouse.set_pos(pos)
        self.rect.topleft = pos
        # print(pos, pg.mouse.get_pos())
        if self.click:
            # DO NOTHING RIGHT NOW FOR CLICK
            print("mouse click")
            None



# GAME LOOP HERE *******************************************************************************************

def GameLoop():

    running = True

    # loading screen
    fill_image = pg.image.load("data/textures/loading_screen.png")
    background.blit(fill_image, (0, 0))


    while running:
        clock.tick(60)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                running = False

        allsprites.update()

        screen.blit(background, (0, 0))
        allsprites.draw(screen)
        pg.display.flip()

    pg.quit()

# MAIN HERE ************************************************************************************************

if __name__ == '__main__':

    pg.init()

    SCREEN_WIDTH = 1600
    SCREEN_HEIGHT = 900

    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pg.display.set_caption("Tower Def")
    pg.mouse.set_visible(False)
    pg.mouse.set_cursor()

    background = pg.Surface(screen.get_size())
    background = background.convert()
    background.fill((170, 170, 170))

    screen.blit(background, (0, 0))
    pygame.display.flip()

    pointer = Pointer()

    allsprites = pg.sprite.RenderPlain((pointer))

    clock = pg.time.Clock()

    GameLoop()

    print('exiting...')
