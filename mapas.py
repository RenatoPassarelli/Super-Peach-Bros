# Imports 
from config import tile_size

# Diretório com os mapas de cada nível do jogo 
MAPAS = {
    0: [
        '                           ',
        '                           ',
        '           XXX             ',
        '    XX                     ',
        '                  XXXXXXX  ',
        '        XXXXX              ',
        '                           ',
        '      XXXXXXXXXXXX  XXXXXXX',
        ' P XXXXXXXXXXXXXXX  XXXXXXX',
        'XXXXXXXXXXXXXXXXXX  XXXXXXX'
    ],
    1: [
    '                                N      N          N            N                                                       ',
    '               N                                  N                                                         tMtMtMt    ',
    '    N                q ta M a M atq   Nq  tatMMtq M        MMt        M                                    XXXXXXXX   ',
    '           N         XXXXXXXXXXXXX     M XXXXXXXX   tt t   XXXX   t t                    q Mat aMatq    MM             D',
    'E                t M      N         t XXXXXXXXXXX   XXXXX        XXXXX   t  Mqaq          XXXXXXXXXX   XXX        S    D',
    'E   N        MMt XX              N  XXXXXXXXXXXXX             N          XXX  X    t t X               XXXq  at ta a tqD',
    'E           XXXXXXX               tXXXXXXXXXXXXXX                                XXXXXXX               XXXXXXXXXXXXXXXXX',
    'E                  N q M a M a q  XXXXXXXXXXXXXXX                                XXXXXXX               XXXXXXXXXXXXXXXX',
    'E ttt  P        MM    XXXXXXXXX  XXXXXXXXXXXXXXXX N                              XXXXXXX               XXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXXX   XXXXXXXXX  XXXXXXXXXXXXXXXX                                XXXXXXX               XXXXXXXXXXXXXXXX'
] ,
    2: [
    '                                                                                             CCCCCCCCC                  D     ',
    '                                                      MMMMMMMMMM                             GGGGGGGGG     K    S WWWWWWD                  ',
    '                                                    GGGGGGGGGGGGGG   G   G   G        W         MMMMMMMM   LCCCCCCCCCCRWWW                      ',
    '                                                G                                     KLCRqaaaaaa MMMMMqLCCZZZZZZZZZZZZZZZ                                  ',
    '                            KW WKMM  G   G   G                                   W W LCZZZZCCCCCCCCCCCCCCZZZZZZZZZZZZZZZZZ                                    ',
    'E                          LCCCCCCR                  K  K                        LCCCZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ                                        ',
    'E                       W  YZZZZZZU                LCCCCR                       YZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ                                           ',
    'E            q aKWMKMq LCCCZZZZZZZU                 YZZZZRq KKaaaq               YZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ                                          ',
    'EqK PKaMM a q LCCCCCR  YZZZZZZZZZZU                 YZZZZZCCCCCCR      G  G   G  YZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ                                        ',
    'ELCCCCCCCCCR  YZZZZZU  YZZZZZZZZZZU                 YZZZZZZZZZZZZCCR G G  G   G  YZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ                                         ',
] 
}
