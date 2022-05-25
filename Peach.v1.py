# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
from os import path
pygame.init()

# ----- Gera tela principal
window = pygame.display.set_mode((1200, 600))
pygame.display.set_caption('Super Peach game')

# ----- Inicia Assets
chao_padrao = pygame.image.load(path.join(path.dirname(__file__),"chaozinho.jpg")).convert()
chaozinho1 = pygame.transform.scale(chao_padrao, (200,60)) 
peachzinha = pygame.image.load(path.join(path.dirname(__file__),"Peachzinha.png")).convert_alpha()
peachzinha1=pygame.transform.scale(peachzinha, (60,80))
peach_altura=460
peach_largura=200
# ----- Inicia estruturas de dados



window.blit(chaozinho1, (0, 540)), 
window.blit(chaozinho1, (200, 540)),
window.blit(chaozinho1, (400, 540)), 
window.blit(chaozinho1, (600, 540)),  
window.blit(chaozinho1, (800, 540)),  
window.blit(chaozinho1, (1000, 540))

class boneco(pygame.sprite.Sprite):
    def __init__(self, img):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centerx = peach_largura / 2
        self.rect.bottom = peach_altura - 10
        self.speedx = 0

    def update(self):
        # Atualização da posição da nave
        self.rect.x += self.speedx

        # Mantem dentro da tela
        if self.rect.right > peach_largura:
            self.rect.right = peach_largura
        if self.rect.left < 0:
            self.rect.left = 0
game = True
# Variável para o ajuste de velocidade
clock = pygame.time.Clock()
FPS = 30
all_sprites = pygame.sprite.Group()
player = boneco(peachzinha1)
all_sprites.add(player)
while game:
    clock.tick(FPS)

    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False
        # Verifica se apertou alguma tecla.
        if event.type == pygame.KEYDOWN:
            # Dependendo da tecla, altera a velocidade.
            if event.key == pygame.K_LEFT:
                player.speedx -= 8
            if event.key == pygame.K_RIGHT:
                player.speedx += 8
        # Verifica se soltou alguma tecla.
        if event.type == pygame.KEYUP:
            # Dependendo da tecla, altera a velocidade.
            if event.key == pygame.K_LEFT:
                player.speedx += 8
            if event.key == pygame.K_RIGHT:
                player.speedx -= 8

    # ----- Atualiza estado do jogo
    # Atualizando a posição dos meteoros
    all_sprites.update()

    # ----- Gera saídas
    window.fill((0, 200, 253))  # Preenche com a cor branca
    window.blit(chaozinho1, (0, 540))
    window.blit(chaozinho1, (200, 540))
    window.blit(chaozinho1, (400, 540)) 
    window.blit(chaozinho1, (600, 540))  
    window.blit(chaozinho1, (800, 540))  
    window.blit(chaozinho1, (1000, 540))
    # Desenhando meteoros
    all_sprites.draw(window)

    pygame.display.update()