import pygame
from os import path
import time 

from config import * 
def Pag1(screen):
    
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
                    state = MP 
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

def mapas_screen(screen):
    
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    # ----- Carrega Imagem de fundo
    background = pygame.image.load(path.join(path.dirname(__file__), 'Imagens\ela_mapas.png')).convert()
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
                state = PG
                running = False
                ret = [state, NN]

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1: 
                    NN=0
                    state = INIT 
                    running = False
                    ret = [state, NN]
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_2: 
                    NN=1
                    state = INIT 
                    running = False
                    ret = [state, NN]
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_3: 
                    NN=2
                    state = INIT
                    running = False
                    ret = [state, NN]
           
        
        # A cada loop, redesenha o fundo, escritos e os sprites
        screen.fill((255,255,255))
        screen.blit(background1, background_rect) 

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

    return ret 

def init_screen(screen):
    
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    # ----- Carrega Imagem de fundo
    background = pygame.image.load(path.join(path.dirname(__file__), 'Imagens\selplayer_ct.png')).convert()
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
                ret = [state, PP]

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1: 
                    PP=0
                    state = GAME
                    running = False
                    ret = [state, PP]
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_2: 
                    PP=1
                    state = GAME
                    running = False
                    ret = [state, PP]
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_3: 
                    PP=2
                    state = GAME
                    running = False
                    ret = [state, PP]
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_4: 
                    PP=3
                    state = GAME
                    running = False
                    ret = [state, PP]
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_5: 
                    PP=4
                    state = GAME
                    running = False
                    ret = [state, PP]
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_6: 
                    PP=5
                    state = GAME
                    running = False
                    ret = [state, PP]
                
        # A cada loop, redesenha o fundo, escritos e os sprites
        screen.fill((255,255,255))
        screen.blit(background1, background_rect) 

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

    return ret 

def game_over_screen(screen):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock() 

    # Carrega o fundo da tela inicial
    background = pygame.image.load(path.join(path.dirname(__file__), 'Imagens\gameover.png')).convert()
    #background1 = pygame.transform.scale(background, (WIDTH,HEIGHT)) 
    background_rect = background.get_rect()
    # Carrega a fonte 
    fonte_placar = pygame.font.Font(path.join(path.dirname(__file__),"font\PressStart2P.ttf" ),40) 

    pygame.mixer.music.load(path.join(path.dirname(__file__),"sounds\gameover_music.wav"))
    pygame.mixer.music.play()

    running = True
    while running:
        # Ajusta a velocidade do jogo.
        clock.tick(FPS)
        # Processa os eventos (mouse, teclado, botão, etc).
        # Musica tema
        pygame.mixer.music.set_volume(0.4)

        for event in pygame.event.get():
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                state = QUIT
                running = False

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_TAB: 
                    state = PG
                    time.sleep(0.5)
                    pygame.mixer.music.stop() 
                    running = False
                if event.key == pygame.K_ESCAPE:
                    state = QUIT
                    time.sleep(1)
                    pygame.mixer.music.stop() 
                    running = False 

        text_1 = fonte_placar.render("Aperte TAB para reiniciar", True, (255,255,255))
        text_2 = fonte_placar.render('para sair do jogo clique esc',True, (255,255,255))
        # A cada loop, redesenha o fundo e os sprites
        screen.fill((0,0,0))
        screen.blit(background, ((WIDTH/3)-50, 0))
        screen.blit(text_1, (60, 70))
        screen.blit(text_2, (25, 510))


        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()


    return state

def win_screen(screen):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock() 

    # Carrega o fundo da tela inicial
    background = pygame.image.load(path.join(path.dirname(__file__), 'Imagens\Você Venceu!.png')).convert()
    background1 = pygame.transform.scale(background, (WIDTH,HEIGHT)) 
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
                    state = MP
                    running = False
 

        
        # A cada loop, redesenha o fundo e os sprites
        screen.fill((0,0,0))
        screen.blit(background, background_rect)



        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()


    return state