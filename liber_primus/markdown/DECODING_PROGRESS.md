# Informe de Progreso - Fase 14: Matrices 16x16 y Cifrados de Ruta en P20

## Pre-procesamiento de Matriz
*   Se identificó que la Página 20 (263 runas) requiere la eliminación de 7 caracteres nulos para formar una matriz simétrica de 16x16 (256 runas).
*   Se generaron tres variantes de matriz 16x16:
    1.  **Trim First 7:** Eliminación de las primeras 7 runas.
    2.  **Trim Last 7:** Eliminación de las últimas 7 runas.
    3.  **Frequency Trim:** Eliminación de las primeras 7 apariciones de la runa 'ᛖ' (E).

## Cifrados de Ruta (Route Ciphers)
Se implementaron y ejecutaron los siguientes algoritmos de extracción sobre las matrices simétricas:
1.  **Spiral Inward:** Lectura en espiral desde las esquinas hacia el centro.
2.  **Knight's Tour:** Extracción siguiendo la Ruta del Caballo de ajedrez (algoritmo de Warnsdorff).
3.  **Columnar:** Lectura vertical de la matriz cuadrada.

## Hallazgos Técnicos
*   **Convergencia de IC:** Todas las rutas mantienen un Índice de Coincidencia alto (~1.68 - 1.71), confirmando que la distribución de letras es correcta.
*   **Estado Semántico:** Aunque el IC es óptimo, las rutas probadas no han revelado palabras legibles contiguas.
*   **Implicación:** Es posible que la transposición no sea una ruta geométrica simple, sino una permutación basada en una clave externa (ej. audio) aplicada a la matriz 16x16, o que las 7 runas nulas no estén al principio/final sino intercaladas.

## Herramientas Consolidadas
*   `matrix_preprocessor.py`: Generador de matrices simétricas.
*   `route_cipher_solver.py`: Motor de extracción por rutas (Spiral/Knight/Columnar).
