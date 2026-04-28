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

## Análisis Matemático de la Página 20 (Fase 5)
*   **Ataque de Raíces Primitivas:** Se generaron y probaron secuencias exponenciales (^i \pmod{29}$) para las 12 raíces primitivas de 29.
    *   No se detectaron aumentos significativos del IC (>1.55) bajo este modelo de clave cíclica pura.
    *   Las distancias Chi-cuadrado respecto a los perfiles de  y  se mantuvieron en niveles de ruido.
*   **Cifrado Afín Progresivo:** Se exploró el modelo  = a^{-1}(c - (b + i \cdot step)) \pmod{29}$. No se encontraron coincidencias.
*   **Cruces Inter-páginas:** Se utilizaron los números de la Página 5 como clave Vigenère sobre la P20 sin éxito.

## Conclusión Técnica (P20)
Aunque la señal de longitud 28 es robusta, la clave no sigue una progresión aritmética o exponencial simple basada en raíces primitivas. La clave de 28 posiciones es probablemente:
1. Una secuencia de una página aún no resuelta o un dato externo.
2. Un PRNG más complejo (ej. BBS o un LCG con parámetros desconocidos).
3. Una permutación del alfabeto rúnico específica.

## Estado de las Herramientas
*   `primitive_root_v2.py`: Motor de ataque exponencial modular.
*   `affine_progressive.py`: Buscador de transformaciones lineales dinámicas.

## Análisis Matemático de la Página 20 (Fase 5)
*   **Ataque de Raíces Primitivas:** Se generaron y probaron secuencias exponenciales ($g^i \pmod{29}$) para las 12 raíces primitivas de 29.
    *   No se detectaron aumentos significativos del IC (>1.55) bajo este modelo de clave cíclica pura.
    *   Las distancias Chi-cuadrado respecto a los perfiles de PHILOSOPHY y KOAN se mantuvieron en niveles de ruido.
*   **Cifrado Afín Progresivo:** Se exploró el modelo $p = a^{-1}(c - (b + i \cdot step)) \pmod{29}$. No se encontraron coincidencias.
*   **Cruces Inter-páginas:** Se utilizaron los números de la Página 5 como clave Vigenère sobre la P20 sin éxito.

## Conclusión Técnica (P20)
Aunque la señal de longitud 28 es robusta, la clave no sigue una progresión aritmética o exponencial simple basada en raíces primitivas. La clave de 28 posiciones es probablemente una secuencia de una página aún no resuelta o un dato externo.

## Estado de las Herramientas
*   `primitive_root_v2.py`: Motor de ataque exponencial modular.
*   `affine_progressive.py`: Buscador de transformaciones lineales dinámicas.

## Análisis Heurístico de la Página 20 (Fase 6)
*   **Algoritmo Genético (Hill Climbing):** Se implementó un motor de evolución de claves de 28 posiciones optimizando el IC y la distancia Chi-cuadrado contra perfiles nativos.
*   **Convergencia:** El algoritmo converge rápidamente hacia un IC de **1.6994** (casi idéntico al inglés estándar).
*   **Resultados:** Aunque el IC es ideal, el texto resultante sigue careciendo de estructura semántica clara (ej: "C/K E J F A L E IA/IO T I W I...").
*   **Interpretación:** Esto sugiere que la Página 20 podría tener una capa adicional de transposición de filas/columnas o que la clave no es Vigenère simple, sino que afecta a las runas de forma no lineal.

## Estado de las Herramientas
*   `genetic_solver_p20.py`: Motor heurístico de alto rendimiento para búsqueda de claves de longitud 28.
