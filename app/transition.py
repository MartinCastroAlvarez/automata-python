from typing import Dict
from typing import Set
from typing import Tuple
from typing import Union

from .exceptions import SymbolNotRecognizedByTransitionTable
from .state import State
from .symbol import DEFAULT_SYMBOL
from .symbol import Symbol


class TransitionTable:
    def __init__(self, rules: Dict[Tuple[State, Union[str, Symbol]], Set[State]]) -> None:
        assert rules and isinstance(rules, dict)
        self.rules = {
            (when[0], when[1] if isinstance(when[1], Symbol) else Symbol(when[1])): then for when, then in rules.items()
        }

    def evaluate(self, current_state: State, symbol: Symbol) -> Set[State]:
        if (current_state, symbol) in self.rules:
            new_states = self.rules[(current_state, symbol)]
            print(f"Transitioning: {symbol} causes ({current_state}, {symbol}) => {new_states}")
            return new_states
        elif (current_state, DEFAULT_SYMBOL) in self.rules:
            new_states = self.rules[(current_state, DEFAULT_SYMBOL)]
            print(f"Transitioning: {symbol} causes ({current_state}, {DEFAULT_SYMBOL}) => {new_states}")
            return new_states
        raise SymbolNotRecognizedByTransitionTable(current_state, symbol)

    def __repr__(self) -> str:
        return f"<Transition Table: '{self.rules}'>"
