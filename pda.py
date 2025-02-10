from pydantic import BaseModel
from typing import Dict, Set

class PushdownAutomata(BaseModel):
    states: Set[str]
    input_symbols: Set[str]
    stack_symbols: Set[str]

    transitions: Dict[str, Dict[str, Dict[str, list]]]

    initial_state: str
    initial_stack_symbol: str
    final_states: Set[str]
    acceptance_mode: str