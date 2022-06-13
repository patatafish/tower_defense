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

ADMIN = True
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


# GAME ObJECT CLASSES HERE *********************************************************************************
class Menu():

    def __init__(self):
        self.menu_x = 800
        self.menu_y = 1600
        self.menu_background = pg.Surface((menu_x, menu_y))
        self.menu_background.fill((0, 0, 0))
        self.menu_background_rect = self.menu_background.get_rect(center = center_screen)
        self.menu_options = ['NEW', 'SAVE', 'QUIT']
        if ADMIN:
            self.menu_options.append('EDIT')

    def show(self):
        print("Menu called...")
        self.render_menu()
        return(False)

    def render_menu(self):
        print("Entering render...")
        screen.blit(self.menu_background, self.menu_background_rect)

        menu_len = len(self.menu_options)
        option_height = self.menu_x / menu_len
        for item in self.menu_options:


        pg.display.update()

        time.sleep(2)


class Pointer(pg.sprite.Sprite):

    def __init__(self):
        super(Pointer, self).__init__()

    def update(self):
        if ADMIN is True:
            mouse_pos = pg.mouse.get_pos()
            mouse_pos = f"x:{mouse_pos[0]}, y:{mouse_pos[1]}"
            self.font = pg.font.Font(None, 36)
            self.textSurf = self.font.render(mouse_pos, True, WHITE, BLACK)
            self.image = pygame.Surface((175, 35))
            self.image.blit(self.textSurf, (5, 5))
            screen.blit(self.image, (5, 5))

# GAME LOOP HERE *******************************************************************************************

def GameLoop():

    running = True

    game_menu = Menu()
    pointer = Pointer()

    render_group = pg.sprite.Group(pointer)

    while running:
        clock.tick(60)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                running = game_menu.show()

        render_group.update()
        pg.display.update()

    pg.quit()

# MAIN HERE ************************************************************************************************

if __name__ == '__main__':

    pg.init()
    clock = pg.time.Clock()

    screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)
    screen.fill((150, 150, 150))
    pg.display.set_caption("Tower Def")

    # determine screen resolution
    my_resolution = screen.get_size()
    center_screen = screen.get_rect().center
    print("Native resolution: ", my_resolution)

    # loading screen
    fill_image = pg.image.load(os.path.join(os.path.dirname(__file__), 'data/textures', 'loading_screen.png')).convert()
    fill_image_rect = fill_image.get_rect(center = center_screen)
    screen.blit(fill_image, fill_image_rect)
    pg.display.flip()

    GameLoop()

    print('exiting...')
