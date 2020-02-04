import pytest

from bassassyn.utils import text_repr


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
