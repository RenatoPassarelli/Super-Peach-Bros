# ===== Inicialização =====
# ----- Importa e inicia pacotes
from pickle import TRUE
import pygame
from math import * 
from os import path
from config import * 
from personagem import * 
from mapas import MAPAS, jan_altura, jan_largura
from elementos import *
from personagem import batida
from telas import * 


pygame.init()
pygame.mixer.init() 
# ----- Gera tela principal
window = pygame.display.set_mode((jan_largura, jan_altura))
pygame.display.set_caption('Super Peach game')
# ----- Settings Placar / escritos 
fonte_placar = pygame.font.Font(path.join(path.dirname(__file__),"font\PressStart2P.ttf" ),28) 

# ----- Inicia Assets
# Tiles
chao_padrao = pygame.image.load(path.join(path.dirname(__file__),"Imagens\chao.png")).convert_alpha()
chaozinho = pygame.transform.scale(chao_padrao, (60,60))
jorre1 = pygame.image.load(path.join(path.dirname(__file__),"Imagens\jorre.png")).convert_alpha()
jorre = pygame.transform.scale(jorre1, (60,60))
Vazio1= pygame.image.load(path.join(path.dirname(__file__),"Imagens\pngegg.png")).convert_alpha()
Vazio=pygame.transform.scale(Vazio1, (60,60))
# Personagem 
peachzinha = pygame.image.load(path.join(path.dirname(__file__),"Imagens\Peachzinha.png")).convert_alpha()
peachzinha1=pygame.transform.scale(peachzinha, (60,80))
peachzinhaco=pygame.image.load(path.join(path.dirname(__file__),"Imagens\Peachzinha contrária.png")).convert_alpha()
peachzinhaco1=pygame.transform.scale(peachzinhaco, (60,80))
Gomba1=pygame.image.load(path.join(path.dirname(__file__),"Imagens\gomp.gif")).convert_alpha()
Gomba=pygame.transform.scale(Gomba1, (60,60))
caiu_sound = pygame.mixer.Sound(path.join(path.dirname(__file__),"sounds\caiu.wav")) 
pisou_sound = pygame.mixer.Sound(path.join(path.dirname(__file__),"sounds\smb_bump.wav"))
# Moedinhas
moedinha = pygame.image.load(path.join(path.dirname(__file__), "Imagens\moedinha.png")).convert_alpha()
moedinha1 = pygame.transform.scale(moedinha, (40, 40))
som_moeda = pygame.mixer.Sound(path.join(path.dirname(__file__),"sounds\smb_coin.wav"))
# Nuvem 
nuvem1 = pygame.image.load(path.join(path.dirname(__file__),"Imagens\pngwing.com.png")).convert_alpha()
nuvemzinha = pygame.transform.scale(nuvem1, (100,100))
# Estrelinha 
estrela1 = pygame.image.load(path.join(path.dirname(__file__),"Imagens\estrelinha_peq.png")).convert_alpha()
estrela = pygame.transform.scale(estrela1, (40,40)) 
#Árvore
arvore1=pygame.image.load(path.join(path.dirname(__file__),"Imagens\Arvore.png")).convert_alpha()
arvore=pygame.transform.scale(arvore1, (125,250))
Deserto1=pygame.image.load(path.join(path.dirname(__file__),"Imagens\Duna.png")).convert_alpha()
Deserto=pygame.transform.scale(Deserto1, (1210,600))
game = True


# Variável para o ajuste de velocidade

limite=pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_blocos = pygame.sprite.Group()
all_moedas = pygame.sprite.Group() 
movimento_blocos=pygame.sprite.Group()
movimento_nuvem=pygame.sprite.Group()
player = None
         
pygame.mixer.music.load(path.join(path.dirname(__file__),"sounds\emafundo1.wav")) 
pygame.mixer.music.set_volume(0) 
            
pygame.mixer.music.play(loops=-1)
# Looping do Game 

state = INIT
while state != QUIT:
    if state == INIT:
        state = init_screen(window)
        clock = pygame.time.Clock()
        limite=pygame.sprite.Group()
        all_sprites = pygame.sprite.Group()
        all_blocos = pygame.sprite.Group()
        all_moedas = pygame.sprite.Group() 
        movimento_nuvem=pygame.sprite.Group()
        LimiteE_peach=pygame.sprite.Group()
        LimiteD_peach=pygame.sprite.Group()
        morrer=pygame.sprite.Group()
        player = None
        tempo = 0 
        moedas = 0 
        nivel = 0 
        
        pygame.mixer.music.load(path.join(path.dirname(__file__),"sounds\emafundo1.wav")) 
        pygame.mixer.music.set_volume(0) 
                    
        pygame.mixer.music.play(loops=-1)
        # Looping do Game 
        mapa = MAPAS[0]
        nivel = list(MAPAS.keys())[0] + 1 

        for l in range(len(mapa)):
            for c in range(len(mapa[l])):
                e = mapa[l][c]
                if e == "t":
                    a = Arvore(arvore, l, c)
                    all_sprites.add(a)
                    movimento_blocos.add(a)
                elif e == "q":
                    b=Limite(Vazio,l,c)
                    limite.add(b)
                    all_sprites.add(b)
                    movimento_blocos.add(b)
                elif e == "X":
                    b = Bloco(chaozinho, l, c)
                    all_blocos.add(b)
                    all_sprites.add(b)
                    movimento_blocos.add(b)
                elif e == "J":
                    b = Jorre(jorre, l, c)
                    all_blocos.add(b)
                    all_sprites.add(b)
                    movimento_blocos.add(b)
                elif e == "P":
                    player = Player(peachzinha1,peachzinhaco1, l, c,all_blocos)
                    all_sprites.add(player)
                    
                elif e == 'M':
                    coin = Moedas(moedinha1, l, c)
                    all_moedas.add(coin)
                    all_sprites.add(coin)
                    movimento_blocos.add(coin)
                elif e == 'S':
                    est = Estrela(estrela, l, c)
                    all_sprites.add(est)
                    movimento_blocos.add(est)    
                elif e == 'N':
                    cloud = Nuvem(nuvemzinha, l, c)
                    all_sprites.add(cloud)
                    movimento_nuvem.add(cloud)
                elif e == "a":
                    g = Animais(l, c,limite)
                    all_sprites.add(g)
                    movimento_blocos.add(g)
                    morrer.add(g)
                elif e == "E":
                    a = LimiteE(Vazio, l, c)
                    all_sprites.add(a)
                    movimento_blocos.add(a)
                    LimiteE_peach.add(a)

                elif e == "D":
                    a = LimiteD(Vazio, l, c)
                    all_sprites.add(a)
                    movimento_blocos.add(a)
                    LimiteD_peach.add(a)
                

    elif state == GAME:
        pygame.mixer.music.set_volume(0.3)
        tempo += clock.tick_busy_loop()/100/2.8
        # pygame.time.get_ticks()/1000 mudar esse tipo de pygame.time

        clock.tick(FPS)
        # ----- Trata eventos
        for event in pygame.event.get():
            # ----- Verifica consequências
            # ----- Se é para sair do jogo
            if event.type == pygame.QUIT:
                state = QUIT 
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
            
        # Atualizando a posição das sprites tiles 
        if player.rect.y >= 600:
            caiu_sound.play() 
            time.sleep(2.5) 
            state = GO 

        if player.rect.x < WIDTH/8 and player.speedx < 0: 
            for bloco in movimento_blocos:
                bloco.rect.x += 5
                player.speedx = -0.0001

        if player.rect.x > WIDTH/2 and player.speedx > 0: 
            for bloco in movimento_blocos:
                bloco.rect.x -= 5
                player.speedx = 0.0001

        # Movimento das nuvens
        if player.rect.x > WIDTH/2 and player.speedx > 0: 
            for bloco in movimento_nuvem:
                bloco.rect.x -= 1
        
        bloco = pygame.sprite.spritecollide(player, all_blocos, False)
        for blocos in bloco:
            if player.speedx > 0:
                player.rect.right = blocos.rect.left-1
            elif player.speedx < 0:
                player.rect.left = blocos.rect.right+1
                
        
        #print(player.speedx)

        # Colisões com as moedas (colocar som)
        peg_moeda = pygame.sprite.spritecollide(player, all_moedas, True)
        for m in peg_moeda:
            som_moeda.play()
            moedas += 1 
        
        morrere = pygame.sprite.spritecollide(player,morrer,False,pygame.sprite.collide_mask)
        for m in morrere:
            if player.speedy>0:
                pisou_sound.play() 
                morrere = pygame.sprite.spritecollide(player,morrer,True,pygame.sprite.collide_mask)
            else:
                pygame.time.wait(1000)
                state=GO
                
            #pygame.time.wait(1000)
            #state= GO

        limitee=pygame.sprite.spritecollide(player,LimiteE_peach,False)
        for l in limitee:
            
            player.rect.left=l.rect.right+1
                
        limited=pygame.sprite.spritecollide(player,LimiteD_peach,False)
        for l in limited:
            player.rect.right=l.rect.left-1
            

        all_sprites.update() 
        window.fill((0, 200, 253))  # Preenche com a cor de fundo
        window.blit(Deserto,(0,150))
        all_sprites.draw(window)

        # Placar
        text_tempo = fonte_placar.render("Tempo: {}".format(ceil(tempo)), True, (0,0,0))
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

    elif state == GO:
        state = game_over_screen(window)
    
    else:
        state = QUIT
        

