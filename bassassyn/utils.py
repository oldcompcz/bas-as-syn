import io

from bassassyn import constants


def grab_data(data, start):
    """Generate a sequence representing individual Basic lines."""
    stream = io.BytesIO(data)
    stream.seek(start)

    # split to Basic lines based on line length tokens
    while True:
        adr = stream.tell()
        line_length = int.from_bytes(stream.read(2), 'little')

        # eof is indicated by two null-bytes
        if line_length == 0:
            break

        line_number = int.from_bytes(stream.read(2), 'little')
        line_length -= 5
        if line_length > 0xff:
            raise ValueError(f'Line length > 255: line {line_number},'
                             f' length {line_length}.')

        line_info = {'number': line_number,
                     'contents': stream.read(line_length),
                     'adr': adr}

        # skip line-ending null-byte
        stream.read(1)

        yield line_info


def text_repr(data, adr_to_num=None,
              token_mode='keywords', token_0c_mode='number', basic='700'):
    """Generate a sequence representing elements of a Basic line."""
    if adr_to_num is None:
        adr_to_num = {}
    if basic == '700':
        tokens, prefixed_tokens = constants.TOKENS_700, constants.PREFIXED_700
    else:
        tokens, prefixed_tokens = constants.TOKENS_800, constants.PREFIXED_800

    stream = io.BytesIO(data)
    inside_quotes = False
    inside_comment = False
    inside_data = False

    while True:
        byte = stream.read(1)
        if byte:
            n = byte[0]    # bytes -> int
        else:
            break

        if inside_quotes:
            tag = 'comment' if inside_comment else 'str'
            # double quote
            if n == 34:
                inside_quotes = False
                yield '"', tag

            # ascii chars from ' ' to ']'
            elif 0x20 <= n <= 0x5d:
                yield chr(n), tag

            elif n in constants.OTHER:
                yield constants.OTHER[n], tag

            else:
                yield f'[${n:x}]', 'special'

        elif inside_comment:
            # double quote
            if n == 34:
                inside_quotes = True
                yield '"', 'comment'

            # colon
            elif n == 58:
                inside_comment = False
                yield ':', 'separator'

            # ascii chars from ' ' to ']'
            elif 0x20 <= n <= 0x5d:
                yield chr(n), 'comment'

            elif n in constants.OTHER:
                yield constants.OTHER[n], 'comment'

            else:
                yield f'[${n:x}]', 'special'

        elif inside_data:
            # double quote
            if n == 34:
                inside_quotes = True
                yield '"', 'str'

            # colon
            elif n == 58:
                inside_data = False
                yield ':', 'separator'

            # ascii chars from ' ' to ']'
            elif 0x20 <= n <= 0x5d:
                yield chr(n), 'data'

            elif n in constants.OTHER:
                yield constants.OTHER[n], 'data'

            else:
                yield f'[${n:x}]', 'special'

        else:
            # double quote
            if n == 34:
                inside_quotes = True
                yield '"', 'str'

            # colon
            elif n == 58:
                next_byte = stream.read(1)
                # apostrophe
                if next_byte == b"'":
                    yield "'", 'comment'
                    inside_comment = True
                # ELSE token
                elif next_byte == b'\xc2':
                    yield 'ELSE', 'keyword'
                else:
                    # if next_byte is b'', we don't want to seek by -1
                    stream.seek(-len(next_byte), io.SEEK_CUR)
                    yield ':', 'separator'

            # ascii chars from ' ' to ']'
            elif 0x20 <= n <= 0x5d:
                yield chr(n), 'identifier'

            elif n in tokens:
                tag = 'operator' if 234 <= n <= 253 else 'keyword'
                if token_mode == 'keywords':
                    yield tokens[n], tag
                else:
                    yield (f'[{n:X}]' if token_mode == 'tokens_hex'
                           else f'[{n}]'), tag
                # DATA
                if n == 148:
                    inside_data = True
                # REM
                if n == 151:
                    inside_comment = True

            # FE or FF prefix
            elif n in (0xfe, 0xff):
                if token_mode == 'keywords':
                    yield prefixed_tokens[n][stream.read(1)[0]], 'keyword'
                else:
                    yield '[', 'keyword'
                    yield f'{n:X}', 'comment'
                    yield (f'{stream.read(1)[0]:X}]'
                           if token_mode == 'tokens_hex'
                           else f'{stream.read(1)[0]}]'), 'keyword'

            # float number token
            elif n == 0x15:
                float_str = get_float_40bit(stream.read(5), return_string=True)
                yield float_str, 'dec'

            # hex number token
            elif n == 0x11:
                num_16bit = int.from_bytes(stream.read(2), 'little')
                yield f'${num_16bit:X}', 'hex'

            # line number token
            elif n == 0x0b:
                line_num = int.from_bytes(stream.read(2), 'little')
                yield str(line_num), 'line_number'

            # line address token
            elif n == 0x0c:
                line_adr = int.from_bytes(stream.read(2), 'little')
                if token_0c_mode == 'address':
                    yield f'${line_adr:X}', 'special'
                elif token_0c_mode == 'number':
                    line_num = adr_to_num[line_adr]
                    yield str(line_num), 'line_number'

            else:
                yield f'[${n:x}]', 'special'


def get_float_40bit(sequence, return_string=False):
    """Return a number represented by the first 5 bytes of 'sequence'.

    If 'sequence' is not bytes-like, its first 5 values must
    be numbers in range 0-255. These five bytes represent the number
    as a 40-bit float.

    By default, return a float. If 'return_string' is True, return
    a string formatted {:.0f} for whole numbers, {:f} otherwise.
    """
    if sequence[0]:
        exponent = sequence[0] - 0x80

        mantissa_bytes = bytes((sequence[1] & 0x7f,)) + bytes(sequence[2:5])
        mantissa = int.from_bytes(mantissa_bytes, 'big') / 2**32

        result = 2**exponent * (0.5 + mantissa)

    else:
        result = 0.0

    if return_string:
        return f'{result:.0f}' if result.is_integer() else f'{result:f}'

    else:
        return result


def retrieve_keywords(data, name):
    titles = ['TOK_FF', 'TOK_FE', 'TOK']
    # we assume that GOTO is the first keyword (b'O' + 0x80 = 0xcf)
    i = data.index(b'GOT\xcf')
    adr = i
    keyword = ''
    output_file = open(name + '_KEYWORDS.py', 'w')
    print(f'{titles.pop()} = {{', file=output_file)
    token = 0x80

    while True:
        n = data[i]
        if n == 0xff:
            i += 1
            if titles:
                print(f'}}\n{titles.pop()} = {{', file=output_file)
                token = 0x80
            else:
                break
        else:
            flag, letter = n & 0x80, chr(n & 0x7f)
            keyword += letter
            i += 1
            if flag:
                if letter != '\x00':
                    print(f'    {token:#x}: {keyword!r},    # {adr:#x}',
                          file=output_file)
                keyword = ''
                token += 1
                adr = i
    print('}', file=output_file)
