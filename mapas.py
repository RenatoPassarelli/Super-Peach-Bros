# CONFIGURAÇÕES GERAI
from config import tile_size
#bex 

MAPAS = {
    0: [
    '                               N      N                                                                                ',
    '              N                                  N                                                         t t t t       ',
    '                   q ta M a M a tq   N   t tMMt  M       MM t        M                                     XXXXXXXX      ',
    '          N         XXXXXXXXXXXXX     M XXXXXXXX  Mtt t  XXXX     t t                    M t M t M    MMM              ',
    '                t M      N         tXXXXXXXXXX     XXXXX         XXXXXX  t  Mt            XXXXXXXXXX   XXXXX      E     ',
    'X           MMtXXX    M  M   N  tNXXXXXXXXXXX     N          N          XXX  XX   t t X                XXXX   t t    t ',
    'X          XXXXXXX   XXXXXX  NXXXXXXXXXXXXXXX                                   XXXXXX                XXXXXXXXXXXXXXXX',
    'X                 N  XXXXXX   XXXXXXXXXXXXXXX       N              N            XXXXXX                XXXXXXXXXXXXXXXX',
    'Xttt  P        MM      XXXXXXN  XXXXXXXXXXXXXXX N                                 XXXXXX                XXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXX   XXXXXX   XXXXXXXXXXXXXXX                                   XXXXXX                XXXXXXXXXXXXXXXX'
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