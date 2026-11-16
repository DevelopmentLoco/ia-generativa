# ordenar.py
# Algoritmo para ordenar tres números enteros de menor a mayor.
# Se utilizan comparaciones e intercambios, sin listas ni ciclos.

a = int(input("Ingresa el primer número: "))
b = int(input("Ingresa el segundo número: "))
c = int(input("Ingresa el tercer número: "))

# Primera comparación: ordenar a y b
if a > b:
    auxiliar = a
    a = b
    b = auxiliar

# Segunda comparación: ordenar a y c
if a > c:
    auxiliar = a
    a = c
    c = auxiliar

# Tercera comparación: ordenar b y c
if b > c:
    auxiliar = b
    b = c
    c = auxiliar

print("Números ordenados de menor a mayor:", a, b, c)
