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
# ----- Inicia estruturas de dados
game = True

# ===== Loop principal =====
while game:
    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False

    # ----- Gera saídas
    window.fill((0, 200, 253))  # Preenche com a cor branca
    window.blit(chaozinho1, (0, 540)) 
    window.blit(chaozinho1, (200, 540))
    window.blit(chaozinho1, (400, 540)) 
    window.blit(chaozinho1, (600, 540))  
    window.blit(chaozinho1, (800, 540))  
    window.blit(chaozinho1, (1000, 540)) 

    #peach
    window.blit(peachzinha1, (200, 460))
    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====