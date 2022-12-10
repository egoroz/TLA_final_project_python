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

def read_data(screen, platforms, spikes, input_file):
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

class PushableButton:
    def __init__(self, screen, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.rect = (x, y, w, h)
        self.color = (255, 0, 0)
        self.screen = screen

    def update(self, obj):
        if pg.Rect.colliderect((obj.x, obj.y, obj.w, obj.h), self.rect):
            self.y = obj.y + obj.h
    def draw(self):
        pg.draw.rect(self.screen, self.color, self.rect)

class Door:
    def __init__(self, screen, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.rect = (x, y, w, h)
        self.color = (0, 0, 0)

    def update(self, obj):
        self.y = obj.y + obj.h
    def draw(self):
        pg.draw.rect(self.screen, self.color, self.rect)


def check_passage(player, objects):
    '''Проверяет прохождение уровня'''
        # if
    return False

