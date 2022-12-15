import models.menu as menu
import models.level as level
import sys
import pygame as pg
import models.player as player

width, height = 1920//2, 1080//2
sys_width, sys_height = pg.display.Info().current_w, pg.display.Info().current_h
scales = (sys_width/width, sys_height/height)
screen = pg.display.set_mode((sys_width, sys_height))
pg.mixer.music.load("Soundtrack.wav")
pg.mixer.music.play(-1)

WHITE = (200, 200, 200)

platforms = []
spikes = []
buttons = []
doors = []
old_platforms = []
old_spikes = []
old_buttons = []
old_doors = []
levels = 0
slide = False
need_slide = 0
count_wind = -1  # номер картинки ветра
tick = 0  # раз в сколько-то тиков меняется картинка ветра
collisable_obj = []
player_position = (0, 0, 0)

level.read_data(screen, platforms, spikes, buttons, doors, 'docs/objects.json')
collisable_obj = platforms.copy()
collisable_obj.append(doors[0])
level.scale_objects(platforms, scales)
level.scale_objects(spikes, scales)
level.scale_objects(buttons, scales)
level.scale_objects(doors, scales)

title_dict = {
    0:"0.Нулёвка по общесосу",
    1:"1.Повторение - мать учения",
    2:"2.Илон Маск",
    3:"3.Возьми подсказку",
    4:"4.Just chill",
    5:"5.Dota-2",
    6:"6.Предел жизней кота",
    7:"7.Сникерсни - притормози"
    }

hint_dict = {
    0:"Серьезно?!",
    1:"Просто сильнее",
    2:"SPACE-X",
    3:"ВОЗЬМИ ЁЁ!!!",
    4:"Руки прочь",
    5:"Бедная мышка",
    6:"Нет, тут без Тейлора",
    7:"Может, проверить ту кнопочку?"
    }

hero = player.Player(0, 440, screen)
fps = 60
fpsClock = pg.time.Clock()
pg.init()

theme = menu.Theme("pic/background.png", sys_width, sys_height)

finished = False
left = False
right = False
up = False
down = False
space = False

class Game:
    '''Конструктор класса Game
    Args:
    screen - экран
    platforms - список платформ
    spikes - список шипов
    '''
    def __init__(self, screen, up, down, right, left, space):
        self.screen = screen
        self.up = up
        self.down = down
        self.right = right
        self.left = left
        self.space = space

    def start_game(self):
        '''Запуск игры'''
        global levels, old_platforms, old_spikes, old_buttons, old_doors, need_slide, slide, count_wind, tick, player_position
        finished = False
        while not finished:
            self.screen.fill(WHITE)
            for button in buttons:
                button.draw()
                button.update(hero)
            for platform in platforms:
                platform.draw()
            for spike in spikes:
                spike.draw()
            for door in doors:
                door.draw()
                flag, player_position = level.check_passage(scales, hero, levels, buttons, self.space, player_position)
                door.update(flag)
            for button in old_buttons:
                button.draw()
                button.update(hero)
            for platform in old_platforms:
                platform.draw()
            for spike in old_spikes:
                spike.draw()
            for door in old_doors:
                door.draw()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    finished = True
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_UP:
                        self.up = True
                    if event.key == pg.K_LEFT:
                        self.left = True
                    if event.key == pg.K_RIGHT:
                        self.right = True
                    if event.key == pg.K_SPACE:
                        self.space = True
                elif event.type == pg.KEYUP:
                    if event.key == pg.K_UP:
                        self.up = False
                    if event.key == pg.K_LEFT:
                        self.left = False
                    if event.key == pg.K_RIGHT:
                        self.right = False
                    if event.key == pg.K_SPACE:
                        self.space = False           
            menu.pause_game.has_been_called = False
            menu.ask_hint.has_been_called = False
            menu.game_buttons(screen, scales, menu.pause_game, menu.ask_hint)
            menu.title(screen, scales, title_dict, levels)
            if menu.pause_game.has_been_called:
                break
            if menu.ask_hint.has_been_called == True:
                menu.hint(screen, scales, hint_dict, levels)
            collisable_obj = platforms.copy()
            collisable_obj.append(doors[0])
            hero.update(self.left, self.right, self.up, self.down, self.screen, collisable_obj, spikes)

            levels, old_platforms, old_spikes, old_buttons, old_doors, slide, need_slide = level.update_level(screen, need_slide, width, levels, hero, scales, platforms, spikes, buttons, doors, old_platforms, old_spikes, old_buttons, old_doors, slide)
            need_slide, count_wind, tick = level.level_slide(screen, slide, need_slide, width, height, scales, platforms, spikes, buttons, doors, old_platforms, old_spikes, old_buttons, old_doors, hero, count_wind, tick)
            pg.display.update()
            fpsClock.tick(fps)

game = Game(screen, up, down, right, left, space)

while not finished:
    screen.fill(WHITE)
    theme.init_theme(screen)
    menu.start_buttons(screen, scales, game.start_game, pg.quit)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            finished = True
    pg.display.update()
    fpsClock.tick(fps)

pg.quit()