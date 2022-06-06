# CONFIGURAÇÕES GERAI
from config import tile_size
#bex 

MAPAS = {
    0: [
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
    1: [
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
    2: [
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
    ]
}
jan_largura = 1200
jan_altura = len(MAPAS[0])*tile_size