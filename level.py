import models.menu as menu
import sys
import pygame as pg

pg.init()
width, height = 900, 600
screen = pg.display.set_mode((width, height))

platforms = []
WHITE = (200, 200, 200)
GRAY = (150, 150, 150)
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


spikes = []


class Spike:
    def __init__(self, x, y, screen, color):
        self.x = x
        self.y = y
        self.screen = screen
        self.color = color

    def drow(self):
        pg.draw.rect(self.screen, self.color, (self.x, self.y, 15, 15))


#spikes.append(Spike())

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
    pg.display.update()
pg.quit()
