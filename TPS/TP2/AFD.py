dfa = {0:{'a':0, 'b':1},
       1:{'a':2, 'b':0},
       2:{'a':1, 'b':2}}

def accepts(transitions,initial,accepting,s):
    state = initial
    for c in s:
        state = transitions[state][c]
    return state in accepting

print(accepts(dfa,0,{0},'aba'))