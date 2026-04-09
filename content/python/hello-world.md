Title: Hola mundo con Python
Date: 2026-04-01
Category: Python
Tags: Python, Tutorial, Programación
Summary: Cuando empiezas a programar, hay un programa clásico que todos escriben: “Hola, Mundo!”. En este tutorial aprenderás a crear tu primer programa en Python y entender cómo funciona la entrada y salida de datos.

Después de haber instalado Python, comenzaremos haciendo el programa más popular cuando se empieza a estudiar programación, "Hola, Mundo!".

Este es el programa más sencillo que existe, el objetivo es crear un programa, que al ejecutarlo imprima la frase "Hola, Mundo!" en la pantalla.

Iniciamos creando un archivo llamado *hola.py* donde escribiremos el siguiente código.

```python
--8<-- "content/code/python/hola.py"
```

Así de sencillo es crear este programa en Python, ya que es un lenguaje de programación muy fácil de aprender.
Lo que estamos haciendo es usar la función *print*, que como su nombre lo indica, se usa para imprimir cosas en pantalla.

Para usarla, tenemos que escribir paréntesis y dentro de estos, pasarle lo
que queremos imprimir, lo que pasamos dentro de los paréntesis se llama *parámetro*.

Para ejecutar nuestro programa abrimos la terminal en Visual Studio Code
(shortcut:  ++ctrl+"`"++) e ingresamos el siguiente comando.

```bash
python hola.py
```

Una vez ingresado el comando, vemos como en la terminal se imprime el texto *Hola, Mundo!*

## Entrada de datos

Nuestro primer programa no es nada interactivo, pues, solo imprime el mismo
mensaje en pantalla cada vez que lo ejecutamos. El objetivo principal de un
programa es solucionar un problema, para esto tiene que recibir datos de
entrada, procesarlos internamente y generar datos de salida que sean de utilidad
y faciliten nuestra vida.

Para recibir datos de entrada por consola en python se usa la función *input*.
Para entender como se usa, escribamos un programa que pida al usuario su nombre, y una
vez que lo haya ingresado lo salude diciendo "Hola, " seguido del nombre que el
usuario ingresó.

Para ello creemos un archivo llamado *saludo.py* e ingresemos el siguiente código

{% include_code python/saludo.py lang:python :hideall:  %}

Para correr este programa ingresamos el siguiente comando en la terminal.

    :::bash
    python saludo.py

Al ingresar el comando se ejecutará nuestro programa.

La función *input* recibe como parámetro el texto con el que pediremos al usuario que ingrese algún dato, en este caso el nombre. Como resultado nos da lo que el usuario haya ingresado antes de presionar *enter*, este resultado lo guardamos en una variable llamada nombre.

En la línea 2 usamos la función de *print*, del primer programa, para imprimir el
saludo en pantalla, aunque ahora el parámetro ha cambiado. Al principio
de nuestro mensaje, afuera de las comillas, hemos escrito una *f*. Al poner esta *f*
al principio hacemos uso de una de las características de Python llamada
*"F-Strings"*

Pero, que es un *"F-String"*, para entender este término primero necesitamos
entender que es un *string*. Un string en Python es un tipo de dato que
representa una cadena de texto, la cual siempre va dentro de comillas sencillas
'cadena' o comillas dobles "cadena".

Entonces, un *"F-String"*, es un *string*, cadena de texto, que nos permite
incrustar el valor de una variable, poniéndolo entre corchetes {}, es por esto que nuestro programa imprime "Hola, " seguido del nombre que el usuario ingresó y no "Hola, nombre"

## Ejercicio: Cafetería

Para reforzar los conceptos aprendidos el día de hoy. Escribe un programa que
simule el pedido en una cafetería. Tu programa debe darle la bienvenida al
usuario con el mensaje "Bienvenido a la cafetería Robert's" luego, debe
de preguntarle "¿Qué va a ordenar?", después, debe de preguntar "¿A nombre
de quién?". Por último debe de imprimir, la orden y a quien va dirigida, por
ejemplo. Si el usuario Roberto pidió un café americano el programa debe de
imprimir "Sale café americano para Roberto".

## Solución al ejercicio

![Imagen de código]({static}/images/solution.jpg)

Antes de ver la solución, trata de resolver el problema por ti mismo, haz uso de las funciones *print* e *input* y si tienes alguna duda vuelve a repasar los ejemplos y la explicación.

Para crear nuestro programa crea un archivo llamado *cafeteria.py* e ingresa el siguiente código.

{% include_code python/cafeteria.py lang:python :hideall:  %}

Para solucionar el ejercicio primero imprimimos el mensaje de bienvenida usando
la función *print*, enseguida pedimos al usuario su orden y su nombre usando la
función *input* y guardamos los resultados en las variables orden y nombre,
respectivamente. Por último, imprimimos el mensaje indicando que la orden está
lista volviendo a hacer uso de la función *print*

## Resumen

En este post aprendiste a imprimir texto en pantalla, usando la función *print*,
y a recibir datos del usuario, usando la función *input*. En el siguiente tutorial veremos cómo trabajar con números y realizar operaciones básicas en Python.
