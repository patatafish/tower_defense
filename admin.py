import pygame as pg

class AdminMenu(pg.sprite.Sprite):

    def __init__(self):
        super(AdminMenu, self).__init__()
        admin_window_size = (800, 600)
        self.admin_window = pg.Surface(admin_window_size)
        self.admin_window_rect = self.admin_window.get_rect()

        self.admin_window.fill((0, 0, 0))
        self.admin_window_rect.move(100, 100)
