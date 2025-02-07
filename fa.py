from pydantic import BaseModel
from typing import Dict, Set

class FiniteAutomata(BaseModel):
    states: Set[str]
    input_symbols: Set[str]
    transitions: Dict[str, Dict[str, str]]
    initial_state: str
    final_states: Set[str]
