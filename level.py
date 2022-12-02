import pygame as pg
import json

pg.init()
width, height = 1920//2, 1080//2
screen = pg.display.set_mode((width, height))

platforms = []
WHITE = (200, 200, 200)
CYAN = (0, 150, 150)
BLACK = (0, 0, 0)
BROWN = (100, 50, 20)

class Platform:
    def __init__(self, screen, x, y, xx, yy):
        self.x = x
        self.y = y
        self.xx = xx
        self.yy = yy
        self.color = BLACK
        self.screen = screen

    def draw(self):
        pg.draw.rect(self.screen, self.color, (self.x, self.y, self.xx, self.yy))

    def move(self):
        self.x -= 0.1



spikes = []


class Spike:
    def __init__(self, screen, x, y, a, color=CYAN):
        self.x = x
        self.y = y
        self.a = 25
        self.screen = screen
        self.color = color

    def draw(self):
        pg.draw.rect(self.screen, self.color, (self.x, self.y, self.a, self.a))

    def move(self):
        self.x -= 0.1


with open('objects.json', 'r') as file:
    data = json.load(file)
    count_of_platforms = len(data[0]['platform'])
    for i in range(count_of_platforms):
        platform = Platform(screen, **data[0]['platform'][i])
        platforms.append(platform)
    count_of_spikes = len(data[1]['spike'])
    for i in range(count_of_spikes):
        spike = Spike(screen, **data[1]['spike'][i])
        spikes.append(spike)

def check_passage():
    #FIXME: Условие при котором уровень будет пройден return True
    return False


fps = 60
fpsClock = pg.time.Clock()

finished = False

while not finished:

    screen.fill(WHITE)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            finished = True

    for platform in platforms:
        platform.draw()
    for spike in spikes:
        spike.draw()

    if check_passage():
        #FIXME: когда уровень пройден нужно открыть дверь
        for el in platforms:
            el.move()
        for el in spikes:
            el.move()

    pg.display.update()

pg.quit()
