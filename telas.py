import pygame
from os import path

from config import * 


def init_screen(screen):
    
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()
    # ----- Carrega settings escritos 
    fonte_placar = pygame.font.Font(path.join(path.dirname(__file__),"font\PressStart2P.ttf" ),40) 
    fonte_placar_peq = pygame.font.Font(path.join(path.dirname(__file__),"font\PressStart2P.ttf" ),30) 


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

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE: 
                    state = GAME
                    running = False

        text_1 = fonte_placar.render("Bem vindo!", True, (0,0,0))
        text_2 = fonte_placar_peq.render("Aperte qualquer tecla para iniciar", True, (0,0,0))

        # A cada loop, redesenha o fundo, escritos e os sprites
        screen.fill((255,255,255))
        screen.blit(background1, background_rect)
        screen.blit(text_1, (320, 70))
        screen.blit(text_2, (90, 520))

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
    # Carrega a fonte 
    fonte_placar = pygame.font.Font(path.join(path.dirname(__file__),"font\PressStart2P.ttf" ),40) 


    running = True
    while running:
        pygame.mixer.music.set_volume(0) 
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
                    state = INIT 
                    running = False
                if event.key == pygame.K_ESCAPE:
                    pygame.time.delay(2000) 
                    state = QUIT
                    running = False 

        text_1 = fonte_placar.render("Aperte space para reiniciar", True, (255,255,255))
        text_2 = fonte_placar.render('para sair do jogo clique esc',True, (255,255,255))
        # A cada loop, redesenha o fundo e os sprites
        screen.fill((0,0,0))
        screen.blit(background, ((WIDTH/3)-50, 0))
        screen.blit(text_1, (60, 70))
        screen.blit(text_2, (25, 510))


        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()


    return state
