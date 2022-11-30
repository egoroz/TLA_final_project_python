import models.menu as menu
import pygame as pg

fps = 60
fpsClock = pg.time.Clock()
pg.init()

while True:
    menu.theme()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()

    for object in menu.objects:
        object.process()

    pg.display.flip()
    fpsClock.tick(fps)