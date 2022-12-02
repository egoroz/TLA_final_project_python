import pygame as pg
class Player(pg.sprite.Sprite):
    ax=1
    ay=1
    maxv=10
    
    def __init__(self,x,y,sc) -> None:
        '''#Добавь докстринг'''
        self.x=x
        self.y=y
        self.vx=0
        self.vy=0
        self.ax=1
        self.ay=1
        self.image=pg.image.load('test.png')
        self.image = pg.transform.scale(self.image, (50, 100))
        self.rect=self.image.get_rect()
    
    def update(self,left,right,up,down):
        '''#Добавь докстринг'''
        if left:
            vx=max(-self.maxv,vx-self.ax)
        if right:
            vx=min(self.maxv,vx+self.ax)
        x+=vx
    
    def draw(self,screen):
        '''#Добавь докстринг'''
        image_rect=self.image.get_rect()
        screen.blit(self.image,(self.x,self.y))




