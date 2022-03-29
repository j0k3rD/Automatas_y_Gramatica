import re
import string
from wsgiref.validate import PartialIteratorWrapper

def contiene_s(cadena):
    patron_n = '[0-9]'
    patron_l = '[a-z A-Z]'
    
    patron = '7'
    patron_2= 'p|P'


    if re.search(patron_n, cadena[0]):
        print(f'Para el Patron 7')
        print(f'existe')

        if re.search(patron, cadena):
            print(f'La cadena "{cadena}" si aparece el numero "{patron}"\n')
        else:
            print(f'La cadena "{cadena}" NO aparece el numero "{patron}"\n')

    
    elif re.search(patron_l, cadena[0]):
        print(f'Para el Patron P')
        print(f'existe')

        if re.search(patron_2, cadena):
            print(f'La cadena "{cadena}" si aparece el numero "{patron_2}"\n')
        else:
            print(f'La cadena "{cadena}" NO aparece el numero "{patron_2}"\n')


cadena_1 = '1237Fernand0'
cadena_2 = 'umP7'
cadena_3 = 'facultad'

contiene_s(cadena_1)
contiene_s(cadena_2)
contiene_s(cadena_3)