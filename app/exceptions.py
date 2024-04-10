class SymbolNotRecognizedByAlphabet(Exception):
    """Raised when a symbol is not recognized by an alphabet."""


class SymbolNotRecognizedByTransitionTable(Exception):
    """Raised if the transition table does not recognize a symbol."""
