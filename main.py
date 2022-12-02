import models.menu as menu
import models.level as level
import sys
import pygame as pg
import player
width, height = 900, 600
screen = pg.display.set_mode((width, height))
hero=player.Player(100,100,screen)
fps = 60
fpsClock = pg.time.Clock()
pg.init()
hero.draw(screen)

theme = menu.Theme()
New_game_button = menu.Button(120, 70, 400, 100, 'New Game', level.start_game)
Exit_game_button = menu.Button(120, 180, 400, 100, 'Exit game', menu.exit_game)
Resume_game_button = menu.Button(120, 290, 400, 100, 'Resume game', menu.resume_game)

objects = [New_game_button, Exit_game_button, Resume_game_button]

while True:
    theme.init_theme(screen)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
        

    for object in objects:
        object.process(screen)

    pg.display.flip()
    fpsClock.tick(fps)