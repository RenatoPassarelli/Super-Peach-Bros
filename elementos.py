import pygame
from config import tile_size, WIDTH

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