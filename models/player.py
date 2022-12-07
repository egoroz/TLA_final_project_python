import pygame as pg
class Player():
    ax = 0.5
    ay = 0.5
    maxv = 5
    h=60
    w=60
   
    def __init__(self, x, y, sc) -> None:
        '''Добавь докстринг'''
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0
        self.ax = 1
        self.ay = 1
        self.jump=-10
        self.g=0.3
        self.land=False
        self.image = pg.image.load('test2.png').convert_alpha()
       # self.image= self.image.convert_alpha(self.image)
        self.image = pg.transform.scale(self.image, (self.w, self.h))
        self.rect = self.image.get_rect()
    
    def update(self, left, right, up, down,screen,platforms):
        '''Добавь докстринг'''
        if left:
            self.vx=max(-self.maxv, self.vx-self.ax)
        if right:
            self.vx=min(self.maxv, self.vx+self.ax)
        if not left and not right:
            self.vx=0
        if up:
            if self.land:
                self.vy=self.jump
                
            
        if not self.land:
            self.vy+=self.g
        self.x += self.vx
       # print(self.vy)
        self.y+=self.vy
        
        self.land=False
        self.collision(platforms)
        self.rect= pg.Rect(self.x,self.y,self.w,self.h)
        self.draw(screen)
    
    def collision(self,platforms):
        for pl in platforms:
            #print(pl)
            d=7
            if pg.Rect.colliderect(self.rect,pl.make_rect()):
                if pg.Rect.colliderect(pg.Rect(self.x,self.y+d, 2 ,self.h-3*d),pl.make_rect()):#left
                   # self.x=pl.x+pl.xx
                    self.vx=3
                if pg.Rect.colliderect(pg.Rect(self.x,self.y,self.w,2),pl.make_rect()):#up
                    self.vy=3
                if pg.Rect.colliderect(pg.Rect(self.x,self.y+self.h,self.w,2),pl.make_rect()):#down
                    self.vy=-1
                    self.land=True
                   # self.y=-self.h+pl.y
                if pg.Rect.colliderect(pg.Rect(self.x+self.w-d,self.y+d,2,self.h-2*d),pl.make_rect()):#right
                  # self.x=pl.x-self.w
                   self.vx=-3
                    
                #print(pl)
    def draw(self, screen):
        '''Добавь докстринг'''
        image_rect = self.image.get_rect()
        screen.blit(self.image, (self.x, self.y))




