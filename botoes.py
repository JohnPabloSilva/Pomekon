import pygame
from pygame.locals import *

class Buttons:
    def __init__(self, scale, x, y, image, image2=None):
        self._largura = image.get_width()
        self._altura = image.get_height()
        self._image = pygame.transform.scale(image, (int(self._largura * scale), int(self._altura * scale)))
        self._rect = self._image.get_rect()
        self._rect.topleft = (x,y)
        self._pressionado = False
        if image2 != None: 
            self._image2 = pygame.transform.scale(image2, (int(self._largura * scale), int(self._altura * scale)))
    
    def draw(self):
        acao = False
        pos = pygame.mouse.get_pos()

        if self._rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self._pressionado == False:
                self._pressionado = True
                acao = True
                return acao
        
        if pygame.mouse.get_pressed()[0] == 0:
            self._pressionado = False
            return acao
        
    def put_it_on_func(self, surface):
        surface.blit(self._image, (self._rect.x, self._rect.y))

    def put_it_on_nfuc(self, surface):
        surface.blit(self._image2, (self._rect.x, self._rect.y)) 

#tem 62 linhas na versão do dia 11/01/2024
#tem 47 linhas na versão do dia 19/01/2024
#tem 33 linhas na versão do dia 11/04/2024 
        