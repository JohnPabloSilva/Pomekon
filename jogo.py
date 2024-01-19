import pygame
from pygame.locals import *
import botoes
from parametros import *
from pomekons import Pomekon
from ia_pomekon import inteligencia
from battle_system import *
from time import sleep

pygame.init()
#Criando a tela
largura, altura = 240, 160
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('BATALHA POMEKÓN')

#Carregando imagens dos botoes do menu
i_start = pygame.image.load('imagens/start.png').convert_alpha()
i_quit_menu = pygame.image.load('imagens/quit_menu.png').convert_alpha() #Esse também vai ser usado no menu de pause e encerramento
#Carregando imagens do menu de pause
i_pause = pygame.image.load('imagens/pause.png').convert_alpha()
i_resume = pygame.image.load('imagens/resume.png').convert_alpha()
i_restart = pygame.image.load('imagens/restart.png').convert_alpha() #também será usado no encerramento

#Carregando imagens dos botoes do jogo
i_descansa = pygame.image.load('imagens/sleep.png').convert_alpha()
i_nodescan = pygame.image.load('imagens/No_sleep.png').convert_alpha()
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

#Criando os botões da tela do inicio 
botao_start_menu = botoes.Buttons(i_start, 1.0, 88, 43)
botao_sair_menu = botoes.Buttons(i_quit_menu, 1.0, 88, 85)
#Criando os botões do menu do pause
botao_resume = botoes.Buttons(i_resume, 1.0, 88, 22)
botao_restart = botoes.Buttons(i_restart, 1.0, 88, 64)
botao_sair_pause = botoes.Buttons(i_quit_menu, 1.0, 88, 106)
#Criando botões que encerramento da partida
botao_restart_ence = botoes.Buttons(i_restart, 1.0, 88, 73)
botao_sair_encerra = botoes.Buttons(i_quit_menu, 1.0, 88, 115)

#Criando os botões da tela de jogo
botao_atkforte = botoes.ButtonsPlayer(i_atkforte, i_noatkfor, 1.0, 185, 135)
botao_atkfraco = botoes.ButtonsPlayer(i_atkfraco, i_noatkfra, 1.0, 185, 114)
botao_dormir = botoes.ButtonsPlayer(i_descansa, i_nodescan, 1.0, 185, 93)
botao_sair = botoes.Buttons(i_quitgame, 1.0, 225, 4)
botao_pause = botoes.Buttons(i_pause, 1.0, 225,20)
#Escolhendo a fonte e cor
text_font = pygame.font.SysFont("Arial", 13)
text_font2 = pygame.font.SysFont("Arial", 16)
cor = (255, 165, 0 )

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

#Variável auxiliar para colocar ou tirar botões da tela
fim = False

#Loop principal
run = True

#Estado da tela
state = 'Inicio'

while run:
    tela.fill((65,105,225))
    if state == 'Inicio':
        botao_start_menu.put_it_on(tela)
        botao_sair_menu.put_it_on(tela)
        if botao_start_menu.draw():
            print('Iniciando')
            state = 'Jogando'
        if botao_sair_menu.draw():
            print('saindo')
            run = False

    if state == 'Jogando':
        #Colocando botao de sair do jogo
        botao_sair.put_it_on(tela)
        botao_pause.put_it_on(tela)
        if botao_sair.draw():
            run = False
        if botao_pause.draw():
            state = 'Pause'
        #Colocando todos os parâmetro do pokemon do player e do adversário
        things_on_battle(pica_chu, squirtle, i_stamina, i_ptdevida, text_font, cor, tela)
        #Apertando
        if fim == False:
            if vez == 1:
                escreve('YOUR TURN', text_font, cor, 5, 10, tela)
                #Colocando botões na tela
                put_buttons_player(pica_chu, botao_dormir, botao_atkforte, botao_atkfraco, tela)
                pica_chu.conserta_hp()
                #Escolha do player
                    #Apertando o botão de ataque forte
                if botao_atkforte.draw():
                    print('ATAQUE FORTE')
                    vez = attacking_strong(pica_chu, squirtle)
                    #Apertando o botão de ataque fraco
                if botao_atkfraco.draw():
                    print('ATAQUE FRACO')
                    vez = attacking_weak(pica_chu, squirtle)
                    #Apertando o botão para dormir
                if botao_dormir.draw():
                    print('DORMIU')
                    pica_chu.dormir()
                    vez = 2
                #Fim da batalha?
                fim = fim_de_batalha(pica_chu, squirtle)
            #Usando algo que era pra ser uma IA
            else:
                escreve("OPPONENT'S TURN", text_font, cor, 5, 10, tela)
                pygame.display.update()
                sleep(1)
                taking_out_buttons(botao_dormir, botao_atkforte, botao_atkfraco, tela)
                inteligencia(squirtle, pica_chu)
                sleep(1)
                vez = 1
                #Fim da batalha?
                fim = fim_de_batalha(pica_chu, squirtle)
        else:
            who_won(pica_chu, squirtle, text_font2, cor, tela)
            botao_restart_ence.put_it_on(tela)
            botao_sair_encerra.put_it_on(tela)
            if botao_restart_ence.draw():
                restart(pica_chu, squirtle)
                fim = False
            if botao_sair_encerra.draw():
                state = 'Inicio'

    if state == 'Pause':
        #Colocando botao de sair do jogo
        botao_sair_pause.put_it_on(tela)
        botao_restart.put_it_on(tela)
        botao_resume.put_it_on(tela)
        if botao_resume.draw():
            state = 'Jogando'
        if botao_restart.draw():
            restart(pica_chu, squirtle)
            state = 'Jogando'
        if botao_sair_pause.draw():
            run = False
    
    #fechando o jogo
    for event in pygame.event.get(): 
        if event.type == QUIT:
            run = False

    pygame.display.update()

pygame.quit()

#Tem 141 linhas  02/01/2024
#Tem 173 linhas  11/01/2024