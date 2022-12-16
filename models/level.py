import pygame as pg
import json

pg.init()

WHITE = (200, 200, 200)
CYAN = (0, 150, 150)
BLACK = (0, 0, 0)
BROWN = (100, 50, 20)


def scale_objects(objects, scales):
    '''Скейлит объекты под разрешение экрана пользователя
    Args:
    objects - список объектов для скейла
    scales - масштабирование
    '''
    scale_x, scale_y = scales

    for object in objects:
        object.x *= scale_x
        object.w *= scale_x
        object.y *= scale_y
        object.h *= scale_y


class Platform:
    '''Конструктор класса Platform
    Args:
    screen - экран
    x - координата по иксу
    y - координата по игреку
    w - ширина
    h - высота
    '''
    def __init__(self, screen, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = BLACK
        self.screen = screen
    
    def make_rect(self):
        '''Делает прямоугольник для платформы'''
        return pg.Rect(self.x, self.y, self.w, self.h)
    
    def draw(self):
        '''Рисует платформы на уровне'''
        pg.draw.rect(self.screen, self.color, (self.x, self.y, self.w, self.h))

    def move(self):
        '''Движение платформ при прохождении'''
        self.x -= 0.1


class Spike:
    '''Конструктор класса Spike
    Args:
    screen - экран
    x - положение по иксу
    y - положение по игреку
    color - цвет
    '''
    def __init__(self, screen, x, y, a, color=CYAN):
        self.x = x
        self.y = y
        self.w = a
        self.h = a
        # self.image = pg.transform.scale(pg.image.load("pic\spike.png"), (25, 25))
        self.screen = screen
        self.color = color

    def draw(self):
        '''Рисует шипы на уровне'''
        pg.draw.rect(self.screen, self.color, (self.x, self.y, self.w, self.h))
        # self.screen.blit(self.image, (self.x, self.y))

    def move(self):
        '''Движение шипов при прохождении'''
        self.x -= 0.1

    def make_rect(self):
        '''Делает прямоугольник для шипа'''
        return pg.Rect(self.x, self.y, self.w, self.h)


def read_data(screen, platforms, spikes, buttons, doors, input_file):
    '''Считывает данные о расположении платформ и шипов с файла input_file
    Args:
    screen - экран
    platforms - список платформ, куда идет запись
    spikes - список шипов, куда идет запись
    buttons - список кнопок
    doors - список дверей
    input_file - файл считывания
    '''
    with open(input_file, 'r') as file:
        data = json.load(file)
        count_of_platforms = len(data[0]['platform'])
        for i in range(count_of_platforms):
            platform = Platform(screen, **data[0]['platform'][i])
            platforms.append(platform)

        count_of_spikes = len(data[1]['spike'])
        for i in range(count_of_spikes):
            spike = Spike(screen, **data[1]['spike'][i])
            spikes.append(spike)

        count_of_buttons = len(data[2]['button'])
        for i in range(count_of_buttons):
            button = PushableButton(screen, **data[2]['button'][i])
            buttons.append(button)

        count_of_doors = len(data[3]['door'])
        for i in range(count_of_doors):
            door = Door(screen, **data[3]['door'][i])
            doors.append(door)


class PushableButton:
    '''Конструктор класса PushableButton
    Args:
    screen - экран
    x - положение по иксу
    y - положение по игреку
    w - ширина
    h - высота
    '''
    def __init__(self, screen, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.rect = pg.Rect(self.x, self.y, self.w, self.h)
        self.color = (255, 0, 0)
        self.screen = screen
        self.c = 0  # на сколько пикселей опустилось вниз
        self.push = False

    def update(self, obj):
        '''Обновляет объект obj'''
        if pg.Rect.colliderect(pg.Rect(obj.x, obj.y, obj.w, obj.h), self.rect):
            self.y += 1
            self.c += 1
            self.push = True
        else:
            if self.c:
                self.y -= 1
                self.c -= 1
            self.push = False
        self.rect = pg.Rect(self.x, self.y, self.w, self.h)

    def draw(self):
        '''Отрисовка'''
        pg.draw.rect(self.screen, self.color, (self.x, self.y, self.w, self.h))


class Door:
    '''Конструктор класса Door
    Args:
    screen - экран
    x - положение по иксу
    y - положение по игреку
    w - ширина
    h - высота
    '''
    def __init__(self, screen, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.rect = (self.x, self.y, self.w, self.h)
        self.color = (0, 0, 0)
        self.screen = screen
        self.opened = False
        self.c = 0  # на сколько пикселей поднялась дверь

    def update(self, func, scale):
        '''Обновляет положение двери если выполнена функция func'''
        if func:
            self.opened = True

        if self.opened and self.c < 120*scale:
            self.y -= 1
            self.c += 1

    def make_rect(self):
        return pg.Rect(self.x, self.y, self.w, self.h)

    def draw(self):
        pg.draw.rect(self.screen, self.color, (self.x, self.y, self.w, self.h))
        self.rect = (self.x, self.y, self.w, self.h)


def check_passage(scales, player, levels, buttons, space, player_position, doors, knock_count, mouse, count_mouse,
                  last_mouse, secret, platforms, spikes, old_platforms, old_spikes, old_buttons, old_doors,
                  flag_11):
    '''
    Agrs:
    scales - скейлинг
    player - игрок
    levels - номер уровня, для которого проводится проверка
    buttons - кнопки
    space - пробел
    player_position - позиция игрока
    '''
    scale_x, scale_y = scales
    player_x_last, player_y_last, count_one_position = player_position
    flag = False

    if levels == 0:
        for button in buttons:
            if button.push:
                flag = True

    if levels == 1:
        for button in buttons:
            if button.push and player.vy > 1:
                flag = True

    if levels == 2:
        if space:
            flag = True

    if levels == 3:
        #  90, 30, 50, 30 положения кнопки хинт: верхний левый угол, ширина, высота
        if 90 * scale_x < player.x < (90+50) * scale_x  and 30 * scale_y < player.y < (30 + 30) * scale_y:
            flag = True

    if levels == 4:
        if player.x == player_x_last and player.y == player_y_last:
            count_one_position += 1
            if count_one_position > 600:
                flag = True
        else:
            count_one_position = 0
            player_x_last = player.x
            player_y_last = player.y
        knock_count = 0

    if levels == 5:
        for door in doors:
            if pg.Rect.colliderect(pg.Rect(player.x, player.y, player.w, player.h), pg.Rect(door.rect)):
                knock_count += 1
                if knock_count == 5:
                    flag = True
        count_mouse = 0

    if levels == 6:
        if mouse and not(last_mouse):
            count_mouse += 1
            if count_mouse > 15:
                flag = True
        last_mouse = mouse
        player.death = 0

    if levels == 7:
        if player.death >= 9:
            flag = True
    if levels == 8:
        # 30, 30, 50, 30 координаты кнопки пауза
        x, y = pg.mouse.get_pos()
        if (30 * scale_x < x < (30+50) * scale_x) and (30 * scale_y < y < (30 + 30) * scale_y) and mouse:
            flag = True
    if levels == 10:
        if secret:
            flag = True
    if levels == 11:
        if flag_11:
            del platforms[:]
            del doors[:]
            del spikes[:]
            del buttons[:]
            del old_platforms[:]
            del old_doors[:]
            del old_spikes[:]
            del old_buttons[:]
    return flag, (player_x_last, player_y_last, count_one_position), knock_count, count_mouse, last_mouse


def update_level(screen, need_slide, width, levels, player, scales, platforms, spikes,
                 buttons, doors, old_platforms, old_spikes, old_buttons, old_doors, slide):
    '''Обновление уровня
    Args:
    screen - экран
    slide - флаг скольжения
    need_slide - остаток скольжения
    width - ширина
    height - высота
    scales - скейлинг
    platforms - список платформ
    spikes - список шипов
    buttons - список
    doors - дверь
    old_platforms - платформы, которые исчезнут при слайде
    old_spikes - шипы, которые исчезнут при слайде
    old_buttons - кнопки, которые исчезнут при слайде
    old_doors - дверь
    player - игрок
    count_wind - счетчик изображения ветра
    tick - счетчик обновления главного цикла
    '''
    scale_x, scale_y = scales
    if need_slide <= 0:
        slide = False
        player.ax = 0.5
        player.ay = 1
        player.jump = -10
    if player.x > (1920//2)*scale_x and 250*scale_y < player.y < 300*scale_y:
        pg.draw.rect(screen, BROWN, ((1920//2)*scale_x, 250*scale_y, 100*scale_x, 50*scale_y))
        if len(platforms) > 0 and not(slide):
            old_platforms = list(platforms)
            old_spikes = list(spikes)
            old_buttons = list(buttons)
            old_doors = list(doors)
            del platforms[:]
            del doors[:]
            del spikes[:]
            del buttons[:]
            read_data(screen, platforms, spikes, buttons, doors, 'docs/objects.json')
            scale_objects(platforms, scales)
            scale_objects(spikes, scales)
            scale_objects(buttons, scales)
            scale_objects(doors, scales)
            for spike in spikes:
                spike.w += 2
                spike.h += 2

            for platform in platforms:
                platform.w += 1
                platform.h += 1
            for pl in platforms:
                pl.x += width*scale_x
            for sp in spikes:
                sp.x += width*scale_x
            for bt in buttons:
                bt.x += width*scale_x
            for dr in doors:
                dr.x += width*scale_x
            levels += 1
            slide = True
            need_slide = width*scale_x
    return levels, old_platforms, old_spikes, old_buttons, old_doors, slide, need_slide


def level_slide(screen, slide, need_slide, width, height, scales, platforms, spikes, buttons,
                doors, old_platforms, old_spikes, old_buttons, old_doors, player, count_wind, tick):
    '''Скольжение уровня
    Args:
    screen - экран
    slide - флаг скольжения
    need_slide - остаток скольжения
    width - ширина
    height - высота
    scales - скейлинг
    platforms - список платформ
    spikes - список шипов
    buttons - список
    doors - дверь
    old_platforms - платформы, которые исчезнут при слайде
    old_spikes - шипы, которые исчезнут при слайде
    old_buttons - кнопки, которые исчезнут при слайде
    old_doors - дверь
    player - игрок
    count_wind - счетчик изображения ветра
    tick - счетчик обновления главного цикла
    '''
    if slide:
        if need_slide > 0:
            scale_x, scale_y = scales
            need_slide -= width*scale_x/50
            d = width*scale_x/50
            for pl in platforms:
                pl.x -= d
            for sp in spikes:
                sp.x -= d
            for bt in buttons:
                bt.x -= d
            for dr in doors:
                dr.x -= d

            for pl in old_platforms:
                pl.x -= d
            for sp in old_spikes:
                sp.x -= d
            for bt in old_buttons:
                bt.x -= d
            for dr in old_doors:
                dr.x -= d
            player.x -= d
            player.vx = 0
            player.vy = 0
            player.ax = 0
            player.ay = 0
            player.jump = 0
            if tick % 7 == 0:
                count_wind = (count_wind + 1) % 7
            image = pg.transform.scale(pg.image.load(f"pic\_{count_wind}.png"), (width * scale_x, height*scale_y))
            screen.blit(image, (0, 0))
            tick += 1
            if len(platforms) > 0:
                if platforms[0].x < 0:
                    d = -0.1
                    while platforms[0].x < 0:
                        for pl in platforms:
                            pl.x -= d
                        for sp in spikes:
                            sp.x -= d
                        for bt in buttons:
                            bt.x -= d
                        for dr in doors:
                            dr.x -= d

                        for pl in old_platforms:
                            pl.x -= d
                        for sp in old_spikes:
                            sp.x -= d
                        for bt in old_buttons:
                            bt.x -= d
                        for dr in old_doors:
                            dr.x -= d
    return need_slide, count_wind, tick
