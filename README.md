# Algoritmo Shunting Yard

## Definición
Algoritmo para convertir expresiones de infix (operadores entre operandos) a postfix (notación polaca inversa). Desarrollado por Edsger Dijkstra (1961).

## Cómo Funciona
1. Inicializar:
   - Cola de salida (output)
   - Pila para operadores (stack)

2. Reglas por Token:
   - Operando → Va al output
   - Operador → Se compara con la pila (precedencia)
   - "(" → Se apila
   - ")" → Desapilar hasta encontrar "("

3. Final: Vaciar la pila al output.

## Precedencia (Ejemplo)
| Operador | Ejemplo | Precedencia |
|----------|---------|-------------|
| *, /     | 4 * 2   | 3           |
| +, -     | 3 + 4   | 2           |

## Ejemplo Paso a Paso
Expresión Infix: 3 + 4 * 2

Token  Acción                  Output       Pila
-----  ----------------------  -----------  ------
3      Añadir a output         [3]          []
+      Apilar                  [3]          [+]
4      Añadir a output         [3, 4]       [+]
*      Apilar (* > +)          [3, 4]       [+, *]
2      Añadir a output         [3, 4, 2]    [+, *]
Final  Desapilar * y +         [3, 4, 2, *, +] []

Resultado Postfix: 3 4 2 * +


## Aplicaciones
- Calculadoras
- Compiladores (parser de expresiones)
- Conversión de regex (ej: (a|b)* → a b | *)

## Recursos
- https://www.youtube.com/watch?v=1VjJe1PeExQ 
