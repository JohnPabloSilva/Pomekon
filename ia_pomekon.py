from random import randint
from battle_system import *

def inteligencia(mob_ia, user):
    print(f'{mob_ia.get_name()}: HP{mob_ia.get_hp()} EN:{mob_ia.get_stamina()}')
    mob_ia.conserta_hp()
    desejo = randint(1,3)
    if desejo == 1:
        mob_ia.dormir()

    elif desejo == 2:
        func = da_pra_bater(mob_ia.get_stamina(), 1)
        if func:
            ataque_fraco(mob_ia, user)   
        else:
            mob_ia.dormir()

    elif desejo == 3:
        func = da_pra_bater(mob_ia.get_stamina(), 2)
        if func:
            ataque_forte(mob_ia, user)    
        else:
            mob_ia.dormir()

    mob_ia.conserta_hp()