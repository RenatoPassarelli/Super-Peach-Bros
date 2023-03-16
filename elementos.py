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


class Objetos(pygame.sprite.Sprite):
    def __init__(self,img, l, c):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = c * tile_size
        self.rect.y = l * tile_size 

        
   
# Blocos mapa 
class Bloco(Objetos):
    def __init__(self, img, l, c):
        # Construtor da classe mãe (Bloco).
        super().__init__(img, l, c) 
        
        
    

# Torre jogo 
class Jorre(Objetos):
    def __init__(self, img, l, c):
        # Construtor da classe mãe (Bloco).
        super().__init__(img, l, c) 

# Arvores      
class Arvore(Objetos):
    def __init__(self, img, l, c):
        # Construtor da classe mãe (Bloco).
        super().__init__(img, l, c) 
        self.rect.y -= 130

#Pinheiros
    def update(self):
        pass 

class Pinheiro(Objetos):
    def __init__(self, img, l, c):
        # Construtor da classe mãe (Bloco).
        super().__init__(img, l, c) 
        self.rect.y -= 330

class Gelinho(Objetos):
    def __init__(self, img, l, c):
        # Construtor da classe mãe (Bloco).
        super().__init__(img, l, c) 

    def update(self):
        pass 

class Vegetacao(Objetos):
    def __init__(self, img, l, c):
        # Construtor da classe mãe (Bloco).
        super().__init__(img, l, c) 
        self.rect.y += 30

    def update(self):
        pass 

class Arvore_morta(Objetos):
    def __init__(self, img, l, c):
        # Construtor da classe mãe (Bloco).
        super().__init__(img, l, c) 
        self.rect.y -= 150

    def update(self):
        pass 


            
        
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
class Nuvem(Objetos):
    def __init__(self, img, l, c):
        # Construtor da classe mãe (Bloco).
        super().__init__(img, l, c) 

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
