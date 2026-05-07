"Konwenter na 5"


def to_binary(n):
    """Konwertuje liczbę naturalną na system binarny."""
    if not isinstance(n, int):
        raise TypeError("To nie jest liczba naturalna")

    if n < 0 or n > 100:
        raise ValueError("Liczba poza zakresem (0-100)")

    if n == 0:
        return "0"
    return bin(n).replace("0b", "")
