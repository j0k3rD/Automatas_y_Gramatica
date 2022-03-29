# Ejercicio 1_a -- Automata para '[A|B]'

def automata():
    aut = []
    c = str(input("Ingrese un caracter entre [A|B]: "))
    while c == 'A' or c == 'B':
        aut.append(c)
        print("Exelente!")
        print("La cadena hasta ahora es:", aut)
        c = str(input("Ingrese otro caracter entre [A|B]: "))
    print("Error. No es compatible con el Automata.")

automata()
