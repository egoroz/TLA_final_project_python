import models.menu as menu
import models.level as level
import sys
import pygame as pg
import models.player as player

width, height = 1920//2, 1080//2
sys_width, sys_height = pg.display.Info().current_w, pg.display.Info().current_h
scales = (sys_width/width, sys_height/height)
screen = pg.display.set_mode((sys_width, sys_height))

WHITE = (200, 200, 200)

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

finished = False

class Game:
    '''Конструктор класса Game
    Args:
    screen - экран
    platforms - список платформ
    spikes - список шипов
    '''
    def __init__(self, screen, platforms, spikes):
        self.screen = screen
        self.platforms = platforms
        self.spikes = spikes

    def start_game(self):
        '''Запуск игры'''
        finished = False
        while not finished:
            self.screen.fill(WHITE)
            menu.pause_button(screen, scales, menu.exit_game)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    finished = True

            for platform in self.platforms:
                platform.draw()
            for spike in self.spikes:
                spike.draw()
                
            if level.check_passage():
                #FIXME: когда уровень пройден нужно открыть дверь
                for el in self.platforms:
                    el.move()
                for el in self.spikes:
                    el.move()
            pg.display.update()

game = Game(screen, platforms, spikes)

while not finished:
    theme.init_theme(screen)
    menu.start_buttons(screen, scales, game.start_game, menu.exit_game, menu.resume_game)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            finished = True
    pg.display.update()
    fpsClock.tick(fps)


pg.quit()