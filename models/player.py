import pygame as pg

class Player:
    '''Конструктор класса Player
    Args:
    x - стартовое положение героя по иксу
    y - стартовое положение героя по игреку
    '''
    ax = 0.5
    ay = 0.5
    maxv = 3

    def __init__(self, x, y, w, h, scales):
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0
        self.ax = 0.5
        self.ay = 1
        self.jump = -10
        self.g = 0.25
        self.animation_index = 0
        self.land = False
        self.imp = 0
        self.scales = scales
        self.h = h * scales[1]
        self.w = w * scales[0]
        self.walk_cycle = [pg.transform.scale(pg.image.load(f"pic\p1_walk{i:0>2}.png"),(self.w,self.h)) for i in range(1,12)]
        self.stop = pg.transform.scale(pg.image.load("pic\p1_front.png"),(self.w,self.h))
        self.death = 0

    def kill (self, on, spikes):
        '''Убивает и телепортирует в начало при касании шипов'''
        flag = False
        if on:
            for pl in spikes:
                if pg.Rect.colliderect(self.rect, pl.make_rect()):
                    self.x=0
                    self.y=270*self.scales[1]
                    self.vx=0
                    self.vy=0
                    flag = True
        if flag:
            self.death += 1

    def oldcollision(self, platforms):
        '''Коллизия платформ'''
        for pl in platforms:
            d = 6
            if pg.Rect.colliderect(self.rect, pl.make_rect()):
                if pg.Rect.colliderect(pg.Rect(self.x+self.w,self.y+d,2,self.h-3*d),pl.make_rect()):
                   self.x -= 3
                   self.vx = 0
                if pg.Rect.colliderect(pg.Rect(self.x,self.y+d, 2 ,self.h-3*d),pl.make_rect()):
                    self.x += 3
                    self.vx = 0
                if pg.Rect.colliderect(pg.Rect(self.x,self.y,self.w,2),pl.make_rect()):
                    self.vy = 3
                if pg.Rect.colliderect(pg.Rect(self.x,self.y+self.h+1,self.w,2),pl.make_rect()):
                    self.vy = 0
                    while pg.Rect.colliderect(pg.Rect(self.x,self.y+self.h+1,self.w,2),pl.make_rect()):
                       self.y -= 0.01
                    self.land=True
                
    def move(self, platforms):
        '''Передвижение
        Args:
        platforms - список платформ
        '''
        if self.vx > 0 and not self.collision_in_future('r', platforms):
            self.x += self.vx
        if self.vx < 0 and not self.collision_in_future('l', platforms):
            self.x += self.vx
        if self.vy > 0 and not self.collision_in_future('d', platforms):
            self.y += self.vy
        if self.vy < 0 and not self.collision_in_future('u', platforms):
            self.y += self.vy

    def collision_in_future(self, dir, platforms):
        '''Коллизия,
        Args:
        dir - параметр
        platforms - список платформ
        '''
        d = 7
        plats = []
        for pl in platforms:
            plats.append(pl.make_rect())
        if dir == 'd':
            if pg.Rect(self.x, self.y+self.h+2, self.w, 2).collidelist(plats)!=-1:
                self.land = True
                self.vy = 0
            return pg.Rect(self.x, self.y+self.h+1, self.w, 2).collidelist(plats)!=-1
        if dir == 'l':
            return pg.Rect(self.x-1, self.y+d, 2, self.h-3*d).collidelist(plats)!=-1 or self.x<5
        if dir == 'r':
            return pg.Rect(self.x+self.w+1, self.y+d, 2, self.h-3*d).collidelist(plats)!=-1
        if dir == 'u':
            if pg.Rect(self.x, self.y-1, self.w, 2).collidelist(plats)!=-1:self.vy=0
            return pg.Rect(self.x, self.y-1, self.w, 2).collidelist(plats)!=-1
                
    def anim(self):
        '''Анимация'''
        if self.vx == 0:
            self.image = self.stop
        else:
            self.image = self.walk_cycle[self.animation_index]
            if self.vx<0:
                self.image = pg.transform.flip(self.image, True, False)
            
            if self.animation_index < len(self.walk_cycle)-1:
                self.animation_index += 1
            else:
                self.animation_index = 0  
                          
    def draw(self, screen):
        '''Отрисовка на экране screen'''
        screen.blit(self.image, (self.x, self.y))

    def update(self, left, right, up, screen, platforms, spikes):
        '''Обновление героя
        Args:
        left - обрабатывает движение влево
        right - обрабатывает движение вправо
        up - обрабатывает прыжок
        screen - экран
        platforms - список платформ
        spikes - список шипов
        '''
        if left:
            self.vx = max(-self.maxv, self.vx-self.ax)
        if right:
            self.vx = min(self.maxv, self.vx+self.ax)
        if not left and not right:
            self.vx = 0
        if up:
            if self.land:
                self.vy = self.jump
        if not self.land:
            self.vy += self.g
            self.vy = min(7, self.vy)
        self.anim()
        self.land = False
        self.move(platforms)              
        self.rect = pg.Rect(self.x, self.y, self.w, self.h+1)
        self.kill(True, spikes)
        self.draw(screen)


