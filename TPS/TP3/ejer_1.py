w = str(input("Enter the string: "))

transitions = [
    {"a": {1,2}},
    {"b": {1, 2}},
    {"c": {1,2}}
]
starting_state = 0
accepting_states = {0}

def nfa(w):
    cur_states = {starting_state}
    for c in w:
        if not cur_states: 
            print("reject")
        cur_states = set.union(*
            (transitions[s].get(c, set()) for s in cur_states))
    print("accept") if cur_states & accepting_states else print("reject")

nfa(w)