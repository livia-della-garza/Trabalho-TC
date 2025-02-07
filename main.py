from fastapi import FastAPI
from mt import TuringMachine
from automata.tm.dtm import DTM
from fastapi.responses import FileResponse
from fa import FiniteAutomata
from automata.fa.dfa import DFA
from pda import PushdownAutomata
from automata.pda.dpda import DPDA
import graphviz

app = FastAPI()

dtm = None
dfa = None
pda = None

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/mt/")
def create_mt(turing: TuringMachine):
    global dtm
    dtm = DTM(
        states=turing.states,
        input_symbols=turing.input_symbols,
        tape_symbols=turing.tape_symbols,
        transitions=turing.transitions,
        initial_state=turing.initial_state,
        blank_symbol=turing.blank_symbol,
        final_states=turing.final_states,
    )
    return dtm.accepts_input(turing.my_input)

@app.get("/mt/image/")
def get_mt_image():
    """Gera e retorna a imagem do autômato salvo."""
    global dtm
    if dtm is None:
        return {"error": "Nenhuma máquina de Turing salva. Envie um POST para /mt/save/ primeiro."}


    # Gerar imagem do autômato
    dot = graphviz.Digraph(format="png")

    dot.node("", shape="none")  
    dot.edge("", dtm.initial_state)

    for state in dtm.states:
        if state in dtm.final_states:
            dot.node(state, shape="doublecircle")
        else:
            dot.node(state, shape="circle")
    
    for state, transitions in dtm.transitions.items():
        for symbol, (next_state, write, move) in transitions.items():
            label = f'<<FONT>{symbol}/{write} {move}<BR/></FONT>>'
            dot.edge(state, next_state, label=label)
    
    dot.render("dtm")

    dtm.show_diagram(path="dtm.png")

    return FileResponse("dtm.png", media_type="image/png")

@app.post("/fa/")
def create_fa(finite: FiniteAutomata):
    global dfa
    dfa = DFA(
        states=finite.states,
        input_symbols=finite.input_symbols,
        transitions=finite.transitions,
        initial_state=finite.initial_state,
        final_states=finite.final_states,
    )
    return dfa.accepts_input(finite.my_input)

@app.get("/fa/image/")
def get_fa_image():
    global dfa
    # Supondo que dfa.show_diagram() retorne um objeto AGraph (se for o caso)
    dfa_diagram = dfa.show_diagram()  # ou use dfa.get_diagram() se for o método correto
    dfa_diagram.draw("dfa.png", format="png")  # Use 'draw' para gerar e salvar a imagem
    
    return FileResponse("dfa.png", media_type="image/png")

@app.post("/pda/")
def create_pda(pushdown: PushdownAutomata):
    global pda
    pda = DPDA(
        states=pushdown.states,
        input_symbols=pushdown.input_symbols,
        stack_symbols=pushdown.stack_symbols,
        transitions=pushdown.transitions,
        initial_state=pushdown.initial_state,
        initial_stack_symbol=pushdown.initial_stack_symbol,
        final_states=pushdown.final_states,
        acceptance_mode=pushdown.acceptance_mode
    )
    return pda.accepts_input(pushdown.my_input)

@app.get("/pda/image/")
def get_pda_image():
    global pda
    # Supondo que dfa.show_diagram() retorne um objeto AGraph (se for o caso)
    pda_diagram = pda.show_diagram()  # ou use dfa.get_diagram() se for o método correto
    pda_diagram.draw("pda.png", format="png")  # Use 'draw' para gerar e salvar a imagem
    
    return FileResponse("pda.png", media_type="image/png")