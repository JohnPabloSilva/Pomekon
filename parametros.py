import pygame
import pomekons


def imagens(image, scale, x, y, surface):
    largura = image.get_width()
    altura = image.get_height()
    image = pygame.transform.scale(image, (int(largura * scale), int(altura * scale)))
    surface.blit(image, (x,y))

def escreve(text, font, cor, x, y, surface):
    image = font.render(text, False, cor)
    pygame.draw.rect(surface, (0, 0, 0), (x,y,12,12))
    surface.blit(image, (x, y))
