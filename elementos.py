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

    def update(self):
        pass 

# Gombas 
class Animais(pygame.sprite.Sprite):
    def __init__(self, l, c,limites):
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
        self.speedx=2
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
                self.speedx=-2
            elif self.speedx < 0:
                self.speedx=2

    def afundando(self):
        self.image = pygame.image.load(path.join('Super-Peach-Bros/Imagens/goompa2/Imagem{}.png'.format(3))).convert_alpha()
        self.image = pygame.transform.scale(self.image, (60,60))
            
        
# Moedas        
class Moedas(pygame.sprite.Sprite):
    def __init__(self, img, l, c):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = c * tile_size
        self.rect.y = l * tile_size 

    def update(self):
        pass 

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
    def __init__(self, img, l, c):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = c * tile_size
        self.rect.y = l * tile_size 

    def update(self):
        pass 
