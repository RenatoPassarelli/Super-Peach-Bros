import pygame 
from config import * 

#pulo do personagem
y_gravidade=1
y_saltomax=20
y_velocidade= y_saltomax
foto=0
jumping=False 
right=False
left=False

# Cria Classe do personagem
class player(pygame.sprite.Sprite):
    def __init__(self, img, imgcont):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.certo=img
        self.cont=imgcont
        self.rect = self.image.get_rect()
        self.rect.centerx = peach_largura / 2
        self.rect.bottom =540
        self.speedx = 0
        self.speedy=0

    def update(self):
        
        # Atualização da posição da PEACH
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        # Mantem dentro da tela
        if self.rect.right > 1200:
            self.rect.right =1200
        if self.rect.left < 0:
            self.rect.left = 0
        if self.speedx<0:
            self.image= self.cont
        if self.speedx>0:
            self.image= self.certo