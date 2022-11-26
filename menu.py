import pygame as pg
import thorpy as thorpy

WIDTH = 1000
HEIGHT = 800
font_name = pg.font.match_font('arial')
pg.init()
pg.font.init()
pg.display.set_caption("That level again")
screen = pg.display.set_mode((WIDTH, HEIGHT))

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

    box.set_topleft((WIDTH//2 - 35, HEIGHT//2 - 225))
    box.blit()
    box.update()
    return box

buttons(screen)

running = True
while running:
     for event in pg.event.get():    
        if event.type == pg.QUIT:
            running = False
