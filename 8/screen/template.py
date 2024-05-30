from abc import ABC, abstractmethod
import pygame

class Template(ABC):
    pygame.init()
    _hw=800
    res=(_hw,_hw)
    screen = pygame.display.set_mode(res)
    clock=pygame.time.Clock()
    
    @abstractmethod
    def __init__(self): ...

