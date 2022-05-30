# ===== Inicialização =====
# ----- Importa e inicia pacotes
from pickle import TRUE
import pygame
from os import path
from config import * 
from player import * 


pygame.init()
# ----- Gera tela principal
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Super Peach game')

# ----- Inicia Assets
# Tiles
chao_padrao = pygame.image.load(path.join(path.dirname(__file__),"Imagens\chaozinho.jpg")).convert()
chaozinho1 = pygame.transform.scale(chao_padrao, (200,60))

# Personagem 
peachzinha = pygame.image.load(path.join(path.dirname(__file__),"Imagens\Peachzinha.png")).convert_alpha()
peachzinha1=pygame.transform.scale(peachzinha, (60,80))
peachzinhaco=pygame.image.load(path.join(path.dirname(__file__),"Imagens\Peachzinha contrária.png")).convert_alpha()
peachzinhaco1=pygame.transform.scale(peachzinhaco, (60,80))
  
game = True
# Variável para o ajuste de velocidade
clock = pygame.time.Clock()
FPS = 60
all_sprites = pygame.sprite.Group()
player = player(peachzinha1,peachzinhaco1)
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
