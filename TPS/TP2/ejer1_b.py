# Ejercicio 1_b -- Automata para '(AA|B)*(A|BB)'

import sys
from six.moves import input as raw_input

def main():
    transition = [[[0,1],[0]], [[0],[2]], [[2],[3]], [[4],[4]]]
    input = raw_input("Enter the string: ")
    input = list(input)

    for i in range(len(input)): #Cambiamos a,b por 0,1 para simplificar el uso.
        if input[i]=='a':
            input[i]='0' 
        else:
            input[i]='1'

    final = "3" #El ultimo estado lo ponemos = {1}
    start = 0

    trans(transition, input, final, start)
    print("rejected")


def trans(transition, input, final, state):
    for each in transition[state][int(input[0])]: #Verifica cada posibilidad 
        if each < 4:                              #Avanza solo si se encuentra en un estado no hipotetico.
            state = each
            if len(input)==1:
                if (str(state) in final): #Lee el ultimo caracter y verifica que el estado actual no sea el ultimo.
                    print("accepted")
                    sys.exit()
                else:
                    continue
            trans(transition, input[1:], final, state) #Determina que el siguiente caracter a analizar sera el
            # que siga en la lista de inputs

main()