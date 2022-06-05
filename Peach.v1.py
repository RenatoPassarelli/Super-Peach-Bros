# ===== Inicialização =====
# ----- Importa e inicia pacotes
from pickle import TRUE
import pygame
from os import path
from config import * 
from personagem import * 
from mapas import MAPAS, jan_altura, jan_largura
from elementos import Bloco
from personagem import batida


pygame.init()
# ----- Gera tela principal
window = pygame.display.set_mode((jan_largura, jan_altura))
pygame.display.set_caption('Super Peach game')
# Placar 
fonte_placar = pygame.font.Font("C:/Users/bebec/OneDrive/Área de Trabalho\Super-Peach-Bros/font/PressStart2P.ttf", 28)
tempo = 0 
moedas = 0 
nivel = 0 

# ----- Inicia Assets
# Tiles
chao_padrao = pygame.image.load(path.join(path.dirname(__file__),"Imagens\chao.png")).convert()
chaozinho = pygame.transform.scale(chao_padrao, (60,60))

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
all_blocos = pygame.sprite.Group()
player = None

mapa = MAPAS[0]
nivel = list(MAPAS.keys())[0] + 1 

for l in range(len(mapa)):
    for c in range(len(mapa[l])):
        e = mapa[l][c]
        if e == "X":
            b = Bloco(chaozinho, l, c)
            all_blocos.add(b)
            all_sprites.add(b)
        elif e == "P":
            player = Player(peachzinha1,peachzinhaco1, l, c,all_blocos)
            all_sprites.add(player)


# Looping do Game 
while game:
    clock.tick(FPS)
    #tempo = clock.tick(FPS)
    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        # ----- Se é para sair do jogo
        if event.type == pygame.QUIT:
            game = False
        # ----- Checa as teclas apertadas 

        keys_pressed=pygame.key.get_pressed()


        if event.type == pygame.KEYDOWN:        
            if event.key == pygame.K_LEFT:
                player.speedx -= 5
            if event.key == pygame.K_RIGHT:
                player.speedx += 5
            if event.key == pygame.K_SPACE:
                player.jump()   
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT and player.speedx>-1:
                player.speedx = 0 
            if event.key == pygame.K_LEFT and player.speedx<-1:
                player.speedx += 5
            if event.key == pygame.K_RIGHT and player.speedx>1:
                player.speedx -=5
            if event.key == pygame.K_RIGHT and player.speedx<1:
                player.speedx =0

        
    # Atualizando a posição das sprites
    if player.rect.x > WIDTH/2 and player.speedx > 0: 
        for bloco in all_blocos:
            bloco.rect.x -= 5
            player.speedx = 0.0001
    if player.rect.x < WIDTH/8 and player.speedx < 0: 
        for bloco in all_blocos:
            bloco.rect.x += 5
            player.speedx = -0.0001

    #print(player.speedx)

    all_sprites.update() 

    

    window.fill((0, 200, 253))  # Preenche com a cor de fundo
    all_sprites.draw(window)

    # Placar
    text_tempo = fonte_placar.render("Tempo: {:02d}".format(tempo), True, (0,0,0))
    text_moedas = fonte_placar.render("Moedas: {}".format(moedas), True, (0,0,0))
    text_nivel = fonte_placar.render("Nível: {}".format(nivel), True, (0,0,0))
    text_moedas_rect = text_moedas.get_rect()
    text_nivel_rect = text_nivel.get_rect()
    text_tempo_rect = text_tempo.get_rect()
    text_moedas_rect.midtop = ((WIDTH/5), 15)
    text_nivel_rect.midtop = ((WIDTH/5)*2.5, 15)
    text_tempo_rect.midtop = ((WIDTH/5)*4., 15)
    window.blit(text_moedas, text_moedas_rect)
    window.blit(text_nivel, text_nivel_rect)
    window.blit(text_tempo, text_tempo_rect)


    pygame.display.update()
