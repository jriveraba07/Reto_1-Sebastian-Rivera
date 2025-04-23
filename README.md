# Reto_1-Sebastian Rivera 
 Reto 1 de POO grupo (4) con Felipe Gonzalez Roldan

## Retos y explicacion 
Contenido de los retos y como llegue a la solución \mathbb{R}

---

### Ejercicio 1
Crear una función que realice operaciones básicas (suma, resta, multiplicación, división) entre dos números, según la elección del usuario, la forma de entrada de la función será los dos operandos y el caracter usado para la operación. entrada: (1,2,"+"), salida (3).

**Como llegue a la solución:** dado que el usuario va a ingresar un caracter, el cual es el signo correspondiente a la operacion que el usuario quiera, hacemos que la funcion compare con todos los posibles caracteres que hay en el programa una variable en la cual se almacenara dicho caracter.

---

### Ejercicio 2
Realice una función que permita validar si una palabra es un palíndromo. Condición: No se vale hacer slicing para invertir la palabra y verificar que sea igual a la original.

**Como llegue a la solución:** ya que no se puede invertir la palabra segun la condicion del ejercicio, solo recorremos la mitad de la palabra que debe ser igual a la otra mitad y una division entera ya que a los strings con elementos impares tienen un elemento "central"

---

### Ejercicio 3
Escribir una función que reciba una lista de números y devuelva solo aquellos que son primos. La función debe recibir una lista de enteros y retornar solo aquellos que sean primos.

**Como llegue a la solución:** Primo que todo definimos que es un primo, luego de ese recoremos la lista y dejar con los que cumplan la funcion que determine si es primo o no

---

### Ejercicio 4
Escribir una función que reciba una lista de números enteros y retorne la mayor suma entre dos elementos consecutivos.

**Como llegue a la solución** Guardo la primera suma y despues las comparo con las demas, adicional a eso le agregamos la posicion (iniciando en cero) para que se sepa si esta correcto el procedimiento

---

### Ejercicio 5
Escribir una función que reciba una lista de string y retorne unicamente aquellos elementos que tengan los mismos caracteres. e.g. entrada: $["amor", "roma", "perro"]$, salida $["amor", "roma"]$

**Como llegue a la solución:** Para comparar strings los voy a separar como si fueran listas ordenarlos (ya que los caracteres son numeros como tal en ascii) y comparar con un "==", como habia el caso que hay mas de un conjunto de palabras se decide guardarla en una lista de listas que al final va a tener instrucciones si la lista esta vacia, tiene un elemento o mas de un elemento, tambien se eliminan los elementos de la lista para recortar y algunos condicionales que si no se cumplen se sale del ciclo automaticamente.


