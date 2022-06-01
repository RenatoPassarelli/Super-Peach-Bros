# CONFIGURAÇÕES GERAI
from config import tile_size
#bex 

MAPAS = {
    0: [
    '                                                                                                                       ',
    '                                                                                                                       ',
    '                                                                                             XXXX                      ',
    '                  XXXXXXX            XXXXXXXX          XXX                                                             ',
    '                                   XXXXXXXXXX    XXX          XXX                     XXXX               X             ',
    '               X                 XXXXXXXXXXXX                       XXX   XXX                            X             ',
    '           XXXXXXX   XXXXXX   XXXXXXXXXXXXXXX                                   XXXXXX                 XXXXXXXXXXXXXXXX',
    ' P                   XXXXXX   XXXXXXXXXXXXXXX                                   XXXXXX                 XXXXXXXXXXXXXXXX',
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