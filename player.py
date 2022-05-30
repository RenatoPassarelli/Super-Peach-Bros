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
class boneco(pygame.sprite.Sprite):
    def __init__(self, img, imgcont):
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
        self.rect.centerx = peach_largura / 2
        self.rect.bottom =540
        self.speedx = 0
        self.speedy=0

    def get_input(self):
        #movimento do boneco
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        keys_pressed=pygame.key.get_pressed()

        if keys_pressed[pygame.K_SPACE]:
            self.jumping=True
        if self.jumping:
            self.rect.y-=self.y_velocidade
            self.y_velocidade -= self.y_gravidade
            if self.y_velocidade <-(self.y_saltomax):
                self.jumping = False
                self.y_velocidade = self.y_saltomax
        if keys_pressed[pygame.K_LEFT]:
            self.rect.x -= 6
            self.image= self.cont
        if keys_pressed[pygame.K_RIGHT]:
            self.rect.x += 6
            self.image= self.certo


    def update(self):

        # Mantem dentro da tela
        if self.rect.right > 1200:
            self.rect.right =1200
        if self.rect.left < 0:
            self.rect.left = 0
        self.get_input()