Title: Condicionales en Python
Date: 2026-05-04
Category: Python
Status: draft
Tags: Python, Tutorial, Programación
Summary: Un programa tiene que adaptarse a distintas situaciones, adaptando su comportamiento según el escenario, para ello se usan las condicionales, en este tutorial aprenderemos como usar las condicionales en Python.

Nuestros programas anteriores solo tomaban en cuenta un único escenario, los problemas de la vida real nos presentan muchos escenarios y dependiendo de este, tenemos que actuar de una forma u otra. Para que nuestros programas puedan adaptar su comportamiento y tomar decisiones dependiendo de las condiciones del escenario se usan las *condicionales*.

Para entender las condicionales realicemos un programa que determine si una
persona puede votar o no, dependiendo de su edad. En la vida real existen más
condiciones para saber si una persona puede votar o no, pero para nuestro
programa solo tomaremos en cuenta si la persona tiene 18 años o más, puede
votar, de lo contrario no puede votar.

Nuestro programa pedirá al usuario ingresar su edad. Si mayor de 18 años el programa debe imprimir **"Puedes votar"** de lo contrario debe de imprimir **"No puedes votar"**.

En un archivo llamado `:::bash votar.py` Ingresa el siguiente código

```python
--8<-- "content/code/python/votar.py"
```

Nuestro programa comienza pidiendo al usuario que ingrese su edad usando la función `:::python input`, convirtiendolo a entero usando la función `:::python int` y guardando el valor en una variable llamada
`:::python edad`
