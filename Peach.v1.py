# Fala mulecadinha, tudo bem? Suave na nave? Partiu pegar uma prainha, com os truta de verdade

# ===== Inicialização =====
# ----- Importa e inicia pacotes
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

# ----- Cria Classes
class Peach(pygame.sprite.Sprite):
    def __init__(self, img):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = img  
        self.rect = self.image.get_rect()
        self.rect.centerx = 60
        self.rect.bottom = 80
        self.speedx = 0

    def update(self):
        # Atualização da posição da nave
        self.rect.x += self.speedx

        # Mantem dentro da tela
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

# ----- Inicia estruturas de dados
game = True
all_sprites = pygame.sprite.Group()

# ----- Outros dados
player = Peach(peachzinha1)
all_sprites.add(player) 

# ===== Loop principal =====
while game:
    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False

    all_sprites.update()
    # ----- Gera saídas
    
    window.fill((0, 200, 253))  # Preenche com a cor branca
    window.blit(chaozinho1, (0, 540)) 
    window.blit(chaozinho1, (200, 540))
    window.blit(chaozinho1, (400, 540)) 
    window.blit(chaozinho1, (600, 540))  
    window.blit(chaozinho1, (800, 540))  
    window.blit(chaozinho1, (1000, 540))
    # ----- Desenha as coisas no terminal 
    all_sprites.draw(window)
    
    #peach
    # window.blit(peachzinha1, (200, 460))
    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====