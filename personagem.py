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
class Player(pygame.sprite.Sprite):
    def __init__(self, img, imgcont, l, c):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)
        self.y_gravidade=1
        self.y_saltomax=20
        self.y_velocidade=self.y_saltomax
        self.jumping=False
        self.image = img
        self.certo=img
        self.cont=imgcont
        self.rect = self.image.get_rect()
        self.rect.x = c * tile_size
        self.rect.centery = l * tile_size  + 20
        self.speedx = 0
        self.speedy = 0
   
        


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
        if self.jumping:
            self.rect.y -= self.y_velocidade
            self.y_velocidade-= self.y_gravidade
            if self.y_velocidade < -(self.y_saltomax):
                self.jumping= False
                self.y_velocidade= self.y_saltomax
        