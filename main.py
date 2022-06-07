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

    image = image.convert()

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
        self.image, self.rect = load_image("pointer.png")
        self.pointer_offset = (0, 0)
        self.click = False

    def update(self):
        """Move the mouse pointer"""
        pos = pg.mouse.get_pos()
        self.rect.topleft = pos
        self.rect.move_ip(self.pointer_offset)
        if self.click:
            # DO NOTHING RIGHT NOW FOR CLICK
            None

    def punch(self, target):
        """returns the object that is clicked if anything is under mouse"""
        if not self.click:
            self.click = True
            hitbox = self.rect.inflate(-5, -5)
            return hitbox.colliderect(target.rect)

    def unpunch(self):
        """unknown"""
        self.click = False



# GAME LOOP HERE *******************************************************************************************

def GameLoop():

    running = True

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
        pygame.display.flip()

    pg.quit()

# MAIN HERE ************************************************************************************************

if __name__ == '__main__':

    pg.init()

    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600

    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pg.display.set_caption("Tower Def")
    pg.mouse.set_visible(False)

    background = pg.Surface(screen.get_size())
    background = background.convert()
    background.fill((170, 170, 170))

    screen.blit(background, (0, 0))
    pygame.display.flip()

    spawn_sound = load_sound("short_roar.wav")

    pointer = Pointer()

    allsprites = pg.sprite.RenderPlain(pointer)

    clock = pg.time.Clock()

    GameLoop()

    print('exiting...')
