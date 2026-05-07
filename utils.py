"""Moduł z funkcjami kalkulatora."""

def add(a: int, b: int) -> int:
    """Dodaje dwie liczby."""
    return a + b

def subtract(a: int, b: int) -> int:
    """Odejmuje dwie liczby."""
    return a - b

def multiply(a: int, b: int) -> int:
    """Mnoży dwie liczby."""
    return a * b

def divide(a: int, b: int) -> float:
    """Dzieli dwie liczby."""
    if b == 0:
        raise ValueError("Nie dziel przez zero")
    return a / b
