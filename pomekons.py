from pygame import transform

class Pomekon:

    __slots__ = ['image', '_nome', '_maxhp','_hp', '_atk1', '_atk2', '_dano1', '_dano2', '_stamina', '_maxstamina']

    def __init__(self,nome, hp, atk1, dano1, atk2, dano2, stamina, image):
        self.image = image
        self._nome = nome
        self._maxhp = int(hp) #Quantidade máxima de hp da espécie
        self._hp = int(hp) #Quantidade de hp em luta
        self._atk1 = atk1 #Nome do ataque 1
        self._atk2 = atk2 #Nome do ataque 2
        self._dano1 = int(dano1) #Dano do ataque 1
        self._dano2 = int(dano2) #Dano do ataque 2
        self._stamina = int(stamina) #Quantidade de energia em luta
        self._maxstamina = int(stamina) #Quantidade máxima de energia
            
    #Para o mob perder vida durante a batalha
    def apanhar(self, dano_sofrido):
        self._hp = self._hp - dano_sofrido

    #Para recuperar a energia do mob
    def dormir(self):
        if self._stamina + 4 > self._maxstamina:
            self._stamina = self._maxstamina
        else:
            self._stamina = self._stamina + 4
        
    #Função para consertar e impedir erros

    def conserta_hp(self):
        if self._hp < 0:
            self._hp = 0

    #Função para "reiniciar o mob" tanto para hp para stamina
    def restaura_hp(self):
        self._hp = self._maxhp
    
    def restaura_stamina(self):
        self._stamina = self._maxstamina

    #Função para pegar o nome, stamina, hp e atk
    def get_name(self):
        return self._nome
    
    def get_stamina(self):
        return self._stamina 

    def get_hp(self):
        return self._hp
    
    def get_atk(self, num):
        if num == 1:
            return self._dano1
        elif num == 2:
            return self._dano2
        
    def get_name_atk(self, num):
        if num == 1:
            return self._atk1
        elif num == 2:
            return self._atk2
        
    #Função para setar a stamina, isso é, gastar ela
    def energia_gasta(self, num):
        self._stamina -= num

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


#Tem 82 linhas na versão no inicio 02/01/2024
#Tem 75 linhas na versão do dia 11/01/2024
#Tem 72 linhas na versão do dia 19/01/2024
#Tem 79 linhas na versão do dia 12/04/2024



