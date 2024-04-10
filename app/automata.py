from abc import ABC


class Automata(ABC):
    def __repr__(self) -> str:
        raise NotImplementedError()

    def is_accepted(self) -> bool:
        raise NotImplementedError()

    def evaluate(self, value: str) -> None:
        raise NotImplementedError()
