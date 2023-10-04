from random import randint

def inteligencia(objeto_mob, user):
    print(f'Vez do {objeto_mob.nome}')
    print(f'{objeto_mob.nome}: HP{objeto_mob.hp} EN:{objeto_mob.stamina}')
    desejo = randint(1,3)
    if desejo == 1:
        print('DORMIU')
        objeto_mob.dormir()
    elif desejo == 2:
        func = objeto_mob.da_pra_bater(1)
        if func:
            hit = objeto_mob.ataque_fraco()
            print(f'VOCÊ FOI ACERTADO! menos {hit} para {user.nome}')
            user.apanhar(hit)
        else:
            print('DORMIU')
            objeto_mob.dormir()
    elif desejo == 3:
        func = objeto_mob.da_pra_bater(2)
        if func:
            hit = objeto_mob.ataque_forte()
            print(f'VOCÊ FOI ACERTADO! menos {hit} para {user.nome}')
            user.apanhar(hit)
        else:
            print('DORMIU')
            objeto_mob.dormir()