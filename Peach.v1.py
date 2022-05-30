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
chao_padrao = pygame.image.load(path.join(path.dirname(__file__),"Imagens/chaozinho.jpg")).convert()
chaozinho1 = pygame.transform.scale(chao_padrao, (200,60))

# Personagem 
peachzinha = pygame.image.load(path.join(path.dirname(__file__),"Imagens/Peachzinha.png")).convert_alpha()
peachzinha1=pygame.transform.scale(peachzinha, (60,80))
peachzinhaco=pygame.image.load(path.join(path.dirname(__file__),"Imagens/Peachzinha contrária.png")).convert_alpha()
peachzinhaco1=pygame.transform.scale(peachzinhaco, (60,80))
  


# ----- Inicia estruturas de dados
# ----- Plota o chão (futuramente vai ser uma classe)
# window.blit(chaozinho1, (0, 540)), ----------- acho que podemos apagar tudo q ta aqui 
# window.blit(chaozinho1, (200, 540)),
# window.blit(chaozinho1, (400, 540)), 
# window.blit(chaozinho1, (600, 540)),  
# window.blit(chaozinho1, (800, 540)),  
# window.blit(chaozinho1, (1000, 540))

        
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
                player.speedx -= 6
        # Verifica se apertou alguma tecla.
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
