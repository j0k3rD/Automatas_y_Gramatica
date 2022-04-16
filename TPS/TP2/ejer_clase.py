# Ejercicio en Clase - TP3 - Automata: (a|b)*abb

aut = input(str("Enter the string: "))
aut1 = aut.replace(" ","")


dfa = {0:{'a':1, 'b':2},
       1:{'a':1, 'b':3}, 
       2:{'a':1, 'b':2},
       3:{'a':1, 'b':4},
       4:{'a':1, 'b':2}}

# accepting = "2"
initial = 0

def accepts(transitions,initial,accepting,s):
        state = initial
        for c in s:
            state = transitions[state][c]
        return state in accepting

print(accepts(dfa,initial,{4},aut1))