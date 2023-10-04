from random import randint
from pygame import transform

class Pomekon:
    def __init__(self,nome, hp, atk1, dano1, atk2, dano2, stamina, image):
        self.image = image
        self.nome = nome
        self.hp = int(hp)
        self.atk1 = atk1 #Nome do ataque 1
        self.atk2 = atk2 #Nome do ataque 2
        self.stamina = int(stamina) #Quantidade de eneegia
        self.dano1 = int(dano1) #Dano do ataque 1
        self.dano2 = int(dano2) #Dano do ataque 2
        self.max_stamina = int(stamina)

    def ataque_fraco(self):
        prob = randint(0,101) #Calcula a probabilidade do ataque acertar
        #Para o ataque fraco
        #A stamina diminui independetemente se o ataque acerta ou não, mas dependendo do ataque ele pode perder mais ou menos stamina
        self.stamina = self.stamina - 4
        if 100 >= prob >= 60:
            x1 = self.dano1 + 5
            return x1
        elif 60 > prob >= 20:
            x1 = self.dano1
            return x1
        else:
            return 0
             
    def ataque_forte(self):
        prob = randint(0,101) #Calcula a probabilidade do ataque acertar
        #Para o taque forte
        #A stamina diminui independetemente se o ataque acerta ou não, mas dependendo do ataque ele pode perder mais ou menos stamina
        self.stamina = self.stamina - 6
        if 100 >= prob >= 60:
            x1 = self.dano2 + 10
            return self.dano2
        elif 60 > prob >= 20:
            x1 = self.dano2
            return x1
        else:
            return 0
            
    #Para o mob perder vida durante a batalha
    def apanhar(self, dano_sofrido):
        self.hp = self.hp - dano_sofrido

    #Para recuperar a energia do mob
    def dormir(self):
        self.stamina = self.stamina + 4

    #Pra saber se o ataque é realmete possível de ser realizado
    def da_pra_bater(self, atk):
        if atk == 1 and self.stamina >= 4:
            return True
        elif atk == 1 and self.stamina < 4:
            return False
        elif atk == 2 and self.stamina >= 6:
            return True
        elif atk == 2 and self.stamina < 6:
            return False
        
    #Funções para consertar e impedir erros
    def conserta_stamina(self):
        if self.stamina < 0:
            self.stamina = 0
        elif self.stamina > self.max_stamina:
            self.stamina = self.max_stamina 

    def conserta_hp(self):
        if self.hp < 0:
            self.hp = 0
    #Alterando as imagens de acordo com o necessário
    def transformar(self, escala):
        largura = self.image.get_width()
        altura = self.image.get_height()
        self.image = transform.scale(self.image, (int(largura*escala), int(altura*escala)))
    #Colocando os mobs na tela
    def mob_on(self, surface, x, y):
        surface.blit(self.image, (x,y))
    def invertendoX(self):
        self.image = transform.flip(self.image, True, False)





