# Informe de Progreso - Fase 4: Ataque Estructural P20

## Página 20: Análisis Estructural (Modulo 28)
*   **Anomalía Matemática:** La señal de IC en longitud 28 es persistente (1.5363). Dado que el alfabeto tiene 29 runas, un ciclo de 28 apunta a generadores de grupo multiplicativo.
*   **Cifrado Afín (Rutina 1):** Las pruebas de cifrado Afín simple ( = a^{-1}(c - b) \pmod{29}$) para valores fijos de $ y $ no elevaron el IC global. Esto sugiere que los parámetros $ o $ varían cíclicamente.
*   **Clave Alfabeto (Rutina 2):** Se descartó el uso del alfabeto rúnico o su secuencia de primos como clave Vigenère directa de longitud 28.
*   **Análisis Columnar Refinado (Rutina 3):**
    *   Se implementó un calificador basado en 3 perfiles rúnicos: Filosofía, Koans y Parábolas.
    *   El mejor ajuste columnar elevó el IC a **1.4368**. El texto resultante muestra fragmentos fonéticamente consistentes pero no palabras claras.

## Perfiles de Frecuencia Rúnica
Se han establecido tres distribuciones de referencia para el Liber Primus:
1.  **PHILOSOPHY_FREQ:** Basado en el texto de las páginas 0-13.
2.  **KOAN_FREQ:** Basado en las páginas 14-15.
3.  **PARABLE_FREQ:** Basado en la página 72.

## Estado de la Investigación
La Página 20 es un cifrado polialfabético de 28 alfabetos. La estructura del ciclo (28 = 29 - 1) es la pista clave. Los próximos esfuerzos deben centrarse en secuencias que exploten las raíces primitivas de 29 o progresiones matemáticas en el desplazamiento.

## Herramientas Desarrolladas
*   `affine_attack.py`: Motor de búsqueda de parámetros afines.
*   `columnar_refined.py`: Analizador de columnas con multi-perfil estadístico.
*   `primitive_root_attack.py`: Generador de secuencias basadas en raíces primitivas mod 29.
