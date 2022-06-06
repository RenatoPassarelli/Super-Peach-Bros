import pygame
from os import path

from config import * 


def init_screen(screen):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    # Carrega o fundo da tela inicial
    background = pygame.image.load(path.join(path.dirname(__file__), 'Imagens\inicial.png')).convert()
    background1 = pygame.transform.scale(background, (WIDTH,HEIGHT)) 
    background_rect = background1.get_rect()

    running = True
    while running:
        # Ajusta a velocidade do jogo.
        clock.tick(FPS)
        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                state = QUIT
                running = False

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE: 
                    state = GAME
                    running = False

        # A cada loop, redesenha o fundo e os sprites
        screen.fill((255,255,255))
        screen.blit(background1, background_rect)

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

    return state

def game_over_screen(screen):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock() 

    # Carrega o fundo da tela inicial
    background = pygame.image.load(path.join(path.dirname(__file__), 'Imagens\gameover.png')).convert()
    #background1 = pygame.transform.scale(background, (WIDTH,HEIGHT)) 
    background_rect = background.get_rect()

    running = True
    while running:
        # Ajusta a velocidade do jogo.
        clock.tick(FPS)
        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                state = QUIT
                running = False

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE: 
                    state = GAME
                    running = False

        # A cada loop, redesenha o fundo e os sprites
        screen.fill((0,0,0))
        screen.blit(background, ((WIDTH/3)-50, 0))

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

    return state
