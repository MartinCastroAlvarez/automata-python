from typing import Any


class Symbol:
    def __init__(self, value: str) -> None:
        assert value and isinstance(value, str)
        self.value = value

    def __id__(self) -> int:
        return hash(self.value)

    def __hash__(self) -> int:
        return hash(self.value)

    def __eq__(self, other: Any) -> bool:
        return isinstance(other, self.__class__) and other.value == self.value

    def __repr__(self) -> str:
        return f"<Symbol: '{self.value}'>"


DEFAULT_SYMBOL = Symbol("[DEFAULT]")
