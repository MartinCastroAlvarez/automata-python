class State:
    def __init__(self, name: str) -> None:
        assert name and isinstance(name, str)
        self.name = name

    def __repr__(self) -> str:
        return f"<State: '{self.name}'>"
