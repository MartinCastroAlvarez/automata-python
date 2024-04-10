from typing import Set

from .alphabet import Alphabet
from .automata import Automata
from .state import State
from .transition import TransitionTable


class AFN(Automata):
    def __init__(
        self,
        alphabet: Alphabet,
        initial_state: State,
        acceptance_states: Set[State],
        transition_table: TransitionTable,
    ):
        assert isinstance(alphabet, Alphabet)
        assert isinstance(initial_state, State)
        assert isinstance(acceptance_states, set)
        assert isinstance(transition_table, TransitionTable)
        self.alphabet = alphabet
        self.initial_state = initial_state
        self.acceptance_states = acceptance_states
        self.transition_table = transition_table
        self.current_states: Set[State] = {
            self.initial_state,
        }

    def __repr__(self) -> str:
        return f"<AFN: '{self.current_states}'>"

    def is_accepted(self) -> bool:
        return any([state in self.acceptance_states for state in self.current_states])

    def evaluate(self, value: str) -> None:
        assert value and isinstance(value, str)
        symbol = self.alphabet.recognize(value)
        self.current_states = {
            new_state
            for current_state in self.current_states
            for new_state in self.transition_table.evaluate(current_state, symbol)
        }
