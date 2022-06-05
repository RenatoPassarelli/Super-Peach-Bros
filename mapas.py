# CONFIGURAÇÕES GERAI
from config import tile_size
#bex 

MAPAS = {
    0: [
    '                                                                                                                       ',
    '                                                                                             MM                        ',
    '                   MMM                                 M                                     XXXXXXXX                  ',
    '                  XXXXXXX            XXXXXXXX         XXXX                                                             ',
    '                                   XXXXXXXXXX   XXXX        XXXXXX     M               XXXX            XXXX             ',
    'X              X                 XXXXXXXXXXXX                       XXXX  XXXXX                        XXXX             ',
    'X          XXXXXXX   XXXXXX   XXXXXXXXXXXXXXX                                   XXXXXX                 XXXXXXXXXXXXXXXX',
    'X                    XXXXXX   XXXXXXXXXXXXXXX                                   XXXXXX                 XXXXXXXXXXXXXXXX',
    'X   P        MM      XXXXXX   XXXXXXXXXXXXXXX                                   XXXXXX                 XXXXXXXXXXXXXXXX',
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