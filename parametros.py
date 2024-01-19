import pygame

#Esse arquivo é responsável por guardar as funções do que é escrito e colocado na tela

def imagens(image, scale, x, y, surface):
    largura = image.get_width()
    altura = image.get_height()
    image = pygame.transform.scale(image, (int(largura * scale), int(altura * scale)))
    surface.blit(image, (x,y))

def escreve(text, font, cor, x, y, surface):
    image = font.render(text, True, cor)
    #pygame.draw.rect(surface, (0, 0, 0), (x,y,12,12))
    surface.blit(image, (x, y))

def taking_out_buttons(sleep_button, atkS_button, atkW_button, screen):
    #Não estou tirando os botões, mas sim "inutilizando" eles.
    sleep_button.put_it_on_nfuc(screen)
    atkS_button.put_it_on_nfuc(screen)
    atkW_button.put_it_on_nfuc(screen)
    
def who_won(mob_player, mob_ia, style_font, color, screen):
    if mob_player.get_hp() <= 0:
        escreve('GAME OVER!', style_font, color, 78, 48, screen)
    elif mob_ia.get_hp() <= 0:
        escreve('YOU WON!', style_font, color, 86, 48, screen)

def things_on_battle(mob_player, mob_ia, image_stamina, image_hp, text_font, color, screen):
#Colocando os desenhos na tela (referente ao usuário)
    imagens(image_stamina, 1.0, 10, 35, screen)
    imagens(image_hp, 1.0, 45, 35, screen)
    #Colocando os parâmetros de stamina e hp
    escreve(str(mob_player.get_stamina()), text_font, color, 26, 33 ,screen)
    escreve(str(mob_player.get_hp()), text_font, color, 61, 33, screen)
    #Colocando os desenhos na tela(referente ao squirtle)
    imagens(image_stamina, 1.0, 145, 5, screen)
    imagens(image_hp, 1.0, 180, 5, screen)
    #Colocando os parâmetro de stamina e hp do adversário
    escreve(str(mob_ia.get_stamina()), text_font, color, 161, 3, screen)
    escreve(str(mob_ia.get_hp()), text_font, color, 196, 3, screen)
    #Colocando os mobs na tela
    mob_player.mob_on(screen, -15 ,30)
    mob_ia.mob_on(screen, 140, 5)
