from typing import TypedDict,List,Dict,Any

class State(TypedDict):
    foo:int
    bar:List[str]

def update_state(current_state: State, updates: State) -> None:
    new_state = current_state.copy()

    new_state.update(updates)
    return new_state

state:State = {"foo":1,"bar":['hi']}

node1_update = {"foo":2}

state = update_state(state, node1_update)
print(state)
