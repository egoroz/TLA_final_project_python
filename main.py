import models.menu as menu
import models.level as level
import sys
import pygame as pg
import models.player as player

width, height = 1920//2, 1080//2
sys_width, sys_height = pg.display.Info().current_w, pg.display.Info().current_h
scales = (sys_width/width, sys_height/height)
screen = pg.display.set_mode((sys_width, sys_height))

WHITE = (200, 200, 200)

platforms = []
spikes = []

level.read_data(screen, platforms, spikes, 'objects.json')
level.scale_objects(platforms, scales)
level.scale_objects(spikes, scales)

hero = player.Player(300, 100, screen)
fps = 60
fpsClock = pg.time.Clock()
pg.init()

theme = menu.Theme('background.png', sys_width, sys_height)

finished = False
d=2
left=False
right=False
up=False
down=False
space=False

class Game:
    '''Конструктор класса Game
    Args:
    screen - экран
    platforms - список платформ
    spikes - список шипов
    '''
    def __init__(self, screen, platforms, spikes):
        self.screen = screen
        self.platforms = platforms
        self.spikes = spikes
        self.up = up
        self.down = down
        self.right = right
        self.left = left
        self.space = space
        
    def start_game(self):
        '''Запуск игры'''
        finished = False
        while not finished:
            self.screen.fill(WHITE)
            hero.draw(screen)
            menu.game_buttons(screen, scales, menu.exit_game, menu.exit_game)  # Функции выхода из игры заменить на функции паузы и подсказки
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    finished = True

            for platform in self.platforms:
                platform.draw()
            for spike in self.spikes:
                spike.draw()

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    finished = True
                #elif event.type==pg.KEYDOWN:
                  #  if event.key==pg.K_UP:
                        #self.up = True
                   # if event.key==pg.K_LEFT:
                       # self.left = True
                  #  if event.key==pg.K_RIGHT:
                      #  self.right = True
                   # if event.key==pg.K_SPACE:
                      #  self.space = True
               # elif event.type==pg.KEYUP:
                   # if event.key==pg.K_UP:
                        #self.up = False
                   # if event.key==pg.K_LEFT:
                      #  self.left = False
                   # if event.key==pg.K_RIGHT:
                        #self.right = False
                   # if event.key==pg.K_SPACE:
                       # self.space = False
            #hero.update(self.left, self.right, self.up, self.down, self.screen, self.platforms)
            
            if level.check_passage():
                #FIXME: когда уровень пройден нужно открыть дверь
                for el in self.platforms:
                    el.move()
                for el in self.spikes:
                    el.move()

            pg.display.update()

game = Game(screen, platforms, spikes)

while not finished:
    screen.fill(WHITE)
    #theme.init_theme(screen)
    #menu.start_buttons(screen, scales, game.start_game, menu.exit_game, menu.resume_game)
    
    for platform in platforms:
        platform.draw()
    for spike in spikes:
        spike.draw()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            finished = True
        elif event.type==pg.KEYDOWN:
            if event.key==pg.K_UP:
                up =True
            if event.key==pg.K_LEFT:
                left =True
            if event.key==pg.K_RIGHT:
                right =True
            if event.key==pg.K_SPACE:
                space =True
        elif event.type==pg.KEYUP:
            if event.key==pg.K_UP:
                up=False
            if event.key==pg.K_LEFT:
                left = False
            if event.key==pg.K_RIGHT:
                right = False
            if event.key==pg.K_SPACE:
                space = False
    hero.update(left,right,up,down,screen,platforms) 
    for event in pg.event.get():
                if event.type == pg.QUIT:
                    finished = True
                
    # print( pg.Rect.colliderect(hero.rect,platforms[3].make_rect()))
    # print(hero.rect.x,hero.rect.y,hero.rect.width,hero.rect.heightd)
    pg.display.update()
    fpsClock.tick(fps)

pg.quit()