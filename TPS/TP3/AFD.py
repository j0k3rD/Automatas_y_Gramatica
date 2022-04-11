# Ejercicio 1 - TP3 - Automata: (a|b)*

aut = str(input("Enter the string: "))

dfa = {0:{'a':1, 'b':2},
       1:{'a':1, 'b':2},
       2:{'a':1, 'b':2}}

# accepting = "2"
initial = 0

def accepts(transitions,initial,accepting,s):
    state = initial
    for c in s:
        state = transitions[state][c]
    return state in accepting

print(accepts(dfa,initial,{c},aut))

