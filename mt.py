from pydantic import BaseModel
from typing import Dict, Set, Tuple

class TuringMachine(BaseModel):
    states: Set[str]
    input_symbols: Set[str]
    tape_symbols: Set[str]

    transitions: Dict[str, Dict[str, Tuple[str, str, str]]]

    initial_state: str
    blank_symbol: str
    final_states: Set[str]
    my_input: str