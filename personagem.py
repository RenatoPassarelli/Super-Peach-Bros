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

# Gombas 
class Gombas(pygame.sprite.Sprite):
    def __init__(self, l, c,limites,n):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)
        self.frames = []
        for i in range(1,3):
            self.image = pygame.image.load(path.join(path.dirname(__file__),'Imagens/goompa2/Imagem{}.png'.format(i))).convert_alpha()
            self.image = pygame.transform.scale(self.image, (60,60))
            self.frames.append(self.image)
        self.frame_atual = 0
        self.image = self.frames[self.frame_atual]
        self.rect = self.image.get_rect()
        self.rect.x = c * tile_size
        self.rect.y = l * tile_size+6
        self.speedx=2*(n+1)
        self.pecas=limites

    def update(self):
        self.frame_atual += 0.14
        self.rect.x+=self.speedx
        limitess = pygame.sprite.spritecollide(self, self.pecas, False)
        if self.frame_atual > len(self.frames):
            self.frame_atual = 0
        self.image = self.frames[int(self.frame_atual)]
        for blocos in limitess:
            if self.speedx > 0:
                self.speedx=-self.speedx
            elif self.speedx < 0:
                self.speedx=-self.speedx

    def afundando(self):
        self.image = pygame.image.load(path.join('Super-Peach-Bros/Imagens/goompa2/Imagem{}.png'.format(3))).convert_alpha()
        self.image = pygame.transform.scale(self.image, (60,60))


