
from .template import Template
import pygame
import pygame_widgets
import pygame_widgets.button
from .game import Game
class Start(Template):
    
    def __init__(self):

        self.fps=30
        self.hw=(600,300)
    
    def start_screen(self):
        
        #button_start=pygame.Surface((100,50))
        #button_start.fill((255,255,255))
        #self.screen.blit(button_start,(self.hw[0]//2-50,self.hw[1]//2-25),)
        button=pygame_widgets.button.Button(self.screen,self.hw[0]//2-50,self.hw[1]//2-25,100,50,onClick=lambda:Game().start_game(),text="Start")
        while True:
            if self.screen.get_size()!=self.hw:
                self.screen=pygame.display.set_mode(self.hw)
                self.screen.fill((0,0,0))
            self.clock.tick(self.fps)
            events=pygame.event.get()   
            for event in events:
                if event.type == pygame.QUIT:
                    quit()
                #if event.type == pygame.MOUSEBUTTONUP:
                #    pos=pygame.mouse.get_pos()
                #    z=button_start.get_rect().collidepoint(pos)
                #    if z:
                #        self.game_run=True
                #        Game().start_game()
            
            pygame.display.update()
            pygame_widgets.update(events)