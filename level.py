import models.menu as menu
import sys
import pygame as pg

pg.init()
width, height = 900, 600
screen = pg.display.set_mode((width, height))

platforms = []
WHITE = (200, 200, 200)
CYAN = (0, 150, 150)
BLACK = (0, 0, 0)
BROWN = (100, 50, 20)

class Platform:
    def __init__(self, screen, x1, y1, x2, y2, color):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.color = color
        self.screen = screen

    def draw(self):
        pg.draw.rect(self.screen, self.color, (self.x1, self.y1, self.x2, self.y2))


platforms.append(Platform(screen, 0, 0, width, 30, BLACK))  # верхняя граница
platforms.append(Platform(screen, 0, 0, 30, height//2.5, BLACK))  # левая верхняя граница
platforms.append(Platform(screen, 0, height//1.7, 30, height, BLACK))  # левая нижняя граница
platforms.append(Platform(screen, width-30, 0, width, height//2.5, BLACK))  # правая верхняя граница
platforms.append(Platform(screen, width-30, height//1.7, width, height, BLACK))  # правая нижняя граница
platforms.append(Platform(screen, 0, height-70, width, height, BLACK))  # нижняя граница
platforms.append(Platform(screen, 30, height//2.5 - 30, width // 9, 30, BLACK))  # коридор слева верх
platforms.append(Platform(screen, 30, height//1.7, width // 9, 30, BLACK))  # коридор слева низ
platforms.append(Platform(screen, width-30 - width // 9, height//2.5 - 30, width // 9, 30, BLACK))  # коридор справа верх
platforms.append(Platform(screen, width-30 - width // 9, height//1.7, width // 9, 30, BLACK))  # коридор справа низ
platforms.append(Platform(screen, width//2 - 100, height//2 - 30, 200, 30, BLACK))  # центральная платформа
platforms.append(Platform(screen, 180, 160, 150, 30, BLACK))  # левая верхняя платформа
platforms.append(Platform(screen, 550, 160, 150, 30, BLACK))  # правая верхняя платформа
platforms.append(Platform(screen, 180, 390, 150, 30, BLACK))  # левая нижняя платформа
platforms.append(Platform(screen, 550, 390, 150, 30, BLACK))  # правая нижняя платформа
platforms.append(Platform(screen, 369, 30, 150, 70, BLACK))  # самая верхняя платформа
platforms.append(Platform(screen, 369, height - 120, 150, 50, BLACK))  # самая нижняя платформа


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
    pg.display.update()

pg.quit()
