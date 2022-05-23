# Fala mulecadinha, tudo bem? Suave na nave? Partiu pegar uma prainha, com os truta de verdade

# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame

pygame.init()

# ----- Gera tela principal
window = pygame.display.set_mode((1200, 600))
pygame.display.set_caption('Super Peach game')

# ----- Inicia Assets
chao_padrao = pygame.image.load("C:/Users/bebec/OneDrive/Área de Trabalho/Super-Peach-Bros/chaozinho.jpg").convert()
chaozinho1 = pygame.transform.scale(chao_padrao, (200,60)) 

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
<<<<<<< HEAD
    window.fill((0, 200, 253))  # Preenche com a cor branca
    window.blit(chaozinho1, (0, 540)) 
    window.blit(chaozinho1, (200, 540))
    window.blit(chaozinho1, (400, 540)) 
    window.blit(chaozinho1, (600, 540))  
    window.blit(chaozinho1, (800, 540))  
    window.blit(chaozinho1, (1000, 540)) 
=======
    window.fill((102, 178, 255))  # Preenche com a cor branca
>>>>>>> 42d5dae903d7529247a37a8c8ae3caf4bd42e1db

    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====