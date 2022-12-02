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




spikes = []


class Spike:
    def __init__(self, screen, x, y, color):
        self.x = x
        self.y = y
        self.screen = screen
        self.color = color

    def draw(self):
        pg.draw.rect(self.screen, self.color, (self.x, self.y, 25, 25))


spikes.append(Spike(screen, 210, 190, CYAN))  # шип на левой верхней платформе
spikes.append(Spike(screen, 210 + 25, 190, CYAN))  # шип на левой верхней платформе
spikes.append(Spike(screen, 210 + 50, 190, CYAN))  # шип на левой верхней платформе

spikes.append(Spike(screen, 600, 190, CYAN))  # шип на правой верхней платформе
spikes.append(Spike(screen, 600 + 25, 190, CYAN))  # шип на правой верхней платформе

spikes.append(Spike(screen, 369 - 25, height - 95, CYAN))  # шип внизу
spikes.append(Spike(screen, 494 + 25, height - 95, CYAN))  # шип внизу

for i in range(3):
        spikes.append(Spike(screen, width//2 - 100 + 50 + 25*i, height//2, CYAN))  # шип в центре

for i in range(5):
    spikes.append(Spike(screen, 30, height//1.7 + 43+ 25*i, CYAN))  # шип слева внизу

for i in range(6):
    spikes.append(Spike(screen, width - 30 - 25, height//2.5 - 70 - 25*i, CYAN))  # шип справа сверху

for i in range(5):
    spikes.append(Spike(screen, width - 30 - 25, height//1.7 + 43+ 25*i, CYAN))  # шип справа внизу

for i in range(3):
    spikes.append(Spike(screen, 30, height // 2.5 - 65 - 25 * i, CYAN))  # шип слева сверху
# добавить еще шипов, чтобы жизнь медом не казалась ;)


with open('level.json', 'r') as file:
    data = json.load(file)
    N = len(data[0]['platform'])
    for i in range(N):
        platform = Platform(screen, **data[0]['platform'][i])
        platforms.append(platform)

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
        pass
        #FIXME: когда уровень пройден нужно открыть дверь
    # with open('level.json', 'r') as file:
    #     data = json.load(file)
    #     print(data)
    pg.display.update()

pg.quit()
#a = []
# for el in platforms:
#      a.append({'x':el.x1,'y':el.y1,'xx':el.x2,'yy':el.y2})
# with open('level.json', 'w') as file:
#     json.dump(a, file, indent=2)
# print(a)
with open('level.json', 'r') as file:
    data = json.load(file)
    print(data)
    print(data[0])
    print(data[0]['platform'])
    print(data[0]['platform'][0])