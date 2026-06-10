Title: Operaciones matemáticas con Python
Date: 2026-04-09
Category: Python
Tags: Python, Tutorial, Programación
Summary: La función principal de un programa es la resolución de problemas. En este artículo aprenderemos a cómo resolver problemas matemáticos usando los operadores aritméticos. 

En el post pasado vimos cómo imprimir y recibir datos con Python, sin embargo,
nuestros programas no eran de mucha utilidad, pues, aunque tuvieran algo de
interactividad con el usuario, estos no resolvían ningún problema. Si viajamos
al pasado, cuando las primeras computadoras se crearon, su principal función en
aquel tiempo era resolver problemas matemáticos. En este post aprenderemos a cómo 
realizar operaciones matemáticas en Python.

Python, como todo lenguaje de programación, cuenta con una serie de *operadores
matemáticos* que nos ayudan a realizar operaciones aritméticas. Para conocerlos
escribamos un programa que sume dos números.

Comencemos creando un nuevo archivo llamado *sumar.py* e ingresemos el siguiente código.

```python
--8<-- "content/code/python/calculadora_1.py"
```

Comenzamos pidiendo al usuario que ingrese dos valores, los cuales son guardados
en las variables `:::python valor1` y `:::python valor2`, pero esta vez
utilizamos la función `:::python input` dentro de la función `:::python int`.
Esta función convierte una cadena de texto en un entero, un
entero es un número sin decimales.

Posteriormente, creamos otra variable llamada `:::python resultado` y le asignamos como valor la suma de los dos valores ingresados por el usuario, para esto usamos el operador `:::python +` que se utiliza para realizar sumas. Por último, imprimimos el resultado usando la función `:::python print`.

## Datos numéricos vs cadenas de texto

En el programa anterior usamos una nueva función, la función `:::python int`, el
propósito de esta función es convertir una cadena de texto, `:::python str`, en
un número entero, ya que si no hacemos esto nuestro ejemplo de sumar valores no
serviría. Para ver que pasaría si no usáramos la función `:::python int`,
modifica el código en `:::bash sumar.py`, y borra la función `:::python int`. El 
código quedaría de la siguiente manera.

```python
--8<-- "content/code/python/calculadora_error.py"
```

Al ejecutar el programa usando el comando `:::bash python calculadora.py`, el
resultado obtenido no es el esperado, pues en vez de sumar los números ingresados,
los junta, esto se debe a que la función `:::python input` retorna cadenas de
texto de tipo `:::python str`, debido a esto el operador `:::python +` concatena,
el valor de las variables.

Para solucionar, convertimos nuestros datos de entrada en enteros usando la función `:::python int`. Si quisiéramos usar números decimales tendríamos que usar la función `:::python float`.


## Lista de operadores aritméticos en Python

Como se mencionó antes, Python cuenta con una serie de operadores aritméticos. La siguiente tabla los lista, mencionando su uso y proporciona un ejemplo de uso.

| Operador 	| Uso             	| Ejemplo 	| Resultado |
|----------	|-----------------	|---------	|---------  |
| +        	| Sumar           	| 7+2   	| 9         |
| -        	| Restar          	| 7-2     	| 5         |
| *        	| Multiplicar     	| 7*2     	| 14        |
| /        	| División         	| 7/2     	| 3.5       |
| %        	| Residuo         	| 7%2     	| 1         |
| **       	| Potencia        	| 7**2    	| 49        |
| //       	| División enteros 	| 7//2    	| 3         |

Ahora que conocemos los operadores aritméticos, mejoremos nuestro programa, convirtiéndolo en una 
calculadora. Para ello agregaremos las operaciones de resta, multiplicación y división. 
En un archivo llamado `:::bash calculadora.py` ingresa el siguiente código.


```python
--8<-- "content/code/python/calculadora.py"
```

Este programa comienza de igual forma pidiendo al usuario que ingrese dos valores usando las funciones de 
`:::python input` e `:::python int`, posteriormente realizamos las operaciones y guardamos los
resultados en variables con los nombres de las operaciones: `:::python suma`, `:::python resta`, 
`:::python multiplicacion` y `:::python division`. El programa finaliza imprimiendo los resultados 
usando la función `:::python print`.

## Ejercicio: Conversor de temperaturas

Para poner a aprueba el conocimiento de los operadores aritméticos realicemos el siguiente ejercicio.

Escribe un programa en Python que pida al usuario ingresar una temperatura en grados Celsius y retorne la conversión en grados Fahrenheit.

La fórmula para convertir grados Celsius a grados Fahrenheit es la siguiente:

$$ F = \frac{9}{5}C + 32 $$

## Solución al ejercicio 

![Imagen de código]({static}/images/solution.jpg)

Antes de ver la solución, trata de resolver el problema por ti mismo, vuelve a
leer el contenido sobre cómo usar los operadores aritméticos en Python, recuerda
hacer uso de las funciones de salida y entrada de datos: `:::python print`,
`:::python input`.

Para darle solución al problema, creamos un archivo llamado `:::bash temperatura.py` 
e ingresamos el siguiente código.

```python
--8<-- "content/code/python/temperatura.py"
```

Lo primero que hacemos en el programa es pedir al usuario que ingrese la
temperatura haciendo uso de la función `:::python input`, el resultado de esta
función lo convertimos en número decimal usando la función `:::python float`
enseguida aplicamos la fórmula, haciendo el uso de los operadores aritméticos y
por último imprimimos los resultados usando la función `:::python print`.

## Resumen

En este tutorial aprendimos a hacer uso de los operadores aritméticos y a
convertir cadenas de texto, `:::python str` a números enteros usando la función `:::python int` 
y a números decimales usando la función `:::python float`. En el siguiente
artículo aprenderemos a usar condicionales.
