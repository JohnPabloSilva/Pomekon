from random import randint
from parametros import *

#Para ataques fracos
def ataque_fraco(atacante, defensor):
    prob = randint(0,101) #Calcula a probabilidade do ataque acertar
    #A stamina diminui independetemente se o ataque acerta ou não, mas dependendo do ataque ele pode perder mais ou menos stamina
    dano_de_ataque = atacante.get_atk(1)
    atacante.energia_gasta(4)
    if 100 >= prob >= 80: #Caso seja um ataque crítico
        dano_de_ataque += 5
        defensor.apanhar(dano_de_ataque)
    elif 80 > prob >= 20: #Caso seja um ataque normal
        defensor.apanhar(dano_de_ataque)
    else: #falha ao atacar
        defensor.apanhar(0)

def ataque_forte(atacante, defensor):
    prob = randint(0,100) #Calcula a probabilidade de acerto
    dano_de_ataque = atacante.get_atk(2) #Pegar o dano de ataque do pomekon
    atacante.energia_gasta(6) #A stamina é reduzida independe do ataque acertar ou não
    if 100 >= prob >= 80:
        dano_de_ataque += 10
        defensor.apanhar(dano_de_ataque) #Ataque crítico
    elif 80 > prob >= 20:
        defensor.apanhar(dano_de_ataque) #Ataque normal
    else:
        defensor.apanhar(0) #Falha ao atacar

def da_pra_bater(stamina, atk):
    #Pra saber se o ataque é realmete possível de ser realizado
    #1 significa ataque fraco e 2 significa ataque forte
    if atk == 1 and stamina >= 4:
        return True
    elif atk == 1 and stamina < 4:
        return False
    elif atk == 2 and stamina >= 6:
        return True
    elif atk == 2 and stamina < 6:
        return False
    

def attacking_strong(mob_player, mob_ia):
    test = da_pra_bater(mob_player.get_stamina(), 2)
    if test:
        ataque_forte(mob_player, mob_ia)
        return 2 #Foi possível realizar o ataque
    else:
        return 1 #Não foi possível realizar o ataque
    
def attacking_weak(mob_player, mob_ia):
    test = da_pra_bater(mob_player.get_stamina(), 1)
    if test:
        ataque_fraco(mob_player, mob_ia)
        return 2 #Foi possível realizar o ataque
    else:
        return 1 #Não foi possível realizar o ataque
    
def fim_de_batalha(player, ia):
    #Essa funcão analisa o hp dos pokemons e faz com que a batalha de encerre 
    #caso um dos dois tenha hp menor ou igual a 0
    if player.get_hp() <= 0:
        player.conserta_hp()
        player.conserta_stamina()
        return True
    elif ia.get_hp() <= 0:
        ia.conserta_hp()
        return True
    else:
        return False
    
    
def restart(mob_player, mob_ia):
    mob_player.restaura_hp()
    mob_player.restaura_stamina()
    mob_ia.restaura_hp()
    mob_ia.restaura_stamina()

def put_buttons_player(player, sleep_button, atkS_button, atkW_button, screen):
     #Colocando os botoes que o player utiliza, lembrando que alguns botões alteram dependendo dos status do player
            sleep_button.put_it_on_func(screen)
            #Se o botão está funcionando ou não
            test = da_pra_bater(player.get_stamina(),2)
            if test:
                atkS_button.put_it_on_func(screen)
            else:
                atkS_button.put_it_on_nfuc(screen)
            #Se o botão está funcionando ou não
            test1 = da_pra_bater(player.get_stamina(), 1)
            if test1:
                atkW_button.put_it_on_func(screen)
            else:
                atkW_button.put_it_on_nfuc(screen)

#Tem 94 linhas na versão do dia 11/01/2024
#Tem 93 linhas na versão do dia 19/01/2024


