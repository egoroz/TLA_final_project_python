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
game = level.Game(screen, platforms, spikes, menu.pause_button(screen, scales, menu.exit_game))

while True:
    theme.init_theme(screen)
    menu.start_buttons(screen, scales, game.init_game, menu.exit_game, menu.resume_game)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
    
    pg.display.update()
    fpsClock.tick(fps)