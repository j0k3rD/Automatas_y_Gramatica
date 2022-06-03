#---------------------Proyecto Final para Autómatas y Gramática.---------------------#


#-----Importo las librerias a usar.-----#
import sys
import constants
import pandas as pd
import numpy as np


#-----Creo el Menu para elegir las operaciones a realizar.-----#
class Main:

    #-----Leo el archivo de donde voy a obtener la información.-----#
    #Direccion donde se encuentra mi archivo.
    path = "Usuarios_WiFi.csv"

    data = pd.read_csv(path,header=0)
    print(data)

    #-----Primero tengo que rellenar los casilleros vacios que tengo en mi documento CSV-----#
    pd.set_option('display.max_columns', 20)

    # data['Usuario'].str.upper()

    print(data['Usuario'].str.extract(r'([A-Z])'))


    #Funcion Menu
    def menu():
        
        while True:
            print(constants.MENU)
            opc = int(input(constants.ANSWER))
            
            if opc == 1:

                print(constants.SPACE)
                
                print(constants.SPACE)
                input(constants.P_TO_C)

            elif opc == 2:

                print(constants.SPACE)

                input(constants.P_TO_C)

            elif opc == 3:

                print(constants.SPACE)

                input(constants.P_TO_C)


            elif opc == 4:
                print(constants.WANT_QUIT)
                op = int(input(constants.ANSWER))
                if op == 1:
                    print(constants.EXITING)
                    sys.exit(0)
                elif op == 2:
                    print(constants.RETURNING)
                    Main.menu()
                else:
                    print(constants.INV_OP)
            else:
                print(constants.INV_OP2)

if __name__ == "__main__":
    Main.menu()