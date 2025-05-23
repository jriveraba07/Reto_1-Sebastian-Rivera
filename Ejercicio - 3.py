# Ejercicio - 3

#* Función que reciba una lista de números y devuelva solo aquellos que son primos.
#* La función debe recibir una lista de enteros y retornar solo aquellos que sean primos.

import math

#* funciones

def ingresa_lista(mensaje):
    s = input(mensaje)
    s = s[1:-1]
    l = s.split(",")
    return [int(i) for i in l]

def es_primo(x):
    T : bool = True
    if x <= 1:
        return not T
    elif x == 2:
        return T
    else:
        for i in range(2, int(math.sqrt(x))):
            if x % i == 0:
                return not T
            else: 
                continue 
    return T

def lista_primo(x): 
    d = []
    for i in range(len(x)):
        if es_primo(x[i]):
            d.append(x[i])
        else: 
            continue    
    return d #La funcion se puede simplificar en: return [i for i in x if es_primo(i)]

#* programa principal

lista = ingresa_lista("Introduce la lista para tener los primos: ")
y = lista_primo(lista)

#* salida

print("los primos en la lista son:", y)  

