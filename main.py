from fastapi import FastAPI, HTTPException
from mt import TuringMachine
from automata.tm.dtm import DTM
from fastapi.responses import FileResponse
from fa import FiniteAutomata
from automata.fa.dfa import DFA
from pda import PushdownAutomata
from automata.pda.dpda import DPDA
from teste_input import Teste
import graphviz

app = FastAPI()

dtm = None #Máquina de Turing
dfa = None #Autômato finito
pda = None #Autômato com pilha





### MÁQUINA DE TURING ###

#Criar MT
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
    return {"message": "Máquina de Turing criada com sucesso."}

#Gerar imagem da MT
@app.get("/mt/image/")
def get_mt_image():
    global dtm
    if dtm is None:
        raise HTTPException(status_code=404, detail="Nenhuma máquina de Turing criada.")


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
            label = f'<<FONT>{symbol}/{write} {move}</FONT>>'
            dot.edge(state, next_state, label=label)
    
    dot.render("dtm", format="png", cleanup=True)

    return FileResponse("dtm.png", media_type="image/png")

#Retorna informações da MT
@app.get("/mt/")
def get_mt_info():
    global dtm
    if dtm is None:
        raise HTTPException(status_code=404, detail="Nenhuma máquina de Turing criada.")
    return {
        "states": dtm.states,
        "input_symbols": dtm.input_symbols,
        "tape_symbols": dtm.tape_symbols,
        "transitions": dtm.transitions,
        "initial_state": dtm.initial_state,
        "final_states": dtm.final_states,
    }

#Testar input na MT
@app.post("/mt/test/")
def test_mt(teste: Teste):
    global dtm
    if dtm is None:
        raise HTTPException(status_code=404, detail="Nenhuma máquina de Turing criada.")
    return {"accepts": dtm.accepts_input(teste.my_input)}





### AUTÔMATO FINITO ###

#Criar AF
@app.post("/fa")
def create_fa(finite: FiniteAutomata):
    global dfa
    dfa = DFA(
        states=finite.states,
        input_symbols=finite.input_symbols,
        transitions=finite.transitions,
        initial_state=finite.initial_state,
        final_states=finite.final_states,
    )
    return {"message": "Autômato finito criado com sucesso."}

#Gerar imagem do AF
@app.get("/fa/image/")
def get_fa_image():
    global dfa
    if dfa is None:
        raise HTTPException(status_code=404, detail="Nenhum autômato finito criado.")
    dfa_diagram = dfa.show_diagram() 
    dfa_diagram.draw("dfa.png", format="png")
    
    return FileResponse("dfa.png", media_type="image/png")

#Retorna informações do AF
@app.get("/fa/")
def get_fa_info():
    global dfa
    if dfa is None:
        raise HTTPException(status_code=404, detail="Nenhum autômato finito criado.")
    return {
        "states": dfa.states,
        "input_symbols": dfa.input_symbols,
        "transitions": dfa.transitions,
        "initial_state": dfa.initial_state,
        "final_states": dfa.final_states,
    }

#Testa o AF
@app.post("/fa/test/")
def test_fa(teste: Teste):
    global dfa
    if dfa is None:
        raise HTTPException(status_code=404, detail="Nenhum autômato finito criado.")
    return {"accepts": dfa.accepts_input(teste.my_input)}





### AUTÔMATO COM PILHA ###

#Criar PDA
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
    return {"message": "Autômato com pilha criado com sucesso."}

#Gerar a imagem do PDA
@app.get("/pda/image/")
def get_pda_image():
    global pda
    if pda is None:
        raise HTTPException(status_code=404, detail="Nenhum autômato com pilha criado.")
    pda_diagram = pda.show_diagram()  
    pda_diagram.draw("pda.png", format="png") 
    
    return FileResponse("pda.png", media_type="image/png")

#Retornar informações do PDA
@app.get("/pda/")
def get_pda_info():
    global pda
    if pda is None:
        raise HTTPException(status_code=404, detail="Nenhum autômato com pilha criado.")
    return {
        "states": pda.states,
        "input_symbols": pda.input_symbols,
        "stack_symbols": pda.stack_symbols,
        "transitions": pda.transitions,
        "initial_state": pda.initial_state,
        "final_states": pda.final_states,
    }

#Testar o PDA
@app.post("/pda/test/")
def test_pda(teste: Teste):
    global pda
    if pda is None:
        raise HTTPException(status_code=404, detail="Nenhum autômato com pilha criado.")
    return {"accepts": pda.accepts_input(teste.my_input)}