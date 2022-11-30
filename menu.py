import sys
import pygame as pg
from os import path

pg.init()
fps = 60
fpsClock = pg.time.Clock()
width, height = 640, 480
screen = pg.display.set_mode((width, height))

background = pg.image.load(path.join('background.png')).convert()
background_rect = background.get_rect()
pg.display.update()

BLACK = (0, 0, 0)

def theme():
    '''Добавляет фон'''
    screen.fill(BLACK)
    screen.blit(background, background_rect)

font = pg.font.SysFont('Arial', 40)

objects = []

class Button():
    '''Конструктор класса Button
    Args: 
    x - положение кнопки по х
    y - положение кнопки по у
    width - ширина кнопки
    height - высота кнопки
    buttonText - текст на кнопке
    onclickFunction - функция кнопки
    '''
    def __init__(self, x, y, width, height, buttonText='Button', onclickFunction=None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.onclickFunction = onclickFunction

        self.fillColors = {
            'normal': '#ffffff',
            'hover': '#666666',
            'pressed': '#333333',
        }

        self.buttonSurface = pg.Surface((self.width, self.height))
        self.buttonRect = pg.Rect(self.x, self.y, self.width, self.height)

        self.buttonSurf = font.render(buttonText, True, (20, 20, 20))

        self.alreadyPressed = False

        objects.append(self)

    def process(self):
        '''Проверяет положение мыши, меняет цвет при наведении, при нажатии выпоняется функция кнопки'''
        mousePos = pg.mouse.get_pos()
        self.buttonSurface.fill(self.fillColors['normal'])
        if self.buttonRect.collidepoint(mousePos):
            self.buttonSurface.fill(self.fillColors['hover'])
            if pg.mouse.get_pressed(num_buttons=3)[0]:
                self.buttonSurface.fill(self.fillColors['pressed'])
                if not self.alreadyPressed:
                    self.onclickFunction()
                    self.alreadyPressed = True
            else:
                self.alreadyPressed = False
        self.buttonSurface.blit(self.buttonSurf, [
            self.buttonRect.width/2 - self.buttonSurf.get_rect().width/2,
            self.buttonRect.height/2 - self.buttonSurf.get_rect().height/2
        ])
        screen.blit(self.buttonSurface, self.buttonRect)

def new_game():
    '''Начинает новую игру'''
    print('New')  # Ожидает кода, пока так

def exit_game():
    '''Выход из игры'''
    pg.quit()

def resume_game():
    '''Продолжить с предыдущего сохранения'''
    print('Resume')  # Аналогично ждет кода игры

New_game_button = Button(30, 30, 400, 100, 'New Game', new_game)
Exit_game_button = Button(30, 140, 400, 100, 'Exit game', exit_game)
Resume_game_button = Button(30, 250, 400, 100, 'Resume game', resume_game)

while True:
    theme()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()

    for object in objects:
        object.process()

    pg.display.flip()
    fpsClock.tick(fps)