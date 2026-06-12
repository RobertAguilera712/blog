Title: Condicionales en Python
Date: 2026-05-04
Category: Python
Tags: Python, Tutorial, Programación
Status: draft
Summary: Un programa tiene que adaptarse a distintas situaciones, adaptando su comportamiento según el escenario. Para esto se usan las condicionales. En este tutorial aprenderemos como usar las condicionales en Python.

Los programas anteriores solo tomaban en cuenta un único escenario. Los
problemas de la vida real presentan muchos escenarios y dependiendo de este,
el programa tiene que actuar de una forma u otra. Para que los programas puedan
adaptar su comportamiento y tomar decisiones dependiendo de las condiciones del
escenario se usan las *condicionales*.

Para entender las condicionales realicemos un programa que determine si una
persona puede votar o no, dependiendo de su edad. En la vida real existen más
condiciones para saber si una persona puede votar o no, pero para el
programa solo tomaremos en cuenta si la persona tiene 18 años o más. Si es así puede
votar, de lo contrario no puede votar.

El programa pedirá al usuario ingresar su edad. Si es mayor de 18 años el
programa debe imprimir **"Puedes votar"** de lo contrario debe imprimir 
**"No puedes votar"**.

En un archivo llamado `:::bash votar.py` Ingresa el siguiente código.

```python
--8<-- "content/code/python/votar.py"
```

El programa comienza pidiendo al usuario que ingrese su edad usando la función
`:::python input`, convirtiéndolo a entero usando la función `:::python int` y
guardando el valor en una variable llamada `:::python edad`. Enseguida, se usa
la sentencia `:::python if`, la cual evalúa la condición que la sigue
`:::python edad >= 18`, esta sentencia dará un valor de `:::python True` o
`:::python False`, verdadero o falso. 

El bloque de código que sigue la sentencia `:::python if` 
se ejecutará en caso de que la condición sea verdadera. 
Ahí es donde se imprime el mensaje **"Puedes votar"**, este
bloque de código debe de ir identado por un ++tab++. Después, está la 
sentencia `:::python else` la cual indica que el bloque indentado que la
siga se ejecutará en caso de que la condición evaluada sea falsa. 
Ahí es dónde se imprime el mensaje **"No puedes votar"**.
