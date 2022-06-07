# Imports 
import pygame 
from config import * 

# Pulo do personagem
batida=False
jumping=False 
STILL=0
JUMPING=1
FALLING=2
GRAVIDADE=2

# Cria Classe do personagem
class Player(pygame.sprite.Sprite):
    def __init__(self,img,imgco,l,c,peças,ind):
        self.state=STILL
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)
        self.jumping=False 
        self.image = img[ind]
        self.certo=self.image
        self.cont=imgco[ind]
        self.rect = self.image.get_rect()
        self.rect.x = c * tile_size
        self.rect.bottom = l * tile_size 
        self.speedx = 0
        self.speedy = 0
        self.blocoss=peças

    def update(self): # Atualiza a posição do personagem 
        self.speedy += GRAVIDADE
        if self.speedy > 0:
            self.state = FALLING
        self.rect.y += self.speedy
        if self.speedx>0:
            self.image=self.certo
        if self.speedx<0:
            self.image=self.cont
       
       # Colisão com os blocos 
        bloco = pygame.sprite.spritecollide(self,self.blocoss, False)
        for blocos in bloco:
            if self.speedy > 0:
                self.rect.bottom = blocos.rect.top
                self.speedy = 0
                self.state = STILL
            elif self.speedy < 0:
                self.rect.top = blocos.rect.bottom
                self.speedy = 0
                self.state = STILL
            

        # Mantem ele dentro da tela
        if self.rect.right > 1200:
            self.rect.right =1200
        if self.rect.left < 0:
            self.rect.left = 0

        self.rect.x += self.speedx
        
        # Collide com os blocos 
        bloco = pygame.sprite.spritecollide(self, self.blocoss, False)
        for blocos in bloco:
            if self.speedx > 0:
                self.rect.right = blocos.rect.left
            elif self.speedx < 0:
                self.rect.left = blocos.rect.right

    def jump(self): # Pular 
        if self.state == STILL:
            self.speedy -= 30
            self.state = JUMPING




