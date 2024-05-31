from random import randint
from battle_system import *

def inteligencia(mob_ia, user):
    mob_ia.conserta_hp()
    desejo = randint(1,3)
    if desejo == 1:
        mob_ia.dormir()
        return 0

    elif desejo == 2:
        func = da_pra_bater(mob_ia.get_stamina(), 1)
        if func:
            ataque_fraco(mob_ia, user)  
            return 1 
        else:
            mob_ia.dormir()
            return 0

    elif desejo == 3:
        func = da_pra_bater(mob_ia.get_stamina(), 2)
        if func:
            ataque_forte(mob_ia, user)  
            return 2  
        else:
            mob_ia.dormir()
            return 0

    mob_ia.conserta_hp()