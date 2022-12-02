import models.menu as menu
import models.level as level
import sys
import pygame as pg
from os import path

width, height = 900, 600
screen = pg.display.set_mode((width, height))

fps = 60
fpsClock = pg.time.Clock()

background = pg.image.load(path.join('background.png')).convert()
background_rect = background.get_rect()

pg.display.update()
pg.init()

#level.add_platforms(screen, width, height)
#level.add_spikes(screen, width, height)

def new_game():
    print('New')

def exit_game():
    '''Выход из игры'''
    pg.quit()

def resume_game():
    '''Продолжить с предыдущего сохранения'''
    print('Resume')  # Аналогично ждет кода игры

New_game_button = menu.Button(120, 70, 400, 100, 'New Game', new_game)
Exit_game_button = menu.Button(120, 180, 400, 100, 'Exit game', exit_game)
Resume_game_button = menu.Button(120, 290, 400, 100, 'Resume game', resume_game)

while True:
    menu.start_menu()
    