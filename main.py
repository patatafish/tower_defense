# import modules
# import time
# import random
import os
import pygame as pg
import pygame.display

import admin


if not pg.font:
    print('Warning, fonts disabled!')
if not pg.mixer:
    print('Warning, sounds disabled!')


# GLOBAL LOADS AND FUNCTIONS HERE ********************************************************************************

ADMIN = True
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (150, 150, 150)


# GAME ObJECT CLASSES HERE *********************************************************************************
class Menu:

    def __init__(self):
        self.menu_show = False
        self.menu_x = 800
        self.menu_y = 1600
        self.menu_background = pg.Surface((self.menu_x, self.menu_y))
        self.menu_background.fill((0, 0, 0))
        self.menu_background_rect = self.menu_background.get_rect(center=screen.get_rect().center)

    def show(self):
        self.render_menu()
        # loop to catch menu input. We loop here because it pauses the game loop,
        # which pauses all update actions behind menu (pauses game on menu load)
        while self.menu_show:
            for event in pg.event.get():
                if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                    # we need to check the position of the mouse relative to the menu, not
                    # to the whole screen, so we do some maths to get the relative position.
                    pos = pg.mouse.get_pos()
                    pos = (pos[0] - self.menu_background_rect.left, pos[1] - self.menu_background_rect.top)
                    if self.button_quit_rect.collidepoint(pos):
                        self.menu_show = False
                        return False
                elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                    self.menu_show = False

        # closed the menu without exiting game, return true to App loop
        return True

    def render_menu(self):
        # set menu show flag to true for menu input loop.
        self.menu_show = True
        # render he buttons on the menu
        self.button_new = pg.Surface((750, 200))
        self.button_new.fill(GREY)
        self.button_new_rect = self.button_new.get_rect().move(25, 25)
        self.button_new_text = pg.font.Font(None, 72)
        self.button_new_text_surf = self.button_new_text.render("New Game", True, BLACK, GREY)
        self.button_new_text_image = pg.Surface(self.button_new_text_surf.get_size())
        self.button_new_text_image.blit(self.button_new_text_surf, (0, 0))
        self.button_new.blit(self.button_new_text_image, (225, 50))

        self.button_save = pg.Surface((750, 200))
        self.button_save.fill(GREY)
        self.button_save_rect = self.button_save.get_rect().move(25, 250)
        self.button_save_text = pg.font.Font(None, 72)
        self.button_save_text_surf = self.button_save_text.render("Save Game", True, BLACK, GREY)
        self.button_save_text_image = pg.Surface(self.button_save_text_surf.get_size())
        self.button_save_text_image.blit(self.button_save_text_surf, (0, 0))
        self.button_save.blit(self.button_save_text_image, (225, 50))

        self.button_load = pg.Surface((750, 200))
        self.button_load.fill(GREY)
        self.button_load_rect = self.button_load.get_rect().move(25, 475)
        self.button_load_text = pg.font.Font(None, 72)
        self.button_load_text_surf = self.button_load_text.render("Load Game", True, BLACK, GREY)
        self.button_load_text_image = pg.Surface(self.button_load_text_surf.get_size())
        self.button_load_text_image.blit(self.button_load_text_surf, (0, 0))
        self.button_load.blit(self.button_load_text_image, (225, 50))

        self.button_quit = pg.Surface((750, 200))
        self.button_quit.fill(GREY)
        self.button_quit_rect = self.button_quit.get_rect().move(25, 700)
        self.button_quit_text = pg.font.Font(None, 72)
        self.button_quit_text_surf = self.button_quit_text.render("Quit Game", True, BLACK, GREY)
        self.button_quit_text_image = pg.Surface(self.button_quit_text_surf.get_size())
        self.button_quit_text_image.blit(self.button_quit_text_surf, (0, 0))
        self.button_quit.blit(self.button_quit_text_image, (225, 50))

        if ADMIN:
            self.button_debug = pg.Surface((750, 200))
            self.button_debug.fill(GREY)
            self.button_debug_rect = self.button_debug.get_rect().move(25, 925)
            self.button_debug_text = pg.font.Font(None, 72)
            self.button_debug_text_surf = self.button_debug_text.render("DEBUG MENU", True, BLACK, GREY)
            self.button_debug_text_image = pg.Surface(self.button_debug_text_surf.get_size())
            self.button_debug_text_image.blit(self.button_debug_text_surf, (0, 0))
            self.button_debug.blit(self.button_debug_text_image, (225, 50))

        # BLIT the menu items, blit buttons on BG, then blit BG to screen
        self.menu_background.blit(self.button_new, self.button_new_rect)
        self.menu_background.blit(self.button_save, self.button_save_rect)
        self.menu_background.blit(self.button_load, self.button_load_rect)
        self.menu_background.blit(self.button_quit, self.button_quit_rect)
        self.menu_background.blit(self.button_debug, self.button_debug_rect)
        screen.blit(self.menu_background, self.menu_background_rect)

        # we update display here because the app loop is paused
        pg.display.update()


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


class Canvas(pg.sprite.Sprite):

    def __init__(self, level=None):
        super(Canvas, self).__init__()
        self.canvas = pg.Surface(screen.get_size())
        self.canvas_rect = self.canvas.get_rect()
        self.canvas.fill(GREY)

    def update(self):
        screen.blit(self.canvas, self.canvas_rect)


# GAME LOOP HERE *******************************************************************************************


def app():

    # set flag for app loop
    running = True
    # init menu item
    game_menu = Menu()
    # init sprites
    pointer = Pointer()
    canvas = Canvas()
    # add constant sprite to render group
    render_group = pg.sprite.Group()
    render_group.add(canvas)
    render_group.add(pointer)

    while running:
        clock.tick(60)
        for event in pg.event.get():
            # if esc key pressed show menu. This will pause the app loop
            # as well as any render groups
            if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                running = game_menu.show()


        # update render groups and redraw window
        render_group.update()
        pg.display.update()

    # if we escape running loop, clean pygame objects and exit
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
    print("Native resolution: ", my_resolution)

    # loading screen
    fill_image = pg.image.load(os.path.join(os.path.dirname(__file__), 'data/textures', 'loading_screen.png')).convert()
    fill_image_rect = fill_image.get_rect(center=screen.get_rect().center)
    screen.blit(fill_image, fill_image_rect)
    pg.display.flip()

    # call app
    app()

    print('exiting...')
