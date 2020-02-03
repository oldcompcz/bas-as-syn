# coding: utf-8

# Colors for syntax highlighting

COLORS = {
    'line_number': '#35f',
    'keyword': '#1cc',
    'operator': '#188',
    'identifier': '#ddd',
    'dec': '#e4e',
    'hex': '#1e1',
    'str': '#e81',
    'data': '#ee1',
    'comment': '#777',
    'separator': '#555',
    'special': '#f22'
}

# MZ-1Z013 (700 Basic) tokens
# https://original.sharpmz.org/mz-700/basoverv.htm

TOKENS_700 = {
    0x80: 'GOTO',
    0x81: 'GOSUB',
    0x83: 'RUN',
    0x84: 'RETURN',
    0x85: 'RESTORE',
    0x86: 'RESUME',
    0x87: 'LIST',
    0x89: 'DELETE',
    0x8a: 'RENUM',
    0x8b: 'AUTO',
    0x8d: 'FOR',
    0x8e: 'NEXT',
    0x8f: 'PRINT',
    0x91: 'INPUT',
    0x93: 'IF',
    0x94: 'DATA',
    0x95: 'READ',
    0x96: 'DIM',
    0x97: 'REM',
    0x98: 'END',
    0x99: 'STOP',
    0x9a: 'CONT',
    0x9b: 'CLS',
    0x9d: 'ON',
    0x9e: 'LET',
    0x9f: 'NEW',
    0xa0: 'POKE',
    0xa1: 'OFF',
    0xa2: 'MODE',
    0xa3: 'SKIP',
    0xa4: 'PLOT',
    0xa5: 'LINE',
    0xa6: 'RLINE',
    0xa7: 'MOVE',
    0xa8: 'RMOVE',
    0xa9: 'TRON',
    0xaa: 'TROFF',
    0xab: 'INP#',
    0xad: 'GET',
    0xae: 'PCOLOR',
    0xaf: 'PHOME',
    0xb0: 'HSET',
    0xb1: 'GPRINT',
    0xb2: 'KEY',
    0xb3: 'AXIS',
    0xb4: 'LOAD',
    0xb5: 'SAVE',
    0xb6: 'MERGE',
    0xb8: 'CONSOLE',
    0xba: 'OUT#',
    0xbb: 'CIRCLE',
    0xbc: 'TEST',
    0xbd: 'PAGE',
    0xc0: 'ERASE',
    0xc1: 'ERROR',
    0xc3: 'USR',
    0xc4: 'BYE',
    0xc7: 'DEF',
    0xce: 'WOPEN',
    0xcf: 'CLOSE',
    0xd0: 'ROPEN',
    0xd9: 'KILL',
    0xe0: 'TO',
    0xe1: 'STEP',
    0xe2: 'THEN',
    0xe3: 'USING',
    0xe4: 'π',
    0xe6: 'TAB',
    0xe7: 'SPC',
    0xeb: 'OR',
    0xec: 'AND',
    0xee: '><',
    0xef: '<>',
    0xf0: '=<',
    0xf1: '<=',
    0xf2: '=>',
    0xf3: '>=',
    0xf4: '=',
    0xf5: '>',
    0xf6: '<',
    0xf7: '+',
    0xf8: '-',
    0xfb: '/',
    0xfc: '*',
    0xfd: '^',
}

PREFIXED_700 = {
    0xfe: {
        0x81: 'SET',
        0x82: 'RESET',
        0x83: 'COLOR',
        0xa2: 'MUSIC',
        0xa3: 'TEMPO',
        0xa4: 'CURSOR',
        0xa5: 'VERIFY',
        0xa6: 'CLR',
        0xa7: 'LIMIT',
        0xae: 'BOOT',
    },
    0xff: {
        0x80: 'INT',
        0x81: 'ABS',
        0x82: 'SIN',
        0x83: 'COS',
        0x84: 'TAN',
        0x85: 'LN',
        0x86: 'EXP',
        0x87: 'SQR',
        0x88: 'RND',
        0x89: 'PEEK',
        0x8a: 'ATN',
        0x8b: 'SGN',
        0x8c: 'LOG',
        0x8e: 'PAI',
        0x8f: 'RAD',
        0x95: 'EOF',
        0x9e: 'JOY',
        0xa0: 'CHR$',
        0xa1: 'STR$',
        0xa2: 'HEX$',
        0xab: 'ASC',
        0xac: 'LEN',
        0xad: 'VAL',
        0xb3: 'ERN',
        0xb4: 'ERL',
        0xb5: 'SIZE',
        0xba: 'LEFT$',
        0xbb: 'RIGHT$',
        0xbc: 'MID$',
        0xc3: 'STRING$',
        0xc4: 'TI$',
        0xc7: 'FN',
    }
}

# MZ-1Z016 (800 Basic) tokens
# https://original.sharpmz.org/mz-800/1z016ovv.htm

TOKENS_800 = {
    0x80: 'GOTO',
    0x81: 'GOSUB',
    0x83: 'RUN',
    0x84: 'RETURN',
    0x85: 'RESTORE',
    0x86: 'RESUME',
    0x87: 'LIST',
    0x89: 'DELETE',
    0x8a: 'RENUM',
    0x8b: 'AUTO',
    0x8c: 'EDIT',
    0x8d: 'FOR',
    0x8e: 'NEXT',
    0x8f: 'PRINT',
    0x91: 'INPUT',
    0x93: 'IF',
    0x94: 'DATA',
    0x95: 'READ',
    0x96: 'DIM',
    0x97: 'REM',
    0x98: 'END',
    0x99: 'STOP',
    0x9a: 'CONT',
    0x9b: 'CLS',
    0x9d: 'ON',
    0x9e: 'LET',
    0x9f: 'NEW',
    0xa0: 'POKE',
    0xa1: 'OFF',
    0xa2: 'PMODE',
    0xa3: 'PSKIP',
    0xa4: 'PLOT',
    0xa5: 'PLINE',
    0xa6: 'RLINE',
    0xa7: 'PMOVE',
    0xa8: 'RMOVE',
    0xa9: 'TRON',
    0xaa: 'TROFF',
    0xab: 'INP@',
    0xac: 'DEFAULT',
    0xad: 'GET',
    0xae: 'PCOLOR',
    0xaf: 'PHOME',
    0xb0: 'HSET',
    0xb1: 'GPRINT',
    0xb2: 'KEY',
    0xb3: 'AXIS',
    0xb4: 'LOAD',
    0xb5: 'SAVE',
    0xb6: 'MERGE',
    0xb7: 'CHAIN',
    0xb8: 'CONSOLE',
    0xb9: 'SEARCH',
    0xba: 'OUT@',
    0xbb: 'PCIRCLE',
    0xbc: 'PTEST',
    0xbd: 'PAGE',
    0xbe: 'WAIT',
    0xbf: 'SWAP',
    0xc1: 'ERROR',
    0xc2: 'ELSE',
    0xc3: 'USR',
    0xc4: 'BYE',
    0xc7: 'DEF',
    0xca: 'LABEL',
    0xce: 'WOPEN',
    0xcf: 'CLOSE',
    0xd0: 'ROPEN',
    0xd1: 'XOPEN',
    0xd5: 'DIR',
    0xd8: 'RENAME',
    0xd9: 'KILL',
    0xda: 'LOCK',
    0xdb: 'UNLOCK',
    0xdc: 'INIT',
    0xe0: 'TO',
    0xe1: 'STEP',
    0xe2: 'THEN',
    0xe3: 'USING',
    0xe4: 'π',
    0xe5: 'ALL',
    0xe6: 'TAB',
    0xe7: 'SPC',
    0xea: 'XOR',
    0xeb: 'OR',
    0xec: 'AND',
    0xed: 'NOT',
    0xee: '><',
    0xef: '<>',
    0xf0: '=<',
    0xf1: '<=',
    0xf2: '=>',
    0xf3: '>=',
    0xf4: '=',
    0xf5: '>',
    0xf6: '<',
    0xf7: '+',
    0xf8: '-',
    0xf9: '⫽',
    0xfa: 'MOD',
    0xfb: '/',
    0xfc: '*',
    0xfd: '↑',
}

PREFIXED_800 = {
    0xfe: {
        0x81: 'CSET',
        0x82: 'CRESET',
        0x83: 'CCOLOR',
        0x8a: 'SOUND',
        0x8c: 'NOISE',
        0x8d: 'BEEP',
        0x90: 'COLOR',
        0x92: 'SET',
        0x93: 'RESET',
        0x94: 'LINE',
        0x95: 'BLINE',
        0x96: 'PAL',
        0x97: 'CIRCLE',
        0x98: 'BOX',
        0x99: 'PAINT',
        0x9a: 'POSITION',
        0x9b: 'PATTERN',
        0x9c: 'HCOPY',
        0xa0: 'SYMBOL',
        0xa2: 'MUSIC',
        0xa3: 'TEMPO',
        0xa4: 'CURSOR',
        0xa5: 'VERIFY',
        0xa6: 'CLR',
        0xa7: 'LIMIT',
        0xae: 'BOOT',
    },
    0xff: {
        0x80: 'INT',
        0x81: 'ABS',
        0x82: 'SIN',
        0x83: 'COS',
        0x84: 'TAN',
        0x85: 'LN',
        0x86: 'EXP',
        0x87: 'SQR',
        0x88: 'RND',
        0x89: 'PEEK',
        0x8a: 'ATN',
        0x8b: 'SGN',
        0x8c: 'LOG',
        0x8d: 'FRAC',
        0x8e: 'PAI',
        0x8f: 'RAD',
        0x9c: 'STICK',
        0x9d: 'STRIG',
        0xa0: 'CHR$',
        0xa1: 'STR$',
        0xa2: 'HEX$',
        0xa8: 'SPACE$',
        0xab: 'ASC',
        0xac: 'LEN',
        0xad: 'VAL',
        0xb3: 'ERN',
        0xb4: 'ERL',
        0xb5: 'SIZE',
        0xb6: 'CSRH',
        0xb7: 'CSRV',
        0xb8: 'POSH',
        0xb9: 'POSV',
        0xba: 'LEFT$',
        0xbb: 'RIGHT$',
        0xbc: 'MID$',
        0xc4: 'TI$',
        0xc5: 'POINT',
        0xc6: 'EOF',
        0xc7: 'FN',
    }
}

# Lowercase letters, pseudo-graphics and other characters with codes
# different from ASCII

OTHER = {
    0x11: '⇓',    # \u21d3 DOWNWARDS DOUBLE ARROW
    0x12: '⇑',    # \u21d1 UPWARDS DOUBLE ARROW
    0x13: '⇒',    # \u21d2 RIGHTWARDS DOUBLE ARROW
    0x14: '⇐',    # \u21d0 LEFTWARDS DOUBLE ARROW
    0x15: 'ℍ',    # \u210d DOUBLE-STRUCK CAPITAL H
                  # 🅷 \U0001f177, Ⓗ \u24bd
    0x16: 'ℂ',    # \u2102 DOUBLE-STRUCK CAPITAL C
                  # 🅲 \U0001f172, Ⓒ \u24b8
    0x5e: '↑',    # \u2191 UPWARDS ARROW
                  #        see also power operator TOKENS[0xfd]
                  #        see also OTHER[0x8b]
    0x5f: '←',    # \u2190 LEFTWARDS ARROW
    0x63: '⛹',    # \u26f9 PERSON WITH BALL
                  # 🧍 \U0001F9CD, 🚹 \U0001F6B9
    0x67: '☻',    # \u263b BLACK SMILING FACE
    0x68: '☺',    # \u263a WHITE SMILING FACE
    # 0x69: '🐍',    # \U0001f40d SNAKE
    0x6e: '⟛',    # \u27db LEFT AND RIGHT TACK
    0x70: '▒',    # \u2592 MEDIUM SHADE
    0x7b: '°',    # \u00b0 DEGREE SIGN
    0x7c: '░',    # \u2591 LIGHT SHADE
    0x7d: '⫽',    # \u2afd DOUBLE SOLIDUS OPERATOR
                  #        see also integer division operator TOKENS[0xf9]
    0x7f: '⍗',    # \u2357 APL FUNCTIONAL SYMBOL QUAD DOWNWARDS ARROW
    0x80: '}',    # \u007d RIGHT CURLY BRACKET
    0x81: '┼',    # \u253c BOX DRAWINGS LIGHT VERTICAL AND HORIZONTAL
    0x86: '⎝',    # \u239d LEFT PARENTHESIS LOWER HOOK
    0x8b: '^',    # \u005e CIRCUMFLEX ACCENT
                  #        see also OTHER[0x5e]
    0x8d: '⎞',    # \u239e RIGHT PARENTHESIS UPPER HOOK
    0x8e: '⎠',    # \u23a0 RIGHT PARENTHESIS LOWER HOOK
    0x90: '_',    # \u005f LOW LINE
    0x91: '╬',    # \u256c BOX DRAWINGS DOUBLE VERTICAL AND HORIZONTAL
                  # previously '⌗' \u2317 VIEWDATA SQUARE
    0x92: 'e',    # \u0065 LATIN SMALL LETTER E
    0x93: '`',    # \u0060 GRAVE ACCENT
    0x94: '~',    # \u007e TILDE
    0x95: '▩',    # \u25a9 SQUARE WITH DIAGONAL CROSSHATCH FILL
    0x96: 't',    # \u0074 LATIN SMALL LETTER T
    0x97: 'g',    # \u0067 LATIN SMALL LETTER G
    0x98: 'h',    # \u0068 LATIN SMALL LETTER H
    0x9a: 'b',    # \u0062 LATIN SMALL LETTER B
    0x9b: 'x',    # \u0078 LATIN SMALL LETTER X
    0x9c: 'd',    # \u0064 LATIN SMALL LETTER D
    0x9d: 'r',    # \u0072 LATIN SMALL LETTER R
    0x9e: 'p',    # \u0070 LATIN SMALL LETTER P
    0x9f: 'c',    # \u0063 LATIN SMALL LETTER C
    0xa0: 'q',    # \u0071 LATIN SMALL LETTER Q
    0xa1: 'a',    # \u0061 LATIN SMALL LETTER A
    0xa2: 'z',    # \u007a LATIN SMALL LETTER Z
    0xa3: 'w',    # \u0077 LATIN SMALL LETTER W
    0xa4: 's',    # \u0073 LATIN SMALL LETTER S
    0xa5: 'u',    # \u0075 LATIN SMALL LETTER U
    0xa6: 'i',    # \u0069 LATIN SMALL LETTER I
    0xa7: '═',    # \u2550 BOX DRAWINGS DOUBLE HORIZONTAL
    0xa8: 'Ö',    # \u00d6 LATIN CAPITAL LETTER O WITH DIAERESIS
    0xa9: 'k',    # \u006b LATIN SMALL LETTER K
    0xaa: 'f',    # \u0066 LATIN SMALL LETTER F
    0xab: 'v',    # \u0076 LATIN SMALL LETTER V
    0xac: '║',    # \u2551 BOX DRAWINGS DOUBLE VERTICAL
    0xad: 'ü',    # \u00fc LATIN SMALL LETTER U WITH DIAERESIS
    0xae: 'ß',    # \u00df LATIN SMALL LETTER SHARP S
    0xaf: 'j',    # \u006a LATIN SMALL LETTER J
    0xb0: 'n',    # \u006e LATIN SMALL LETTER N
    0xb1: '⎛',    # \u239b LEFT PARENTHESIS UPPER HOOK
    0xb2: 'Ü',    # \u00dc LATIN CAPITAL LETTER U WITH DIAERESIS
    0xb3: 'm',    # \u006d LATIN SMALL LETTER M
    0xb7: 'o',    # \u006f LATIN SMALL LETTER O
    0xb8: 'l',    # \u006c LATIN SMALL LETTER L
    0xb9: 'Ä',    # \u00c4 LATIN CAPITAL LETTER A WITH DIAERESIS
    0xba: 'ö',    # \u00f6 LATIN SMALL LETTER O WITH DIAERESIS
    0xbb: 'ä',    # \u00e4 LATIN SMALL LETTER A WITH DIAERESIS
    0xbd: 'y',    # \u0079 LATIN SMALL LETTER Y
    0xbe: '{',    # \u007b LEFT CURLY BRACKET
    0xc0: '|',    # \u007c VERTICAL LINE
    0xc1: '▐',    # \u2590 RIGHT HALF BLOCK
    0xc2: '▄',    # \u2584 LOWER HALF BLOCK
    0xc3: '▔',    # \u2594 UPPER ONE EIGHTH BLOCK
    0xc4: '▁',    # \u2581 LOWER ONE EIGHTH BLOCK
    0xc5: '▏',    # \u258f LEFT ONE EIGHTH BLOCK
    0xc6: '→',    # \u2192 RIGHTWARDS ARROW
    0xc7: '▕',    # \u2595 RIGHT ONE EIGHTH BLOCK
    0xc8: '█',    # \u2588 FULL BLOCK
    0xc9: '◤',    # \u25e4 BLACK UPPER LEFT TRIANGLE
    0xcb: '├',    # \u251c BOX DRAWINGS LIGHT VERTICAL AND RIGHT
    0xcc: '⌼',    # \u233c APL FUNCTIONAL SYMBOL QUAD CIRCLE
                  # ◙ \u25d9
    0xcd: '└',    # \u2514 BOX DRAWINGS LIGHT UP AND RIGHT
    0xce: '┐',    # \u2510 BOX DRAWINGS LIGHT DOWN AND LEFT
    0xcf: '▂',    # \u2582 LOWER ONE QUARTER BLOCK
    0xd0: '┌',    # \u250c BOX DRAWINGS LIGHT DOWN AND RIGHT
    0xd1: '┴',    # \u2534 BOX DRAWINGS LIGHT UP AND HORIZONTAL
    0xd2: '┬',    # \u252c BOX DRAWINGS LIGHT DOWN AND HORIZONTAL
    0xd3: '┤',    # \u2524 BOX DRAWINGS LIGHT VERTICAL AND LEFT
    0xd4: '▎',    # \u258e LEFT ONE QUARTER BLOCK
    0xd5: '▌',    # \u258c LEFT HALF BLOCK
    0xd8: '▀',    # \u2580 UPPER HALF BLOCK
    0xd9: '▃',    # \u2583 LOWER THREE EIGHTHS BLOCK
    0xda: '⏌',    # \u23cc DENTISTRY SYMBOL LIGHT VERTICAL AND BOTTOM LEFT
    0xdb: '╭',    # \u256d BOX DRAWINGS LIGHT ARC DOWN AND RIGHT
    0xdc: '╮',    # \u256e BOX DRAWINGS LIGHT ARC DOWN AND LEFT
    0xdd: '┘',    # \u2518 BOX DRAWINGS LIGHT UP AND LEFT
    0xde: '▞',    # \u259e QUADRANT UPPER RIGHT AND LOWER LEFT
    0xdf: '▚',    # \u259a QUADRANT UPPER LEFT AND LOWER RIGHT
    0xe0: '─',    # \u2500 BOX DRAWINGS LIGHT HORIZONTAL
    0xe1: '♠',    # \u2660 BLACK SPADE SUIT
    0xe9: '◣',    # \u25e3 BLACK LOWER LEFT TRIANGLE
    0xea: '╰',    # \u2570 BOX DRAWINGS LIGHT ARC UP AND RIGHT
    0xeb: '╯',    # \u256f BOX DRAWINGS LIGHT ARC UP AND LEFT
    0xec: '⎿',    # \u23bf DENTISTRY SYMBOL LIGHT VERTICAL AND BOTTOM RIGHT
    0xed: '╲',    # \u2572 BOX DRAWINGS LIGHT DIAGONAL UPPER LEFT TO LOWER RIGHT
    0xee: '╱',    # \u2571 BOX DRAWINGS LIGHT DIAGONAL UPPER RIGHT TO LOWER LEFT
    0xef: '⎾',    # \u23be DENTISTRY SYMBOL LIGHT VERTICAL AND TOP RIGHT
    0xf0: '⏋',    # \u23cb DENTISTRY SYMBOL LIGHT VERTICAL AND TOP LEFT
    0xf1: '●',    # \u25cf BLACK CIRCLE
    0xf3: '♥',    # \u2665 BLACK HEART SUIT
    0xf5: '◢',    # \u25e2 BLACK LOWER RIGHT TRIANGLE
    0xf6: '╳',    # \u2573 BOX DRAWINGS LIGHT DIAGONAL CROSS
    0xf7: '○',    # \u25cb WHITE CIRCLE
    0xf8: '♣',    # \u2663 BLACK CLUB SUIT
    0xfa: '♦',    # \u2666 BLACK DIAMOND SUIT
    0xfb: '£',    # \u00a3 POUND SIGN
    0xfc: '↓',    # \u2193 DOWNWARDS ARROW
    0xfd: '│',    # \u2502 BOX DRAWINGS LIGHT VERTICAL
    0xfe: '◥',    # \u25e5 BLACK UPPER RIGHT TRIANGLE
    0xff: 'π',    # \u03c0 GREEK SMALL LETTER PI
                  #        see also Pi constant TOKENS[0xe4]
}
