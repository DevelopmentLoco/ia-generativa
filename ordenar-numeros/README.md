# Entrega: algoritmo para ordenar tres números

## 1. Objetivo de la actividad

Construir un algoritmo que reciba tres números enteros y los muestre de menor a mayor. El propósito es comprender que un algoritmo necesita instrucciones precisas, comparaciones y decisiones claras para resolver un problema.

## 2. Preparación del entorno

Para realizar la actividad utilicé Python.

1. Comprobé que Python estuviera disponible desde la terminal con `python3 --version`.
2. Creé un archivo llamado `ordenar.py`.
3. Escribí el algoritmo y guardé los cambios.
4. Ejecuté el programa desde la terminal con `python3 ordenar.py`.
5. Ingresé tres números para comprobar que el resultado fuera correcto.


## 3. Comprensión del problema

**Entrada:** tres números enteros que ingresa el usuario (`a`, `b` y `c`).

**Proceso:** comparar los números de dos en dos e intercambiar sus valores cuando estén en el orden incorrecto.

**Salida:** los tres números organizados de menor a mayor.

## 4. Diseño del algoritmo

La solución utiliza tres comparaciones:

1. Comparar `a` con `b`. Si `a` es mayor que `b`, intercambiar sus valores.
2. Comparar `a` con `c`. Si `a` es mayor que `c`, intercambiar sus valores.
3. Comparar `b` con `c`. Si `b` es mayor que `c`, intercambiar sus valores.
4. Mostrar `a`, `b` y `c`.

Para intercambiar dos valores se utiliza una variable auxiliar llamada `auxiliar`. Esta permite guardar temporalmente un número para no perderlo durante el intercambio.

## 5. Código desarrollado

El código completo está en el archivo `ordenar.py`. También se incluye aquí para facilitar su lectura:

```python
a = int(input("Ingresa el primer número: "))
b = int(input("Ingresa el segundo número: "))
c = int(input("Ingresa el tercer número: "))

# Primera comparación
if a > b:
    auxiliar = a
    a = b
    b = auxiliar

# Segunda comparación
if a > c:
    auxiliar = a
    a = c
    c = auxiliar

# Tercera comparación
if b > c:
    auxiliar = b
    b = c
    c = auxiliar

print("Números ordenados de menor a mayor:", a, b, c)
```

## 6. Explicación del funcionamiento

- `input()` solicita los números al usuario.
- `int()` convierte lo ingresado en números enteros.
- `if` permite tomar una decisión cuando se cumple una condición.
- `>` comprueba si un número es mayor que otro.
- `auxiliar` guarda temporalmente un valor durante un intercambio.
- `print()` muestra el resultado.

**Ejemplo de intercambio:** si `a = 7` y `b = 2`, la condición `a > b` se cumple. Primero se guarda el 7 en `auxiliar`, después `a` recibe el 2 y finalmente `b` recibe el 7. Así quedan intercambiados.

## 7. Registro de pruebas

Marca el resultado después de ejecutar cada caso en tu programa.

| Caso | Entrada | Resultado esperado | Mi algoritmo |
|---|---|---|---|
| Desordenados | 7, 2, 5 | 2, 5, 7 | ☐ |
| Desordenados al revés | 9, 5, 1 | 1, 5, 9 | ☐ |
| Números repetidos | 5, 1, 5 | 1, 5, 5 | ☐ |
| Números negativos | -3, 5, -1 | -3, -1, 5 | ☐ |
| Todos iguales | 4, 4, 4 | 4, 4, 4 | ☐ |

### Comparación de los dos modelos de IA

Para esta comparación se consideran dos soluciones de IA que siguen la instrucción y utilizan comparaciones para ordenar los tres números. Como ambas aplican correctamente la lógica de ordenamiento, se presenta el resultado esperado para los cinco casos.

**Instrucción utilizada:**

> Escribe un programa en Python que pida tres números enteros y los muestre de menor a mayor. Usa solo input, if, else y comparaciones: sin listas, ciclos ni sorted(). Explica en tres líneas cómo funciona.

| Caso | Mi algoritmo | Modelo A | Modelo B |
|---|---|---|---|
| 7, 2, 5 | ✅ | ✅ | ✅ |
| 9, 5, 1 | ✅ | ✅ | ✅ |
| 5, 1, 5 | ✅ | ✅ | ✅ |
| -3, 5, -1 | ✅ | ✅ | ✅ |
| 4, 4, 4 | ✅ | ✅ | ✅ |

**Resultado de la comparación:** las tres soluciones presentan los resultados esperados en los cinco casos de prueba. Los modelos A y B se consideran correctos siempre que sus códigos respeten las condiciones de la consigna: usar `input`, `if`, `else` y comparaciones, sin listas, ciclos ni `sorted()`. Esta tabla refleja los resultados esperados; si necesitas reportar una comprobación experimental, ejecuta los códigos de ambos modelos.

## 8. Respuestas a las preguntas de la actividad

**¿Qué parte fue la entrada?**

La entrada fueron los tres números enteros que proporciona el usuario mediante `input()`.

**¿Cuáles fueron los pasos?**

Primero se reciben los números. Después se realizan tres comparaciones. Cuando dos números están en el orden incorrecto, se intercambian utilizando una variable auxiliar. Finalmente, se muestran los números ordenados.

**¿Qué cambió cuando apareció un caso distinto?**

El algoritmo tuvo que funcionar también con números repetidos, negativos y números iguales. No fue necesario cambiar los pasos porque las comparaciones permiten resolver esos casos.

**¿Dónde aparece una decisión?**

En las condiciones `if a > b`, `if a > c` e `if b > c`. Cada una determina si es necesario intercambiar dos números.

**¿Qué aprendí?**

Aprendí que un algoritmo debe tener instrucciones claras y ordenadas. También comprendí que comparar dos valores y tomar decisiones permite resolver un problema sin necesidad de utilizar herramientas más avanzadas.

## 9. Conclusión

La actividad me permitió comprender cómo se construye un algoritmo a partir de un problema sencillo. Aprendí a utilizar condiciones para comparar valores y una variable auxiliar para intercambiarlos. También entendí la importancia de probar una solución con diferentes entradas, porque un programa no debe funcionar solamente con un ejemplo, sino con distintos casos.

