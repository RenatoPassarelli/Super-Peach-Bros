# ===== Inicialização =====
# ----- Importa e inicia pacotes
from pickle import TRUE
import pygame
from os import path
from config import * 
from personagem import * 
from mapas import MAPAS, jan_altura, jan_largura
from elementos import Bloco


pygame.init()
# ----- Gera tela principal
window = pygame.display.set_mode((jan_largura, jan_altura))
pygame.display.set_caption('Super Peach game')

# ----- Inicia Assets
# Tiles
chao_padrao = pygame.image.load(path.join(path.dirname(__file__),"Imagens\chaozinho.jpg")).convert()
chaozinho = pygame.transform.scale(chao_padrao, (200,60))

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
for l in range(len(mapa)):
    for c in range(len(mapa[l])):
        e = mapa[l][c]
        if e == "X":
            b = Bloco(chaozinho, l, c)
            all_blocos.add(b)
            all_sprites.add(b)
        if e == "P":
            player = Player(peachzinha1,peachzinhaco1, l, c)
            all_sprites.add(player)


# Looping do Game 
while game:
    clock.tick(FPS)
    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False
        keys_pressed=pygame.key.get_pressed()
        
        if keys_pressed[pygame.K_SPACE]:
            player.jumping=True
        if keys_pressed[pygame.K_LEFT]:
            player.speedx = -3
        if keys_pressed[pygame.K_RIGHT]:
            player.speedx = 3
        
    # Atualizando a posição das sprites

    all_sprites.update()

    hits = pygame.sprite.spritecollideany(player, all_blocos)
    blocos = pygame.sprite.spritecollide(player, all_blocos, False)
    print(hits)

    if hits:
        for bloco in blocos:
            if player.rect.right >= bloco.rect.left:
                player.speedx = 0
                player.rect.x -= 1
            elif player.rect.left >= bloco.rect.right:
                player.speedx = 0
                player.rect.x += 1 
            
            if player.rect.bottom <= bloco.rect.top:
                player.rect.bottom = bloco.rect.top
            elif player.rect.top >= bloco.rect.bottom:
                player.rect.top = bloco.rect.bottom
            

        
    
    window.fill((0, 200, 253))  # Preenche com a cor branca
    all_sprites.draw(window)

    pygame.display.update()
