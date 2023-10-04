import pygame
from pygame.locals import *
import botoes
from parametros import *
from pomekons import Pomekon
from ia_pomekon import inteligencia
from time import sleep

pygame.init()
#Criando a tela
largura, altura = 240, 160
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('BATALHA')

#Carregando imagens dos botoes
i_descansa = pygame.image.load('imagens/sleep.png').convert_alpha()
i_atkfraco = pygame.image.load('imagens/ataque_fraco.png').convert_alpha()
i_atkforte = pygame.image.load('imagens/ataque_forte.png').convert_alpha()
i_noatkfor = pygame.image.load('imagens/No_atqforte.png').convert_alpha()
i_noatkfra = pygame.image.load('imagens/No_atqfraco.png').convert_alpha()
i_quitgame = pygame.image.load('imagens/quit.png').convert_alpha()
#carregando sons para botoes
nao_funciona = pygame.mixer.Sound('sons/button_press.mp3')
#carregando imagens dos parâmetros
i_stamina = pygame.image.load('imagens/energy.png').convert_alpha()
i_ptdevida = pygame.image.load('imagens/Coracao.png').convert_alpha()
#Carragando imagens dos mobs
i_pikachu = pygame.image.load('imagens/pikachu.png').convert_alpha()
i_squirt = pygame.image.load('imagens/squirtle_32.png').convert_alpha()

#Criando os botões
botao_atkforte = botoes.Buttons_atk(i_atkforte, i_noatkfor, 1.0, 190, 135)
botao_atkfraco = botoes.Buttons_atk(i_atkfraco, i_noatkfra, 1.0, 190, 114)
botao_dormir = botoes.Buttons(i_descansa, 1.0, 190, 93)
botao_sair = botoes.Buttons(i_quitgame, 1.0, 220, 8)
#Escolhendo a fonte e cor
text_font = pygame.font.SysFont("Arial", 12)
text_font2 = pygame.font.SysFont("Arial", 20)
cor = (255, 255, 0 )

#criando o pomekon
pica_chu = Pomekon('Picachu', 50, 'Choque do Trovão', 10, 'Tempestade Elétrica', 20, 10, i_pikachu)
squirtle = Pomekon('Squirtle', 50, 'Jato de água', 10, 'Pulso de água', 20, 10, i_squirt)

#O pikachu vai ser o 'protagonista' da luta, então ele precisa de destaque na tela
pica_chu.transformar(4.0)
#O Squirtle vai ser o adversário, ele fica no fundo, mas ainda precisa ser visto e no sentido invertido
squirtle.transformar(3.0)
squirtle.invertendoX()
#Decidindo quem começa
vez = 1

#Printando de quem é a vez 
user_time = False
mob_time = False

#Loop principal
run = True

while run:
    #Colocando botao de sair do jogo
    botao_sair.put_it_on(tela)
    if botao_sair.draw():
        run = False
    #Colocando os desenhos na tela 
    imagens(i_stamina, 1.0, 10, 5,tela)
    imagens(i_ptdevida, 1.0, 50, 5, tela)
    #Colocando os parâmetros de stamina e hp
    escreve(str(pica_chu.stamina), text_font, cor, 26, 3 ,tela)
    escreve(str(pica_chu.hp), text_font, cor, 66, 3, tela)
    #Colocando os mobs na tela
    pica_chu.mob_on(tela, 0 ,30)
    squirtle.mob_on(tela, 140, 5)
    #Apertando
    if vez == 1:
            #Colocando os botoes
            botao_dormir.put_it_on(tela)
            #Se o botão está funcionando ou não
            test = pica_chu.da_pra_bater(2)
            if test:
                botao_atkforte.put_it_on_func(tela)
            else:
                botao_atkforte.put_it_on_nfuc(tela)
            #Se o botão está funcionando ou não
            test1 = pica_chu.da_pra_bater(1)
            if test1:
                botao_atkfraco.put_it_on_func(tela)
            else:
                botao_atkfraco.put_it_on_nfuc(tela)

            pica_chu.conserta_stamina()
            #Escolha do player
            if botao_atkforte.draw():
                print('ATAQUE FORTE')
                test = pica_chu.da_pra_bater(2)
                if test:
                    hit = pica_chu.ataque_forte()
                    squirtle.apanhar(hit)
                    vez = 2
                else:
                    nao_funciona.play()

            if botao_atkfraco.draw():
                print('ATAQUE FRACO')
                test = pica_chu.da_pra_bater(1)
                if test:
                    hit = pica_chu.ataque_fraco()
                    squirtle.apanhar(hit)
                    vez = 2
                else:
                    nao_funciona.play()

            if botao_dormir.draw():
                escreve(str(pica_chu.stamina), text_font, cor, 26, 3 ,tela)
                print('DORMIU')
                pica_chu.dormir()
                vez = 2
            
            pica_chu.conserta_hp()

    #Usando algo que era pra ser uma IA
    if vez == 2:
        sleep(3)
        inteligencia(squirtle, pica_chu)
        squirtle.conserta_hp()
        vez = 1
    
    #fim de batalha
    if pica_chu.hp <= 0:
        escreve('VOCÊ PERDEU!', text_font2, cor, 60, 70, tela)
    if squirtle.hp <= 0:
        escreve('VOCÊ GANHOU!', text_font2, cor, 60, 70, tela)

    #fechando o jogo
    for event in pygame.event.get(): 
        if event.type == QUIT:
            run = False

    pygame.display.update()

pygame.quit()