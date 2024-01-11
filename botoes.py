import pygame
from pygame.locals import *

class Buttons:
    def __init__(self, image, scale, x, y):
        largura = image.get_width()
        altura = image.get_height()
        self.image = pygame.transform.scale(image, (int(largura * scale), int(altura * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.pressionado = False

    def draw(self):
        acao = False
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.pressionado == False:
                self.pressionado = True
                acao = True
                return acao
        
        if pygame.mouse.get_pressed()[0] == 0:
            self.pressionado = False
            return acao
        
    def put_it_on(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y)) 


#Para botões de ataque, será feita uma classe diferente
#Nessa classe terá um parâmetro a mais (de imagem) e uma função para alternar imagens       
class ButtonsPlayer:

    def __init__(self, image, image2, escala, x, y):
        largura = image.get_width()
        altura = image.get_height()
        self.image = pygame.transform.scale(image, (int(largura * escala), int(altura * escala)))
        self.image2 = pygame.transform.scale(image2, (int(largura * escala), int(altura * escala)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.pressionado = False

    def draw(self):
        acao = False
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.pressionado == False:
                self.pressionado = True
                acao = True
                return acao
            
        if pygame.mouse.get_pressed()[0] == 0:
            self.pressionado = False
            return acao

    def put_it_on_func(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))

    def put_it_on_nfuc(self, surface):
        surface.blit(self.image2, (self.rect.x, self.rect.y))

        