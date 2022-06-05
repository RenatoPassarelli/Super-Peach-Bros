import pygame
from config import tile_size, WIDTH

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
class Bloco(pygame.sprite.Sprite):
    def __init__(self, img, l, c):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = c * tile_size
        self.rect.y = l * tile_size


    def update(self):
        pass 
class ina(pygame.sprite.Sprite):
    def __init__(self, img, l, c):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = c * tile_size
        self.rect.y = l * tile_size
    def update(self):
        pass
class animais(pygame.sprite.Sprite):
    def __init__(self, img, l, c,limites):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = c * tile_size
        self.rect.y = l * tile_size
        self.speedx=2
        self.pecas=limites

    def update(self):
        self.rect.x+=self.speedx
        limitess = pygame.sprite.spritecollide(self, self.pecas, False)
        for blocos in limitess:
            if self.speedx > 0:
                self.speedx=-2
            elif self.speedx < 0:
                self.speedx=2
        
        pass
class Moedas(pygame.sprite.Sprite):
    def __init__(self, img, l, c):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = c * tile_size
        self.rect.y = l * tile_size 

    def update(self):
        pass 

class nuvem(pygame.sprite.Sprite):
    def __init__(self, img, l, c):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = c * tile_size
        self.rect.y = l * tile_size 

    def update(self):
        pass 
