from typing import Set

from .exceptions import SymbolNotRecognizedByAlphabet
from .symbol import Symbol


class Alphabet:
    def __init__(self, values: Set[str]) -> None:
        assert values and isinstance(values, set)
        self.symbols = [Symbol(value) for value in values]

    def __repr__(self) -> str:
        return f"<Alphabet: '{self.symbols}'>"

    def recognize(self, value: str) -> None:
        assert value and isinstance(value, str)
        symbol = Symbol(value)
        assert isinstance(symbol, Symbol)
        if symbol not in self.symbols:
            raise SymbolNotRecognizedByAlphabet(symbol)
        return symbol
