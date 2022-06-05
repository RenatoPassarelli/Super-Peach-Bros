# CONFIGURAÇÕES GERAI
from config import tile_size
#bex 

MAPAS = {
    0: [
    '                               N                                                                                      ',
    '              N                                  N                                             MM                        ',
    '                  q  a M a M a  q                                  M                                     XXXXXXXX                  ',
    '          N         XXXXXXXXXXXXX       XXXXXXXX         XXXX                                                             ',
    '                        N          XXXXXXXXXX   XXXX        XXXXXX     M               XXXX            XXXX             ',
    'X              XXX               NXXXXXXXXXXXX    N          N         XXXX  XXXXX                        XXXX             ',
    'X          XXXXXXX   XXXXXX  NXXXXXXXXXXXXXXX                                   XXXXXX                 XXXXXXXXXXXXXXXX',
    'X                    XXXXXX   XXXXXXXXXXXXXXX       N              N            XXXXXX                 XXXXXXXXXXXXXXXX',
    'X   P        MM      XXXXXX   XXXXXXXXXXXXXXX N                                 XXXXXX                 XXXXXXXXXXXXXXXX',
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