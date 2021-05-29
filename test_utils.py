import pytest

from bassassyn.utils import text_repr, retrieve_keywords, _retrieve


@pytest.mark.parametrize('data, expected', (
        (
            b'\x9b',
            [
                ('CLS', 'keyword')
            ]
        ),
        (
            b'\x80\x0b\x35\x03',
            [
                ('GOTO', 'keyword'),
                ('821', 'line_number')
            ]
        ),
        (
            b'\x8f\x11\x01\x00:\x91X',
            [
                ('PRINT', 'keyword'),
                ('$1', 'hex'),
                (':', 'separator'),
                ('INPUT', 'keyword'),
                ('X', 'identifier')
            ]
        ),
        (
            b'\x8d F\xf4\x15\x00\x00\x00\x00\x00\xe0\x15\x86\x1c\x00\x00\x00:'
            b'\xfe\x83F,\x15\x00\x00\x00\x00\x00,\x15\x83`\x00\x00\x00,\x15'
            b'\x81\x00\x00\x00\x00:\x8e',
            [
                ('FOR', 'keyword'),
                (' ', 'identifier'),
                ('F', 'identifier'),
                ('=', 'operator'),
                ('0', 'dec'),
                ('TO', 'keyword'),
                ('39', 'dec'),
                (':', 'separator'),
                ('COLOR', 'keyword'),
                ('F', 'identifier'),
                (',', 'identifier'),
                ('0', 'dec'),
                (',', 'identifier'),
                ('7', 'dec'),
                (',', 'identifier'),
                ('1', 'dec'),
                (':', 'separator'),
                ('NEXT', 'keyword')
            ]
        )
))
def test_text_repr(data, expected):
    result = list(text_repr(data))
    assert result == expected


BASIC_700_FILES = (
    'samples/S-Basic.mzf',
    'samples/indy700.mzs',
)

BASIC_800_FILES = (
    'samples/MZ-1Z-016.mzf',
    'samples/2z-046a.mzf',
    'samples/dracula.mzs',
    'samples/amenhotep_stmz.mzs',
)


@pytest.fixture(params=BASIC_700_FILES + BASIC_800_FILES)
def basic_700_800(request):
    filename = request.param
    with open(filename, 'rb') as f:
        data = f.read()
    return data


@pytest.fixture(params=BASIC_700_FILES)
def basic_700(request):
    filename = request.param
    with open(filename, 'rb') as f:
        data = f.read()
    return data


@pytest.fixture(params=BASIC_800_FILES)
def basic_800(request):
    filename = request.param
    with open(filename, 'rb') as f:
        data = f.read()
    return data


def test_retrieve_keywords_basic_700_800(basic_700_800):
    """Test `utils.retrieve_keywords`."""
    result = list(retrieve_keywords(basic_700_800))
    assert result[0] == {'token': '0x80', 'keyword': 'GOTO'}
    assert result[-1] == {'token': '0xffc7', 'keyword': 'FN'}
    assert {'token': '0x8f', 'keyword': 'PRINT'} in result
    assert {'token': '0xfea2', 'keyword': 'MUSIC'} in result
    assert {'token': '0xffa0', 'keyword': 'CHR$'} in result


def test_retrieve_keywords_basic_700(basic_700):
    """Test `utils.retrieve_keywords`."""
    result = list(retrieve_keywords(basic_700))
    assert {'token': '0xc0', 'keyword': 'ERASE'} in result
    assert not any(item['token'] == '0xdc' for item in result)
    assert not any(item['token'] == '0xfe97' for item in result)
    assert {'token': '0xff9e', 'keyword': 'JOY'} in result
    assert not any(item['token'] == '0xffc5' for item in result)

    assert {'token': '0xba', 'keyword': 'OUT#'} in result
    assert {'token': '0xfe81', 'keyword': 'SET'} in result


def test_retrieve_keywords_basic_800(basic_800):
    """Test `utils.retrieve_keywords`."""
    result = list(retrieve_keywords(basic_800))
    assert not any(item['token'] == '0xc0' for item in result)
    assert {'token': '0xdc', 'keyword': 'INIT'} in result
    assert {'token': '0xfe97', 'keyword': 'CIRCLE'} in result
    assert not any(item['token'] == '0xff9e' for item in result)
    assert {'token': '0xffc5', 'keyword': 'POINT'} in result

    assert {'token': '0xba', 'keyword': 'OUT@'} in result
    assert {'token': '0xfe81', 'keyword': 'CSET'} in result


def test_retrieve_basic_700_800(basic_700_800):
    """Test `utils._retrieve`."""
    result = list(_retrieve(basic_700_800))
    assert result[0][0] == 'GOTO'
    assert result[0][-1] == '\x5e'
    assert result[1][0] is None
    assert result[1][-1] == 'BOOT'
    assert result[2][0] == 'INT'


def test_retrieve_basic_700(basic_700):
    """Test `utils._retrieve`."""
    result = list(_retrieve(basic_700))
    assert result[2][-1] is None


def test_retrieve_basic_800(basic_800):
    """Test `utils._retrieve`."""
    result = list(_retrieve(basic_800))
    assert result[2][-1] == 'FN'
