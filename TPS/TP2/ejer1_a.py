# Ejercicio 1_a -- Automata para '[A|B]'
import Constants


def main():
    lista = []
    estado = 0
    print(Constants.INIT_STATE)
    create_state(estado)
    x = print(input("Ingrese el Automata a evaluar: \n"))
    lista.append(x)
    change_state()
    print(Constants.NEXT_STATE)
    
def switch_state(lista, estado):
    for i in range(len(lista)):
        if i == "a":
            create_state(estado)
        elif i == "b":
            
        elif i == "":
            change_state()
        else:
            state_end()


        
def create_state(estado):
    if switch_state():
        estado +=1
    


def state_end(lista):
    if lista.index(-1):
        print("Estado finalizado")



if __name__=='__main__':
    main()