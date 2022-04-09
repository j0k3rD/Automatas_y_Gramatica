# dfa = {0:{'a':0, 'b':1},
#        1:{'a':2, 'b':0},
#        2:{'a':1, 'b':2}}

def accepts(transitions,initial,accepting,s):
    state = initial
    for c in s:
        state = transitions[state][c]
    return state in accepting

print(accepts(state,0,{0},'aba'))


state = {
        '1': {
            'a': ['2'],
            'b': ['3']
        },
        '2': {
            'a': ['3'],
        },
        '3': {
            'a': ['1'],
            'b': ['4']
        },
        '4': {
            'b': ['1']
        },
    }
