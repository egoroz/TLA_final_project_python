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
    xx - ширина
    yy - высота
    '''
    def __init__(self, screen, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = BLACK
        self.screen = screen
    
    def make_rect(self):
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
    screen - 
    x -
    y -
    color -
    '''
    def __init__(self, screen, x, y, a, color=CYAN):
        self.x = x
        self.y = y
        self.w = 25
        self.h = 25
        self.screen = screen
        self.color = color

    def draw(self):
        '''Рисует шипы на уровне'''
        pg.draw.rect(self.screen, self.color, (self.x, self.y, self.w, self.h))

    def move(self):
        '''Движение шипов при прохождении'''
        self.x -= 0.1
    def make_rect(self):
        return pg.Rect(self.x, self.y, self.w, self.h)

def read_data(screen, platforms, spikes, buttons, doors, input_file):
    '''Считывает данные о расположении платформ и шипов с файла input_file
    Args:
    screen - экран
    platforms - список платформ, куда идет запись
    spikes - список шипов, куда идет запись
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
    def __init__(self, screen, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.rect = pg.Rect(self.x, self.y, self.w, self.h)
        self.color = (255, 0, 0)
        self.screen = screen
        self.c = 0  # на сколько пикселей опустилось вниз
    def update(self, obj):
        if pg.Rect.colliderect(pg.Rect(obj.x, obj.y, obj.w, obj.h), self.rect):
            self.y += 1
            self.c += 1
        else:
            if self.c:
                self.y -= 1
                self.c -= 1
        self.rect = pg.Rect(self.x, self.y, self.w, self.h)
    def draw(self):
        pg.draw.rect(self.screen, self.color, (self.x, self.y, self.w, self.h))

class Door:
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

    def update(self, func):
        if func:
            self.opened = True
        else:
            self.opened = False
        if self.opened and self.c < 200:
            self.y -= 1
            self.c += 1
        else:
            self.y += 1
            self.c -= 1

    def draw(self):
        pg.draw.rect(self.screen, self.color, (self.x, self.y, self.w, self.h))
        self.rect = (self.x, self.y, self.w, self.h)


def check_passage(player, objects):
    '''Проверяет прохождение уровня'''
        # if
    return False

#remove +3
