import models.menu as menu
import models.level as level
import sys
import pygame as pg
import models.player as player

width, height = 1920//2, 1080//2
sys_width, sys_height = pg.display.Info().current_w, pg.display.Info().current_h
scales = (sys_width/width, sys_height/height)
screen = pg.display.set_mode((sys_width, sys_height))

platforms = []
spikes = []

level.read_data(screen, platforms, spikes, 'objects.json')
level.scale_objects(platforms, scales)
level.scale_objects(spikes, scales)

hero = player.Player(100,100,screen)
fps = 60
fpsClock = pg.time.Clock()
pg.init()
hero.draw(screen)

theme = menu.Theme('background.png', sys_width, sys_height)
game = level.Game(screen, platforms, spikes)
New_game_button = menu.Button(280, 320, 380, 60, scales, game.init_game, 'New Game')
Exit_game_button = menu.Button(280, 390, 380, 60, scales, menu.exit_game, 'Exit game')
Resume_game_button = menu.Button(280, 460, 380, 60, scales, menu.resume_game, 'Resume game')

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