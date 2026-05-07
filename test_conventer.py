import pytest
from converter import to_binary


@pytest.mark.parametrize(
    "input_val, expected",
    [
        (0, "0"),
        (5, "101"),
        (10, "1010"),
        (100, "1100100"),
    ],
)
def test_conversion_correctness(input_val, expected):
    assert to_binary(input_val) == expected


def test_out_of_range():
    with pytest.raises(ValueError, match="Liczba poza zakresem"):
        to_binary(-1)
    with pytest.raises(ValueError, match="Liczba poza zakresem"):
        to_binary(101)


def test_is_natural_number():
    with pytest.raises(TypeError, match="To nie jest liczba naturalna"):
        to_binary(10.5)
    with pytest.raises(TypeError, match="To nie jest liczba naturalna"):
        to_binary("10")
