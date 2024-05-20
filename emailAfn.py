import sys

from app.afn import AFN
from app.alphabet import Alphabet
from app.state import State
from app.symbol import DEFAULT_SYMBOL
from app.transition import TransitionTable
from app import dictionaries

if __name__ == "__main__":
    if not len(sys.argv) == 2 or not sys.argv[1]:
        raise ValueError("Missing input string")

    alphabet = Alphabet(
        dictionaries.LOWER_CASE |
        dictionaries.UPPER_CASE |
        dictionaries.NUMERIC |
        dictionaries.SYMBOLS
    )

    state_0 = State("0")
    state_1 = State("1")
    state_2 = State("2")
    state_3 = State("3")
    state_4 = State("4")
    state_5 = State("5")
    state_6 = State("6")
    state_7 = State("7")
    state_8 = State("8")
    state_FAIL = State("FAIL")

    transition_table = TransitionTable(
        {
            # Starting with a symbol is not allowed.
            (state_0, "."): {state_FAIL},
            (state_0, "/"): {state_FAIL},
            (state_0, "-"): {state_FAIL},
            (state_0, "_"): {state_FAIL},
            (state_0, "+"): {state_FAIL},
            (state_0, "@"): {state_FAIL},
            (state_0, DEFAULT_SYMBOL): {state_1},
            # Ending with a symbol is not allowed.
            (state_1, "."): {state_2},
            (state_1, "/"): {state_2},
            (state_1, "-"): {state_2},
            (state_1, "_"): {state_2},
            (state_1, "+"): {state_2},
            (state_1, "@"): {state_3},
            (state_1, DEFAULT_SYMBOL): {state_1},
            # No 2 consecutive symbols are allowed.
            (state_2, "."): {state_FAIL},
            (state_2, "/"): {state_FAIL},
            (state_2, "-"): {state_FAIL},
            (state_2, "_"): {state_FAIL},
            (state_2, "+"): {state_FAIL},
            (state_2, "@"): {state_FAIL},
            (state_2, DEFAULT_SYMBOL): {state_1},
            # At the '@' only an alphanumeric value is allowed.
            (state_3, "."): {state_FAIL},
            (state_3, "/"): {state_FAIL},
            (state_3, "-"): {state_FAIL},
            (state_3, "_"): {state_FAIL},
            (state_2, "+"): {state_FAIL},
            (state_3, "@"): {state_FAIL},
            (state_3, DEFAULT_SYMBOL): {state_4},
            # The domain requires at least 1 alphanumeric value.
            (state_4, "."): {state_FAIL},
            (state_4, "/"): {state_FAIL},
            (state_4, "-"): {state_FAIL},
            (state_4, "_"): {state_FAIL},
            (state_4, "+"): {state_FAIL},
            (state_4, "@"): {state_FAIL},
            (state_4, DEFAULT_SYMBOL): {state_5},
            # The domain name must end with a dot.
            (state_5, "."): {state_6},
            (state_5, "/"): {state_FAIL},
            (state_5, "-"): {state_FAIL},
            (state_5, "_"): {state_FAIL},
            (state_5, "+"): {state_FAIL},
            (state_5, "@"): {state_FAIL},
            (state_5, DEFAULT_SYMBOL): {state_5},
            # At the dot only alphanumeric values are allowed.
            (state_6, "."): {state_FAIL},
            (state_6, "/"): {state_FAIL},
            (state_6, "-"): {state_FAIL},
            (state_6, "_"): {state_FAIL},
            (state_6, "+"): {state_FAIL},
            (state_6, "@"): {state_FAIL},
            (state_6, DEFAULT_SYMBOL): {state_7},
            # The TLD requires at least 1 alphanumeric value.
            (state_7, "."): {state_8},
            (state_7, "/"): {state_FAIL},
            (state_7, "-"): {state_FAIL},
            (state_7, "_"): {state_FAIL},
            (state_7, "+"): {state_FAIL},
            (state_7, "@"): {state_FAIL},
            (state_7, DEFAULT_SYMBOL): {state_7},
            # It is possible to have multiple TLDs
            (state_8, "."): {state_6},
            (state_8, "/"): {state_FAIL},
            (state_8, "-"): {state_FAIL},
            (state_8, "_"): {state_FAIL},
            (state_8, "+"): {state_FAIL},
            (state_8, "@"): {state_FAIL},
            (state_8, DEFAULT_SYMBOL): {state_7},
            (state_FAIL, DEFAULT_SYMBOL): {state_FAIL},
        }
    )

    afn = AFN(
        initial_state=state_0,
        acceptance_states={
            state_7,
        },
        alphabet=alphabet,
        transition_table=transition_table,
    )

    word = sys.argv[1]
    for value in word:
        afn.evaluate(value)

    if not afn.is_accepted():
        print(f"Rejected: '{word}'")
        sys.exit(1)
    print(f"Accepted: '{word}'")
