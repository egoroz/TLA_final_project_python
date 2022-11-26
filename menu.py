import pygame as pg
import thorpy as thorpy
from os import path

# Это пойдет потом в main, сделал для запуска
WIDTH = 1000
HEIGHT = 800
BLACK = (0, 0, 0)
font_name = pg.font.match_font('arial')
pg.init()
pg.font.init()
pg.display.set_caption("That level again")
screen = pg.display.set_mode((WIDTH, HEIGHT))
background = pg.image.load(path.join('background.png')).convert()
background_rect = background.get_rect()
pg.display.update()

def theme():
    '''Добавляет фон'''
    screen.fill(BLACK)
    screen.blit(background, background_rect)

def buttons(screen):
    button_new_game = thorpy.make_button("New game")
    button_resume_game = thorpy.make_button("Resume game")
    button_exit_game = thorpy.make_button("Exit game")
    box = thorpy.Box(elements=[
        button_new_game,
        button_resume_game,
        button_exit_game])

    menu = thorpy.Menu(box)
    for element in menu.get_population():
        element.surface = screen

    box.set_topleft((WIDTH//2 - 35, HEIGHT - 150))
    box.blit()
    box.update()
    return box

theme()
buttons(screen)
pg.display.update()

# Это тоже для пробного запуска
running = True
while running:
     for event in pg.event.get():    
        if event.type == pg.QUIT:
            running = False
