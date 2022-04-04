# Ejemplo de clase no trivial en Python

from math import gcd
from functools import total_ordering

@total_ordering
class Racional:

    def __init__(self, numerador=0, denominador=1):
        signo = -1 if numerador * denominador < 0 else 1
        numerador = abs(numerador)
        denominador = abs(denominador)
        comun = gcd(numerador, denominador)
        self.__numerador = numerador // comun * signo
        self.__denominador = denominador // comun

    def __str__(self):
        return f'{self.__numerador}/{self.__denominador}'

    def __eq__(self, other):
        return (self.__numerador == other.__numerador and
            self.__denominador == other.__denominador)

    def __lt__(self, other):
        return (self.__numerador * other.__denominador
            < self.__denominador * other.__numerador)

    def __add__(self, other):
        return Racional(
            self.__numerador * other.__denominador +
                self.__denominador * other.__numerador,
            self.__denominador * other.__denominador)

# Ejemplos de uso

a = Racional()
print(f'a:         {a}')
b = Racional(1, 2)
print(f'b:         {b}')
c = Racional(1, -3)
print(f'c:         {c}')
d = b + c
print(f'd = b + c: {d}')
e = Racional(1, 6)
print(f'e:         {e}')
print(f'e == d:    {e == d}')
print(f'd != e:    {d != e}')
print(f'c < b:     {c < b}')
print(f'e <= d:    {e <= d}')
print(f'c > b:     {c > b}')
print(f'e >= d:    {e >= d}')
