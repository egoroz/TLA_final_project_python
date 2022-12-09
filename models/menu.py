import sys
import pygame as pg
import os

BLACK = (0, 0, 0)

class Theme:
    '''Конструктор класса Theme
    Args:
    image_path - фоновая картинка
    sys_width - ширина экрана пользователя
    sys_height - высота экрана пользователя
    '''

    def __init__(self, image_path, sys_width, sys_height):
        self.background = pg.image.load(os.path.join(os.getcwd(), image_path)).convert()
        self.background = pg.transform.scale(self.background, (sys_width, sys_height))
        self.background_rect = self.background.get_rect()

    def init_theme(self, screen):
        '''Отрисовывает фон'''

        screen.fill(BLACK)
        screen.blit(self.background, self.background_rect)

class Button:
    '''Конструктор класса Button
    Args: 
    x - положение кнопки по х
    y - положение кнопки по у
    width - ширина кнопки
    height - высота кнопки
    buttonText - текст на кнопке
    onclickFunction - функция кнопки
    '''

    def __init__(self, x, y, width, height, scales, onclickFunction, buttonText='Button'):
        scale_x, scale_y = scales
        
        self.x = x*scale_x
        self.y = y*scale_y
        self.width = width*scale_x
        self.height = height*scale_y
        self.onclickFunction = onclickFunction
        self.font = pg.font.SysFont('Monotype Corsiva', 40)

        self.fillColors = {
            'normal': '#FFE4B5',
            'hover': '#778899',
            'pressed': '#333333',
        }

        self.buttonSurface = pg.Surface((self.width, self.height))
        self.buttonRect = pg.Rect(self.x, self.y, self.width, self.height)

        self.buttonSurf = self.font.render(buttonText, True, (20, 20, 20))

        self.alreadyPressed = False

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

def pause_game():
    '''Функция паузы игры'''
    pause_game.has_been_called = True
    pass

def hint():
    '''Функция подсказки к прохождению уровня'''
    pass  # FIXME

def start_buttons(screen, scales, func_1, func_2):
    '''Отображает кнопки стартового меню
    Args:
    screen - экран отрисовки
    scales - масштабирование
    func_1 - первая функция
    func_2 - вторая функция
    '''
    New_game_button = Button(280, 390, 380, 60, scales, func_1, 'Play game')
    Exit_game_button = Button(280, 460, 380, 60, scales, func_2, 'Exit game')    

    objects = [New_game_button, Exit_game_button]
    for object in objects:
        object.process(screen)

def game_buttons(screen, scales, func_1, func_2):
    '''Отображает кнопки игрового экрана
    Args:
    screen - экран отрсовки
    scales - масштабирование
    func_1 - первая функция
    func_2 - вторая функция
    '''
    Pause_button = Button(30, 30, 50, 30, scales, func_1, "Pause")
    Hint_button = Button(90, 30, 50, 30, scales, func_2, "Hint")

    objects = [Pause_button, Hint_button]
    for object in objects:
        object.process(screen)
    

