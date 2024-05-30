 
import pygame
from random import randrange
from .template import Template



class Game(Template):
    
    def __init__(self,blsize=20):
        self.blsize=blsize
        self._hw=self._hw//blsize//2*2*blsize + blsize
        snakest=self._hw//2 - blsize//2
        self.snake_pos=[(snakest,snakest)]
        
        self.fps=7
        self.snake_lng=1
        self.rand_apple()
        self.dirx=0
        self.diry=0
        self.game_run=False
    def rand_apple(self):
        self.apple_pos=(randrange(0,self._hw-self.blsize,self.blsize),randrange(0,self._hw-self.blsize,self.blsize))
        
    def draw_snake(self):
        apple_p=(self.apple_pos[0]+self.blsize//2,self.apple_pos[1]+self.blsize//2)
        for x,y in self.snake_pos:
            pygame.draw.rect(self.screen,(255,255,255),(x,y,self.blsize-2,self.blsize-2))
            pygame.draw.circle(self.screen,(255,0,0),apple_p,self.blsize//2)
    
    def change_s_pos(self):
        
        for i in range(self.snake_lng-1,0,-1):
            self.snake_pos[i]=self.snake_pos[i-1]
        self.snake_pos[0]=(self.snake_pos[0][0]+self.dirx,self.snake_pos[0][1]+self.diry)
        
    def check_death(self):
        if self.snake_pos[0] in self.snake_pos[1:]:
            return True
        for x,y in self.snake_pos:
            if x <0 or y<0 or x>self._hw-self.blsize or y>self._hw-self.blsize:
                return True
        return False
    

    def start_game(self):
        self.screen = pygame.display.set_mode((self._hw, self._hw))
        self.game_run=True
        while self.game_run:
            self.clock.tick(self.fps)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
            
            self.screen.fill((0,0,0))
            self.draw_snake()
            key=pygame.key.get_pressed()
            if key[pygame.K_w]:
                if self.diry==0:
                    self.dirx=0
                    self.diry=-1*self.blsize
            elif key[pygame.K_s]:
                if self.diry==0:
                    self.dirx=0
                    self.diry=self.blsize
            elif key[pygame.K_a]:
                if self.dirx==0:
                    self.dirx=-1*self.blsize
                    self.diry=0
            elif key[pygame.K_d]:
                if self.dirx==0:
                    self.dirx=self.blsize
                    self.diry=0
            self.change_s_pos()
            
                
            if self.check_death():
                self.game_run=False
                
            if self.snake_pos[0]==self.apple_pos:
                self.snake_lng+=1
                self.rand_apple()
                self.snake_pos.append(self.snake_pos[-1])
            pygame.display.flip()