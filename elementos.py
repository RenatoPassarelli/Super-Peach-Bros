# Imports 
import pygame
from config import tile_size, WIDTH
from os import path

# Definind as classes do jogo 

# Limites ---- Direita e Esquerda 
class Limite(pygame.sprite.Sprite):
    def __init__(self, img, l, c):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = c * tile_size
        self.rect.y = l * tile_size

    def update(self):
        pass

class LimiteE(pygame.sprite.Sprite):
    def __init__(self, img, l, c):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = c * tile_size
        self.rect.y = l * tile_size

    def update(self):
        pass

class LimiteD(pygame.sprite.Sprite):
    def __init__(self, img, l, c):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = c * tile_size
        self.rect.y = l * tile_size

    def update(self):
        pass
    
# Blocos mapa 
class Bloco(pygame.sprite.Sprite):
    def __init__(self, img, l, c):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = c * tile_size
        self.rect.y = l * tile_size

# Torre jogo 
class Jorre(pygame.sprite.Sprite):
    def __init__(self, img, l, c):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = c * tile_size
        self.rect.y = l * tile_size

# Arvores      
class Arvore(pygame.sprite.Sprite):
    def __init__(self, img, l, c):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = c * tile_size
        self.rect.y = l*tile_size-130

#Pinheiros
    def update(self):
        pass 

class Pinheiro(pygame.sprite.Sprite):
    def __init__(self, img, l, c):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = c * tile_size
        self.rect.y = l*tile_size-330

class Gelinho(pygame.sprite.Sprite):
    def __init__(self, img, l, c):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = c * tile_size
        self.rect.y = l*tile_size

    def update(self):
        pass 

class Vegetacao(pygame.sprite.Sprite):
    def __init__(self, img, l, c):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = c * tile_size
        self.rect.y = l*tile_size+30

    def update(self):
        pass 

class Arvore_morta(pygame.sprite.Sprite):
    def __init__(self, img, l, c):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = c * tile_size
        self.rect.y = l*tile_size-150

    def update(self):
        pass 


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
            
        
# Moedas    
class Moedas(pygame.sprite.Sprite):
    def __init__(self, l, c,limites):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)
        self.frames = []
        for i in range(1,12):
            self.image = pygame.image.load(path.join(path.dirname(__file__),'Imagens/moeda2/{}.png'.format(i))).convert_alpha()
            self.image = pygame.transform.scale(self.image, (45,45))
            self.frames.append(self.image)
        self.frame_atual = 0
        self.image = self.frames[self.frame_atual]
        self.rect = self.image.get_rect()
        self.rect.x = c * tile_size
        self.rect.y = l * tile_size-20
        
        self.pecas=limites

    def update(self):
        self.frame_atual += 0.40
        limitess = pygame.sprite.spritecollide(self, self.pecas, False)
        if self.frame_atual > len(self.frames):
            self.frame_atual = 0
        self.image = self.frames[int(self.frame_atual)]
       
# Nuvenzinhas do céu 
class Nuvem(pygame.sprite.Sprite):
    def __init__(self, img, l, c):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = c * tile_size
        self.rect.y = l * tile_size 

    def update(self):
        pass 

# Estrela fim de jogo 
class Estrela(pygame.sprite.Sprite):
    def __init__(self, l, c,limites):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)
        self.frames = []
        for i in range(1,9):
            self.image = pygame.image.load(path.join(path.dirname(__file__),'Imagens/estrela2/{}.png'.format(i))).convert_alpha()
            self.image = pygame.transform.scale(self.image, (45,45))
            self.frames.append(self.image)
        self.frame_atual = 0
        self.image = self.frames[self.frame_atual]
        self.rect = self.image.get_rect()
        self.rect.x = c * tile_size
        self.rect.y = l * tile_size-20
        
        self.pecas=limites

    def update(self):
        self.frame_atual += 0.30
        limitess = pygame.sprite.spritecollide(self, self.pecas, False)
        if self.frame_atual > len(self.frames):
            self.frame_atual = 0
        self.image = self.frames[int(self.frame_atual)]
