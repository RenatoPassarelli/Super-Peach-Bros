# ===== Inicialização =====
# ----- Importa e inicia pacotes
from pickle import TRUE
import pygame
from os import path
pygame.init()

# ----- Gera tela principal
WIDTH = 1200
HEIGHT = 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Super Peach game')

# ----- Inicia Assets
chao_padrao = pygame.image.load(path.join(path.dirname(__file__),"chaozinho.jpg")).convert()
chaozinho1 = pygame.transform.scale(chao_padrao, (200,60)) 
peachzinha = pygame.image.load(path.join(path.dirname(__file__),"Peachzinha.png")).convert_alpha()
peachzinha1=pygame.transform.scale(peachzinha, (60,80))
peachzinhaco=pygame.image.load(path.join(path.dirname(__file__),"Peachzinha contrária.png")).convert_alpha()
peachzinhaco1=pygame.transform.scale(peachzinhaco, (60,80))
peach_altura=460
peach_largura=200
# ----- Inicia estruturas de dados



window.blit(chaozinho1, (0, 540)), 
window.blit(chaozinho1, (200, 540)),
window.blit(chaozinho1, (400, 540)), 
window.blit(chaozinho1, (600, 540)),  
window.blit(chaozinho1, (800, 540)),  
window.blit(chaozinho1, (1000, 540))

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
    def __init__(self, img):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = img
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
<<<<<<< HEAD
        
=======

# Inicia o jogo
>>>>>>> a6331b335e85269c7e24925278e7d6fd0cdc17e4
game = True
# Variável para o ajuste de velocidade
clock = pygame.time.Clock()
FPS = 60
all_sprites = pygame.sprite.Group()
player = boneco(peachzinha1)
all_sprites.add(player)

# Looping do Game 
while game:
    all_sprites.add(player)
    clock.tick(FPS)
    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False
        # Verifica se apertou alguma tecla. 
        # Andar   
        if event.type == pygame.KEYDOWN:
            if event.key== pygame.K_LEFT:
                player.speedx -= 6
            if event.key== pygame.K_RIGHT:
                player.speedx += 6
        if event.type == pygame.KEYUP:
            if event.key== pygame.K_LEFT:
                player.speedx += 6
            if event.key== pygame.K_RIGHT:
<<<<<<< HEAD
                player.speedx -= 6
        # Verifica se apertou alguma tecla.
=======
                player.speedx -= 3
        # Pular
>>>>>>> a6331b335e85269c7e24925278e7d6fd0cdc17e4
    keys_pressed= pygame.key.get_pressed()
            # Dependendo da tecla, altera a velocidade.
    if keys_pressed[pygame.K_SPACE]:
            jumping= True
    if jumping:
        player.rect.y -= y_velocidade
        y_velocidade-= y_gravidade
        if y_velocidade < -(y_saltomax):
            jumping= False
            y_velocidade= y_saltomax

    # Atualizando a posição das sprites
    all_sprites.update()
    # ----- Gera saídas
    
    window.fill((0, 200, 253))  # Preenche com a cor branca
    window.blit(chaozinho1, (0, 540))
    window.blit(chaozinho1, (200, 540))
    window.blit(chaozinho1, (400, 540)) 
    window.blit(chaozinho1, (600, 540))  
    window.blit(chaozinho1, (800, 540))  
    window.blit(chaozinho1, (1000, 540)) 
    all_sprites.draw(window)

    pygame.display.update()
