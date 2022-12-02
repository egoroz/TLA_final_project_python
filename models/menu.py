import sys
import pygame as pg
import os

BLACK = (0, 0, 0)

class Theme:

    def __init__(self, image_path = 'background.png'):
        self.background = pg.image.load(os.path.join(os.getcwd(), image_path)).convert()
        self.background_rect = self.background.get_rect()

    def init_theme(self, screen):
        screen.fill(BLACK)
        screen.blit(self.background, self.background_rect)

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
        self.font = pg.font.SysFont('Arial', 40)

        self.fillColors = {
            'normal': '#ffffff',
            'hover': '#666666',
            'pressed': '#333333',
        }

        self.buttonSurface = pg.Surface((self.width, self.height))
        self.buttonRect = pg.Rect(self.x, self.y, self.width, self.height)

        self.buttonSurf = self.font.render(buttonText, True, (20, 20, 20))

        self.alreadyPressed = False

        objects.append(self)

    def process(self, screen):
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

