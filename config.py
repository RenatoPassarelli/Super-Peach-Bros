import pygame
from os import path
from math import *



jan_largura = 1200
jan_altura=600
pygame.init()
pygame.mixer.init()
window = pygame.display.set_mode((jan_largura, jan_altura))
pygame.display.set_caption('Super Peach game')
# Tamanho da tela
WIDTH = 1200
HEIGHT = 600

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
QUIT =10  
PG=11
FPS = 60 
# Personagem 

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

img=[peachzinha1,sonic,yoshi,resina,Humberto,bomba]
imgcont=[peachzinhaco1,sonico,yoshico,resinaco,Humbertoco,bombaco]

chao_padrao = pygame.image.load(path.join(path.dirname(__file__),"Imagens\chao.png"))
chaozinho = pygame.transform.scale(chao_padrao, (60,60)).convert_alpha()
jorre1 = pygame.image.load(path.join(path.dirname(__file__),"Imagens\jorre.png"))
jorre = pygame.transform.scale(jorre1, (60,60)).convert_alpha()

Vazio1= pygame.image.load(path.join(path.dirname(__file__),"Imagens\pngegg.png"))
Vazio=pygame.transform.scale(Vazio1, (60,60)).convert_alpha()

Gomba1=pygame.image.load(path.join(path.dirname(__file__),"Imagens\gomp.gif"))
Gomba=pygame.transform.scale(Gomba1, (60,60)).convert_alpha()

moedinha = pygame.image.load(path.join(path.dirname(__file__), "Imagens\moedinha.png"))
moedinha1 = pygame.transform.scale(moedinha, (40, 40)).convert_alpha()

nuvem1 = pygame.image.load(path.join(path.dirname(__file__),"Imagens\pngwing.com.png"))
nuvemzinha = pygame.transform.scale(nuvem1, (100,100)).convert_alpha()

estrela1 = pygame.image.load(path.join(path.dirname(__file__),"Imagens\estrelinha_peq.png"))
estrela = pygame.transform.scale(estrela1, (40,40)) .convert_alpha()

arvore1=pygame.image.load(path.join(path.dirname(__file__),"Imagens\Arvore.png"))
arvore=pygame.transform.scale(arvore1, (125,250)).convert_alpha()

Deserto1=pygame.image.load(path.join(path.dirname(__file__),"Imagens\Duna.png"))
Deserto=pygame.transform.scale(Deserto1, (1210,600)).convert_alpha()


pygame.mixer.music.load(path.join(path.dirname(__file__),"sounds\emafundo1.wav")) 
pygame.mixer.music.set_volume(0) 
pygame.mixer.music.play(loops=-1)
caiu_sound = pygame.mixer.Sound(path.join(path.dirname(__file__),"sounds\caiu.wav")) 
pisou_sound = pygame.mixer.Sound(path.join(path.dirname(__file__),"sounds\smb_bump.wav"))
som_moeda = pygame.mixer.Sound(path.join(path.dirname(__file__),"sounds\smb_coin.wav"))

fonte_placar = pygame.font.Font(path.join(path.dirname(__file__),"font\PressStart2P.ttf" ),28)

limite=pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_blocos = pygame.sprite.Group()
all_moedas = pygame.sprite.Group() 
movimento_blocos=pygame.sprite.Group()
movimento_nuvem=pygame.sprite.Group()
a_star = pygame.sprite.GroupSingle()
player = None
ret_x=[]
ret_m = []
limite=pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_blocos = pygame.sprite.Group()
all_moedas = pygame.sprite.Group() 
movimento_nuvem=pygame.sprite.Group()
LimiteE_peach=pygame.sprite.Group()
LimiteD_peach=pygame.sprite.Group()
morrer=pygame.sprite.Group()
