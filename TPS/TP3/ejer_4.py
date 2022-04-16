# Ejercicio 4 (en clase) - TP3 - Automata: (a|b)*(a|bb)

aut = input("Enter the string: ")
aut.re

dfa = {0:{'a':1, 'b':2, ' ':1},
       1:{'a':1, 'b':3, ' ':2}, 
       2:{'a':1, 'b':2, ' ':3},
       3:{'a':1, 'b':4, ' ':4},
       4:{'a':1, 'b':2, ' ':4}}

# accepting = "2"
initial = 0

def accepts(transitions,initial,accepting,s):
    state = initial
    for c in s:
        state = transitions[state][c]
    return state in accepting

print(accepts(dfa,initial,{4},aut))