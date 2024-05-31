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
i_panda = pygame.image.load('imagens/panda.png').convert_alpha()
i_redpanda = pygame.image.load('imagens/red_panda.png').convert_alpha()

#Criando os botões da tela do inicio 
botao_start_menu = botoes.Buttons(1.0, 88, 43, i_start)
botao_sair_menu = botoes.Buttons(1.0, 88, 85, i_quit_menu)
#Criando os botões do menu do pause
botao_resume = botoes.Buttons(1.0, 88, 22, i_resume)
botao_restart = botoes.Buttons(1.0, 88, 64, i_restart)
botao_sair_pause = botoes.Buttons(1.0, 88, 106, i_quit_menu)
#Criando botões que encerramento da partida
botao_restart_ence = botoes.Buttons(1.0, 88, 73, i_restart)
botao_sair_encerra = botoes.Buttons(1.0, 88, 115, i_quit_menu)

#Criando os botões da tela de jogo
botao_atkforte = botoes.Buttons(1.0, 185, 135, i_atkforte, i_noatkfor)
botao_atkfraco = botoes.Buttons(1.0, 185, 114, i_atkfraco, i_noatkfra)
botao_dormir = botoes.Buttons(1.0, 185, 93, i_descansa, i_nodescan)
botao_sair = botoes.Buttons(1.0, 225, 4, i_quitgame)
botao_pause = botoes.Buttons(1.0, 225,20, i_pause)
#Escolhendo a fonte e cores
text_font = pygame.font.SysFont("Calibri", 13, bold=True)
text_font2 = pygame.font.SysFont("Papirus", 16, bold=True)
cor_amarela = (255, 165, 0 )
cor_vermelh = (255, 25, 25)

#criando o pomekon
panda = Pomekon('Panda', 50, 'Wuxi finger scam', 10, 'Belly', 20, 10, i_panda)
red_panda = Pomekon('Red_panda', 50, 'Dancing blow', 10, 'Big hug', 20, 10, i_redpanda)

#O pikachu vai ser o 'protagonista' da luta, então ele precisa de destaque na tela
panda.transformar(4.0)
#O red_panda vai ser o adversário, ele fica no fundo, mas ainda precisa ser visto e no sentido invertido
red_panda.transformar(3.0)
red_panda.invertendoX()
#Decidindo quem começa
vez = 1
acao = 3

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
        botao_start_menu.put_it_on_func(tela)
        botao_sair_menu.put_it_on_func(tela)
        if botao_start_menu.draw():
            print('Iniciando')
            state = 'Jogando'
        if botao_sair_menu.draw():
            print('saindo')
            run = False

    if state == 'Jogando':
        #Colocando botao de sair do jogo
        botao_sair.put_it_on_func(tela)
        botao_pause.put_it_on_func(tela)
        if botao_sair.draw():
            run = False
        if botao_pause.draw():
            state = 'Pause'
        #Colocando todos os parâmetro do pokemon do player e do adversário
        things_on_battle(panda, red_panda, i_stamina, i_ptdevida, text_font, cor_amarela, tela)
        #Apertando
        if fim == False:
            if vez == 1:
                escreve('YOUR TURN', text_font, cor_amarela, 5, 10, tela)
                #Colocando botões na tela
                put_buttons_player(panda, botao_dormir, botao_atkforte, botao_atkfraco, tela)
                panda.conserta_hp()
                #Escolha do player
                    #Apertando o botão de ataque forte
                if botao_atkforte.draw():
                    acao = 2
                    vez = attacking_strong(panda, red_panda)
                    #Apertando o botão de ataque fraco
                if botao_atkfraco.draw():
                    acao = 1
                    vez = attacking_weak(panda, red_panda)
                    #Apertando o botão para dormir
                if botao_dormir.draw():
                    acao = 0
                    panda.dormir()
                    vez = 1.5
                #Fim da batalha?
                fim = fim_de_batalha(panda, red_panda)

            elif vez == 1.5: #É um meio termo entre a troca de turnos
                             #Serve para mostrar o nome dos ataques realizados no turno anterior
                try:
                    if acao == 1:
                        escreve(panda.get_name_atk(1), text_font, cor_amarela, 85, 110, tela)
                    elif acao == 2:
                        escreve(panda.get_name_atk(2), text_font, cor_amarela, 85, 110, tela)
                    elif acao == 0:
                        escreve("SLEPPED", text_font, cor_amarela, 85, 110, tela)     
                except:
                    continue
                pygame.display.update()
                #sleep(3)
                pygame.time.delay(3000)
                vez = 2

            elif vez == 2: #Turno do oponente
                pygame.display.update()
                escreve("OPPONENT'S TURN", text_font, cor_amarela, 5, 10, tela)
                pygame.display.update()
                taking_out_buttons(botao_dormir, botao_atkforte, botao_atkfraco, tela)
                #Usando algo que era pra ser uma IA
                acao = inteligencia(red_panda, panda)
                sleep(1)
                vez = 2.5
                #Fim da batalha?
                pygame.display.update()
                fim = fim_de_batalha(panda, red_panda)

            elif vez == 2.5: #É um meio termo entre a troca de turnos
                             #Serve para mostrar o nome dos ataques realizados no turno anterior
                try:
                    if acao == 1:
                        escreve(red_panda.get_name_atk(1), text_font, cor_vermelh, 95, 65, tela)
                    elif acao == 2:
                        escreve(red_panda.get_name_atk(2), text_font, cor_vermelh, 95, 65, tela)
                    elif acao == 0:
                        escreve("SLEPPED", text_font, cor_vermelh, 95, 65, tela)     
                except:
                    continue
                pygame.display.update()
                sleep(3)
                vez = 1
            
        else:
            who_won(panda, red_panda, text_font2, cor_amarela, tela)
            botao_restart_ence.put_it_on_func(tela)
            botao_sair_encerra.put_it_on_func(tela)
            if botao_restart_ence.draw():
                restart(panda, red_panda)
                fim = False
            if botao_sair_encerra.draw():
                state = 'Inicio'

    if state == 'Pause':
        #Colocando botao de sair do jogo
        botao_sair_pause.put_it_on_func(tela)
        botao_restart.put_it_on_func(tela)
        botao_resume.put_it_on_func(tela)
        if botao_resume.draw():
            state = 'Jogando'
        if botao_restart.draw():
            restart(panda, red_panda)
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
#Tem 209 linhas  12/04/2024