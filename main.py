#import models.menu as menu
import sys
import pygame as pg
import player
width, height = 640, 480
screen = pg.display.set_mode((width, height))
hero=player.Player(100,100,screen)
fps = 60
fpsClock = pg.time.Clock()
pg.init()
hero.draw(screen)
while True:
    #menu.theme()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()

    #for object in menu.objects:
     #   object.process()

    pg.display.flip()
    fpsClock.tick(fps)