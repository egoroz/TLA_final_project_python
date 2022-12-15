import pygame as pg

class Player:
    
    ax = 0.5
    ay = 0.5
    maxv = 3
    h = 60
    w = 60
   
    def __init__(self, x, y, sc) -> None:
        
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0
        self.ax = 0.5
        self.ay = 1
        self.jump = -10
        self.g = 0.25
        self.animation_index=0
        self.land=False
        self.imp=0
        self.walk_cycle = [pg.transform.scale(pg.image.load(f"pic\p1_walk{i:0>2}.png"),(self.w,self.h)) for i in range(1,12)]
        self.stop=pg.transform.scale(pg.image.load("pic\p1_front.png"),(self.w,self.h))
        self.death = 0
        #p1_walk01.png
        #self.image = pg.image.load('test2.png').convert_alpha()
       # self.image= self.image.convert_alpha(self.image)
        #self.image = pg.transform.scale(self.image, (self.w, self.h))
       # self.rect = self.image.get_rect()
    def kill (self,on,spikes):
        if on:
            for pl in spikes:
                if pg.Rect.colliderect(self.rect,pl.make_rect()):
                    self.x=0
                    self.y=440
                    self.vx=0
                    self.vy=0
                    self.death += 1

    def oldcollision(self,platforms,screen):
        for pl in platforms:
            #print(pl)
            d=6
            
           # pg.draw.rect(screen,(0,0,255),(self.x,self.y+d, 2 ,self.h-3*d))
           #pg.draw.rect(screen,(255,0,255),(self.x+self.w,self.y+d,2,self.h-3*d))
            if pg.Rect.colliderect(self.rect,pl.make_rect()):
                if pg.Rect.colliderect(pg.Rect(self.x+self.w,self.y+d,2,self.h-3*d),pl.make_rect()):#right
                  # self.x=pl.x-self.w
                  # pg.draw.rect(screen,(0,255,255),(self.x+self.h-d,self.y+d,2,self.h-2*d))
                  # print('right')
                   self.x-=3
                   self.vx=0
                if pg.Rect.colliderect(pg.Rect(self.x,self.y+d, 2 ,self.h-3*d),pl.make_rect()):#left
                   # self.x=pl.x+pl.xx
                   # pg.draw.rect(screen,(0,0,255),(self.x,self.y+d, 2 ,self.h-2*d))
                    #print('left')
                    self.x+=3
                    self.vx=0
                if pg.Rect.colliderect(pg.Rect(self.x,self.y,self.w,2),pl.make_rect()):#up
                    self.vy=3
                if pg.Rect.colliderect(pg.Rect(self.x,self.y+self.h+1,self.w,2),pl.make_rect()):#down
                    self.vy=0
                    while pg.Rect.colliderect(pg.Rect(self.x,self.y+self.h+1,self.w,2),pl.make_rect()):
                       self.y -= 0.01
                    self.land=True
                   # self.y=-self.h+pl.y
                
    def move(self,platforms):
        '''Передвижение

    Args:
    objects - список объектов для скейла
    scales - масштабирование
    '''
        if self.vx>0 and  not self.collision_in_future('r',platforms):
            self.x+=self.vx
        if self.vx<0 and not self.collision_in_future('l',platforms):
            self.x+=self.vx
        if self.vy>0 and not self.collision_in_future('d',platforms):
            self.y+=self.vy
        if self.vy<0 and not self.collision_in_future('u',platforms):
            self.y+=self.vy

    def collision_in_future(self, dir, platforms):
        '''колизится'''
        d=7
        plats=[]
        for pl in platforms:
            plats.append(pl.make_rect())
        if dir=='d':
            if pg.Rect(self.x,self.y+self.h+2,self.w,2).collidelist(plats)!=-1: 
                self.land=True
                self.vy=0
            return pg.Rect(self.x,self.y+self.h+1,self.w,2).collidelist(plats)!=-1
        if dir=='l':
            return pg.Rect(self.x-1,self.y+d, 2 ,self.h-3*d).collidelist(plats)!=-1 or self.x<5
        if dir=='r':
            return pg.Rect(self.x+self.w+1,self.y+d,2,self.h-3*d).collidelist(plats)!=-1
        if dir=='u':
            if pg.Rect(self.x,self.y-1,self.w,2).collidelist(plats)!=-1:self.vy=0
            return pg.Rect(self.x,self.y-1,self.w,2).collidelist(plats)!=-1 

                
    def anim(self):
        if self.vx==0:
            self.image=self.stop
        else:
            self.image = self.walk_cycle[self.animation_index]
            if self.vx<0:
                self.image = pg.transform.flip(self.image, True, False)
            
            if self.animation_index < len(self.walk_cycle)-1:
                self.animation_index += 1
            else:
                self.animation_index = 0  
                          
    def draw(self, screen):
        '''Добавь докстринг'''
        image_rect = self.image.get_rect()
        screen.blit(self.image, (self.x, self.y))

    def update(self, left, right, up, down, screen, platforms,spikes):
        '''Добавь докстринг'''

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
            self.vy+=self.g
            self.vy=min(7,self.vy)
        self.anim()
        self.land = False
        self.move(platforms)              
        
        
        
        self.rect = pg.Rect(self.x,self.y,self.w,self.h+1)
        self.kill(True,spikes)
        #self.collision(platforms,screen)##return!!!
        
        self.draw(screen)


