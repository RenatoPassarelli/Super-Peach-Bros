# Imports 
import pygame
from os import path
from math import *

# Define dimensões da tela 
WIDTH = 1200
HEIGHT = 600
window = pygame.display.set_mode((WIDTH, HEIGHT))

# Inicia o pygame e o módulo de sound 
pygame.init()
pygame.mixer.init()

# Set caption 
pygame.display.set_caption('Super Peach game')

# Settings personagem 
peach_altura=460
peach_largura=200

# Settings jogo
tile_size = 60
PP=0
NN = 0 
INIT = 6
MP = 20
GAME = 8 
GO = 9 
WIN = 12 
QUIT =10  
PG=11
FPS = 60 

# Imagens dos personagens
peachzinha = pygame.image.load(path.join(path.dirname(__file__),"Imagens\Peachzinha.png"))
peachzinha1=pygame.transform.scale(peachzinha, (60,80)).convert_alpha()
peachzinhaco=pygame.image.load(path.join(path.dirname(__file__),"Imagens\Peachzinha contrária.png"))
peachzinhaco1=pygame.transform.scale(peachzinhaco, (60,80)).convert_alpha()

sonic1 = pygame.image.load(path.join(path.dirname(__file__),"Imagens\sonic.png"))
sonic=pygame.transform.scale(sonic1, (60,80)).convert_alpha()
sonico1=pygame.image.load(path.join(path.dirname(__file__),"Imagens\sonico.png"))
sonico=pygame.transform.scale(sonico1, (60,80)).convert_alpha()

yoshi1 = pygame.image.load(path.join(path.dirname(__file__),"Imagens\Yoshi.png"))
yoshi=pygame.transform.scale(yoshi1, (60,80)).convert_alpha()
yoshico1=pygame.image.load(path.join(path.dirname(__file__),"Imagens\Yoshico.png"))
yoshico=pygame.transform.scale(yoshico1, (60,80)).convert_alpha()

resina1 = pygame.image.load(path.join(path.dirname(__file__),"Imagens\lresina.png"))
resina=pygame.transform.scale(resina1, (60,80)).convert_alpha()
resinaco1=pygame.image.load(path.join(path.dirname(__file__),"Imagens\lresina_co.png"))
resinaco=pygame.transform.scale(resinaco1, (60,80)).convert_alpha()

Humberto1 = pygame.image.load(path.join(path.dirname(__file__),"Imagens\mhumberto.png"))
Humberto=pygame.transform.scale(Humberto1, (60,80)).convert_alpha()
Humbertoco1=pygame.image.load(path.join(path.dirname(__file__),"Imagens\mhumberto_co.png"))
Humbertoco=pygame.transform.scale(Humbertoco1, (60,80)).convert_alpha()

bomba1 = pygame.image.load(path.join(path.dirname(__file__),"Imagens\Bomba.png"))
bomba=pygame.transform.scale(bomba1, (60,80)).convert_alpha()
bombaco1=pygame.image.load(path.join(path.dirname(__file__),"Imagens\Bombaco.png"))
bombaco=pygame.transform.scale(bombaco1, (60,80)).convert_alpha()

# Listas com todas as imagens 
img=[peachzinha1,sonic,yoshi,resina,Humberto,bomba]
imgcont=[peachzinhaco1,sonico,yoshico,resinaco,Humbertoco,bombaco]

# Imagens dos assets 
chao_padrao = pygame.image.load(path.join(path.dirname(__file__),"Imagens\chao.png"))
chaozinho = pygame.transform.scale(chao_padrao, (60,60)).convert_alpha()

cantodd1= pygame.image.load(path.join(path.dirname(__file__),"Imagens\canto_d_deserto.jpg"))
cantodd = pygame.transform.scale(cantodd1, (60,60)).convert_alpha()

cantoed1= pygame.image.load(path.join(path.dirname(__file__),"Imagens\canto_e_deserto.png"))
cantoed = pygame.transform.scale(cantoed1, (60,60)).convert_alpha()

centrocd1= pygame.image.load(path.join(path.dirname(__file__),"Imagens\centr_cima_deserto.png"))
centrocd = pygame.transform.scale(centrocd1, (60,60)).convert_alpha()

centrodd1= pygame.image.load(path.join(path.dirname(__file__),"Imagens\centro_d_deserto.png"))
centrodd = pygame.transform.scale(centrodd1, (60,60)).convert_alpha()

centroed1= pygame.image.load(path.join(path.dirname(__file__),"Imagens\centro_e_deserto.png"))
centroed = pygame.transform.scale(centroed1, (60,60)).convert_alpha()

centrodes1= pygame.image.load(path.join(path.dirname(__file__),"Imagens\centro_deserto.png"))
centrodes = pygame.transform.scale(centrodes1, (60,60)).convert_alpha()

flutuandod1= pygame.image.load(path.join(path.dirname(__file__),"Imagens\Aflutuando_deserto.png"))
flutuandod = pygame.transform.scale(flutuandod1, (60,60)).convert_alpha()


cantoef1= pygame.image.load(path.join(path.dirname(__file__),"Imagens\Tile_01.png"))
cantoef = pygame.transform.scale(cantoef1, (60,60)).convert_alpha()

centrocf1 = pygame.image.load(path.join(path.dirname(__file__),"Imagens\Tile_02.png"))
centrocf = pygame.transform.scale(centrocf1, (60,60)).convert_alpha()

cantodf1= pygame.image.load(path.join(path.dirname(__file__),"Imagens\Tile_03.png"))
cantodf = pygame.transform.scale(cantodf1, (60,60)).convert_alpha()

centrof1= pygame.image.load(path.join(path.dirname(__file__),"Imagens\Tile_12.png"))
centrof = pygame.transform.scale(centrof1, (60,60)).convert_alpha()

centrodf1= pygame.image.load(path.join(path.dirname(__file__),"Imagens\Tile_14.png"))
centrodf = pygame.transform.scale(centrodf1, (60,60)).convert_alpha()

centroef1= pygame.image.load(path.join(path.dirname(__file__),"Imagens\Tile_16.png"))
centroef = pygame.transform.scale(centroef1, (60,60)).convert_alpha()

cantobe1= pygame.image.load(path.join(path.dirname(__file__),"Imagens\Tile_21.png"))
cantobe = pygame.transform.scale(cantobe1, (60,60)).convert_alpha()

centrobf1= pygame.image.load(path.join(path.dirname(__file__),"Imagens\Tile_22.png"))
centrobf = pygame.transform.scale(centrobf1, (60,60)).convert_alpha()

cantobe1= pygame.image.load(path.join(path.dirname(__file__),"Imagens\Tile_21.png"))
cantobe = pygame.transform.scale(cantobe1, (60,60)).convert_alpha()

suspf1= pygame.image.load(path.join(path.dirname(__file__),"Imagens\Tile_31.png"))
suspf = pygame.transform.scale(suspf1, (60,60)).convert_alpha()

cantod1 = pygame.image.load(path.join(path.dirname(__file__),"Imagens\canto direito.png"))
cantod = pygame.transform.scale(cantod1, (60,60)).convert_alpha()

cantoe1 = pygame.image.load(path.join(path.dirname(__file__),"Imagens\canto esquerdo.png"))
cantoe = pygame.transform.scale(cantoe1, (60,60)).convert_alpha()

centroc1 = pygame.image.load(path.join(path.dirname(__file__),"Imagens\centro cima.png"))
centroc = pygame.transform.scale(centroc1, (60,60)).convert_alpha()

centroe1 = pygame.image.load(path.join(path.dirname(__file__),"Imagens\centro esquerdo.png"))
centroe = pygame.transform.scale(centroe1, (60,60)).convert_alpha()

centrod1 = pygame.image.load(path.join(path.dirname(__file__),"Imagens\centro direito.png"))
centrod = pygame.transform.scale(centrod1, (60,60)).convert_alpha()

centro1 = pygame.image.load(path.join(path.dirname(__file__),"Imagens\centro.png"))
centro = pygame.transform.scale(centro1, (60,60)).convert_alpha()

gelo1 = pygame.image.load(path.join(path.dirname(__file__),"Imagens\gelo.png"))
gelo = pygame.transform.scale(gelo1, (60,60)).convert_alpha()

cantose=[cantoef,cantoed,cantoe]
cantosd=[cantodf,cantodd,cantod]
centros=[centrof,centrodes,centro]
centrosc=[centrocf,centrocd,centroc]
centrosd=[centrodf,centroed,centrod]
centrose=[centroef,centrodd,centroe]
suspen=[suspf,flutuandod,gelo]

jorre1 = pygame.image.load(path.join(path.dirname(__file__),"Imagens\jorre.png"))
jorre = pygame.transform.scale(jorre1, (60,60)).convert_alpha()

Vazio1= pygame.image.load(path.join(path.dirname(__file__),"Imagens\pngegg.png"))
Vazio=pygame.transform.scale(Vazio1, (60,60)).convert_alpha()

Gomba1=pygame.image.load(path.join(path.dirname(__file__),"Imagens\gomp.gif"))
Gomba=pygame.transform.scale(Gomba1, (60,60)).convert_alpha()

moedinha = pygame.image.load(path.join(path.dirname(__file__), "Imagens\moedinha.png"))
moedinha1 = pygame.transform.scale(moedinha, (20, 20)).convert_alpha()

nuvem1 = pygame.image.load(path.join(path.dirname(__file__),"Imagens\pngwing.com.png"))
nuvemzinha = pygame.transform.scale(nuvem1, (100,100)).convert_alpha()

veg1=pygame.image.load(path.join(path.dirname(__file__),"Imagens\9.png"))
veg = pygame.transform.scale(veg1, (100,60)).convert_alpha()

estrela1 = pygame.image.load(path.join(path.dirname(__file__),"Imagens\estrelinha_peq.png"))
estrela = pygame.transform.scale(estrela1, (40,40)) .convert_alpha()

arvore1=pygame.image.load(path.join(path.dirname(__file__),"Imagens\Arvore.png"))
arvore=pygame.transform.scale(arvore1, (125,250)).convert_alpha()

arvorep1=pygame.image.load(path.join(path.dirname(__file__),"Imagens\Arvore 1.png"))
arvorep=pygame.transform.scale(arvorep1, (125,250)).convert_alpha()

arvorem11=pygame.image.load(path.join(path.dirname(__file__),"Imagens\A1.png"))
arvorem1=pygame.transform.scale(arvorem11, (125,250)).convert_alpha()

arvorem22=pygame.image.load(path.join(path.dirname(__file__),"Imagens\A3.png"))
arvorem2=pygame.transform.scale(arvorem22, (125,250)).convert_alpha()

gelinho1=pygame.image.load(path.join(path.dirname(__file__),"Imagens\Gelinho.jpeg"))
gelinho=pygame.transform.scale(gelinho1, (60,60)).convert_alpha()

Pinheiro1=pygame.image.load(path.join(path.dirname(__file__),"Imagens\Pinherinhos_de_alegria_tralalalalalalalala.png"))
Pinheiror=pygame.transform.scale(Pinheiro1, (200,400)).convert_alpha()

Floresta1=pygame.image.load(path.join(path.dirname(__file__),"Imagens\Fundo floresta.png"))
Floresta=pygame.transform.scale(Floresta1, (1210,600)).convert_alpha()

Deserto1=pygame.image.load(path.join(path.dirname(__file__),"Imagens\Duna.png"))
Deserto=pygame.transform.scale(Deserto1, (1210,600)).convert_alpha()

Montanha1=pygame.image.load(path.join(path.dirname(__file__),"Imagens\Fundo montanha.png"))
Montanha=pygame.transform.scale(Montanha1, (1210,600)).convert_alpha()

# Carrendo sons especiais + músicas de fundo 
# pygame.mixer.music.load(path.join(path.dirname(__file__),"sounds\emafundo1.wav")) 
# pygame.mixer.music.set_volume(0) 
# pygame.mixer.music.play(loops=-1)
sons_fundo = ["sounds\Samba-Pagode.wav","sounds\emafundo1.wav", "sounds\edm_mario.wav"]
caiu_sound = pygame.mixer.Sound(path.join(path.dirname(__file__),"sounds\caiu.wav")) 
pisou_sound = pygame.mixer.Sound(path.join(path.dirname(__file__),"sounds\smb_bump.wav"))
som_moeda = pygame.mixer.Sound(path.join(path.dirname(__file__),"sounds\smb_coin.wav"))
ganhou_sound = pygame.mixer.Sound(path.join(path.dirname(__file__),"sounds\ganhou.wav"))
pulou_sound = pygame.mixer.Sound(path.join(path.dirname(__file__),"sounds\smb_jump-small.wav"))

# Fontes 
fonte_placar = pygame.font.Font(path.join(path.dirname(__file__),"font\PressStart2P.ttf" ),28)


