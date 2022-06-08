# Imports 
from personagem import * 
from mapas import MAPAS
from elementos import *
from personagem import batida
from telas import *
from config import *  

# Looping do Game
game = True 
ret_x=[]
ret_m = []

state = PG
while state != QUIT:

    if state == PG: # Primeira página - inicial 
        state = Pag1(window)
        
    if state == MP: # Mapa dos níveis 
        ret_m.append(mapas_screen(window))
        n = ret_m[0][1] 
        state = ret_m[0][0]
        
    if state == INIT: # Escolhe personagem 

        # Cria os grupos de sprite 
        limite=pygame.sprite.Group()
        all_sprites = pygame.sprite.Group()
        all_blocos = pygame.sprite.Group()
        all_moedas = pygame.sprite.Group() 
        movimento_blocos=pygame.sprite.Group()
        movimento_nuvem=pygame.sprite.Group()
        a_star = pygame.sprite.GroupSingle()
        limite=pygame.sprite.Group()
        all_sprites = pygame.sprite.Group()
        all_blocos = pygame.sprite.Group()
        all_moedas = pygame.sprite.Group() 
        movimento_nuvem=pygame.sprite.Group()
        LimiteE_peach=pygame.sprite.Group()
        LimiteD_peach=pygame.sprite.Group()
        morrer=pygame.sprite.Group()

        # Define as variáveis iniciais da partida 
        ret_x.append(init_screen(window))
        personagem = ret_x[0][1]
        state = ret_x[0][0]
        player = None
        tempo = 0 
        moedas = 0 
        nivel = 0 

        # Música tema de fundo 
        backgroundsound = sons_fundo[n]
        pygame.mixer.music.load(path.join(path.dirname(__file__), backgroundsound))         
        pygame.mixer.music.play(loops=-1)
 
        mapa = MAPAS[n]
        fundo = n
        nivel = list(MAPAS.keys())[n] + 1 

        # Plota os caracteres do mapa 
        for l in range(len(mapa)):
            for c in range(len(mapa[l])):
                e = mapa[l][c]
                if e == "K":
                    a = Gelinho(gelinho, l, c)
                    all_sprites.add(a)
                    movimento_blocos.add(a)
                elif e == "t":
                    a = Arvore(arvore, l, c)
                    all_sprites.add(a)
                    movimento_blocos.add(a)
                elif e == "2":
                    a = Arvore(arvorep, l, c)
                    all_sprites.add(a)
                    movimento_blocos.add(a)
                elif e == "H":
                    a = Arvore_morta(arvorem1, l, c)
                    all_sprites.add(a)
                    movimento_blocos.add(a)
                elif e == "1":
                    a = Arvore_morta(arvorem2, l, c)
                    all_sprites.add(a)
                    movimento_blocos.add(a)
                elif e == "V":
                    a = Vegetacao(veg, l, c)
                    all_sprites.add(a)
                    movimento_blocos.add(a)
                elif e == "3":
                    a = Vegetacao(Lapide, l, c)
                    all_sprites.add(a)
                    movimento_blocos.add(a)
                elif e == "W":
                    a = Pinheiro(Pinheiror, l, c)
                    all_sprites.add(a)
                    movimento_blocos.add(a)
                elif e == "q":
                    b=Limite(Vazio,l,c)
                    limite.add(b)
                    all_sprites.add(b)
                    movimento_blocos.add(b)
                elif e == "Z":
                    b = Bloco(centros[n], l, c)
                    all_blocos.add(b)
                    all_sprites.add(b)
                    movimento_blocos.add(b)
                elif e == "C":
                    b = Bloco(centrosc[n], l, c)
                    all_blocos.add(b)
                    all_sprites.add(b)
                    movimento_blocos.add(b)
                elif e == "U":
                    b = Bloco(centrosd[n], l, c)
                    all_blocos.add(b)
                    all_sprites.add(b)
                    movimento_blocos.add(b)
                elif e == "Y":
                    b = Bloco(centrose[n], l, c)
                    all_blocos.add(b)
                    all_sprites.add(b)
                    movimento_blocos.add(b)
                elif e == "G":
                    b = Bloco(suspen[n], l, c)
                    all_blocos.add(b)
                    all_sprites.add(b)
                    movimento_blocos.add(b)
                elif e == "L":
                    b = Bloco(cantose[n], l, c)
                    all_blocos.add(b)
                    all_sprites.add(b)
                    movimento_blocos.add(b)
                elif e == "R":
                    b = Bloco(cantosd[n], l, c)
                    all_blocos.add(b)
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
                    player = Player(img,imgcont, l, c,all_blocos,personagem)
                    all_sprites.add(player)  
                elif e == 'M':
                    coin = Moedas(l, c,limite)
                    all_moedas.add(coin)
                    all_sprites.add(coin)
                    movimento_blocos.add(coin)
                elif e == 'S':
                    est = Estrela(l, c,limite)
                    all_sprites.add(est)
                    movimento_blocos.add(est)
                    a_star.add(est)    
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

        clock = pygame.time.Clock()

    elif state == GAME: # Looping principal do jogo 
        ret_x=[]
        ret_m = []
        pygame.mixer.music.set_volume(0.3)
        tempo += clock.tick_busy_loop()/100/2.8
        # pygame.time.get_ticks()/1000 mudar esse tipo de pygame.time

        clock.tick(FPS)
        # ----- Trata eventos
        for event in pygame.event.get():
            # ----- Verifica consequências: 

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
                    pulou_sound.set_volume(0.3)
                    pulou_sound.play()   
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and player.speedx>-1:
                    player.speedx = 0 
                if event.key == pygame.K_LEFT and player.speedx<-1:
                    player.speedx += 5
                if event.key == pygame.K_RIGHT and player.speedx>1:
                    player.speedx -=5
                if event.key == pygame.K_RIGHT and player.speedx<1:
                    player.speedx =0
            
        # Verifica se o player caiu da tela 
        if player.rect.y >= 600:
            pygame.mixer.music.set_volume(0) 
            caiu_sound.play() 
            time.sleep(2.5) 
            state = GO 

        # Atualizando a posição das sprites tiles 
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
        
        # Ajuste de colisão com os blocos
        bloco = pygame.sprite.spritecollide(player, all_blocos, False)
        for blocos in bloco:
            if player.speedx > 0:
                player.rect.right = blocos.rect.left-1
            elif player.speedx < 0:
                player.rect.left = blocos.rect.right+1  

        # Colisões com as moedas (colocar som)
        peg_moeda = pygame.sprite.spritecollide(player, all_moedas, True)
        for m in peg_moeda:
            pygame.mixer.music.set_volume(0) 
            som_moeda.play()
            moedas += 1 
        
        # Verifica se o player ganhou o nível 
        ganhou = pygame.sprite.spritecollide(player,a_star, True)
        for g in ganhou:
            pygame.mixer.music.set_volume(0)  
            ganhou_sound.play() 
            state = WIN 
        
        # Verifica se o player morreu colidindo com o gomba
        morrere = pygame.sprite.spritecollide(player,morrer,False,pygame.sprite.collide_mask)
        for m in morrere:
            if player.speedy>0:
                pisou_sound.play() 
                morrere = pygame.sprite.spritecollide(player,morrer,True,pygame.sprite.collide_mask)
            else:
                pygame.time.wait(1000)
                state=GO
                
        # Limita os movimentos do player na tela (esquerda e direita)
        limitee=pygame.sprite.spritecollide(player,LimiteE_peach,False)
        for l in limitee:
            player.rect.left=l.rect.right+1        
        limited=pygame.sprite.spritecollide(player,LimiteD_peach,False)
        for l in limited:
            player.rect.right=l.rect.left-1
            
        # Atualiza as sprites 
        all_sprites.update() 
        window.fill((0, 200, 253))
          # Preenche com a cor de fundo
        if fundo ==0:
            window.blit(Floresta,(0,0))
        if fundo ==1:
            window.blit(Deserto,(0,150))
        if fundo ==2:
            window.blit(Montanha,(0,0))

        all_sprites.draw(window)
        # Placar
        if n>0:
            text_tempo = fonte_placar.render("Tempo: {}".format(ceil(tempo)), True, (0,0,0))
            text_moedas = fonte_placar.render("Moedas: {}".format(moedas), True, (0,0,0))
            text_nivel = fonte_placar.render("Nível: {}".format(nivel), True, (0,0,0))
        else:
            text_tempo = fonte_placar.render("Tempo: {}".format(ceil(tempo)), True, (255,255,255))
            text_moedas = fonte_placar.render("Moedas: {}".format(moedas), True, (255,255,255))
            text_nivel = fonte_placar.render("Nível: {}".format(nivel), True, (255,255,255))
        text_moedas_rect = text_moedas.get_rect()
        text_nivel_rect = text_nivel.get_rect()
        text_tempo_rect = text_tempo.get_rect()
        text_moedas_rect.midtop = ((WIDTH/5), 15)
        text_nivel_rect.midtop = ((WIDTH/5)*2.5, 15)
        text_tempo_rect.midtop = ((WIDTH/5)*4., 15)
        window.blit(text_moedas, text_moedas_rect)
        window.blit(text_nivel, text_nivel_rect)
        window.blit(text_tempo, text_tempo_rect)

        # Atualiza o display do jogo 
        pygame.display.update()

    elif state == GO: # Game Over  
        state = game_over_screen(window)

    elif state == WIN: # Game win 
        state = win_screen(window)

    else: # Sai do jogo 
        state = QUIT
        

