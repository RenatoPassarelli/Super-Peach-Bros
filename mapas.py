# CONFIGURAÇÕES GERAI
from config import tile_size
#bex 

MAPAS = {
    0: [
    '                               N      N                                                                                ',
    '              N                                  N                                             MM                      ',
    '                  q  a M a M a  q   N                              M                                     XXXXXXXX      ',
    '          N         XXXXXXXXXXXXX       XXXXXXXX         XXXX                                                          ',
    '                        N          XXXXXXXXXX    XXXXX      XXXXXX     M              XXXXXXXXXXXXX   XXXXX      E     ',
    'X              XXX          N    NXXXXXXXXXXX     N          N         XXXX  XXXXX                        XXXX         ',
    'X          XXXXXXX   XXXXXX  NXXXXXXXXXXXXXXX                                   XXXXXX                 XXXXXXXXXXXXXXXX',
    'X                 N  XXXXXX   XXXXXXXXXXXXXXX       N              N            XXXXXX                 XXXXXXXXXXXXXXXX',
    'X   P        MM      XXXXXXN  XXXXXXXXXXXXXXX N                                 XXXXXX                 XXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXX   XXXXXX   XXXXXXXXXXXXXXX                                   XXXXXX                 XXXXXXXXXXXXXXXX'
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