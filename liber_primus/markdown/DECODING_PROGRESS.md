# Informe de Progreso - Fase 7: Capas de Transposición en P20

## Resumen Estadístico
*   **Sustitución:** Probablemente resuelta mediante Algoritmo Genético (Hill Climbing). Se ha alcanzado un **IC de 1.6994**, que es el objetivo estadístico para texto plano en inglés.
*   **Problema Actual:** El texto resultante ("ᚹᛡᚪᛈᚪᛚᚠ...") posee la distribución de letras correcta pero carece de sentido semántico, indicando una **Capa de Transposición**.

## Pruebas de Transposición Realizadas
1.  **Scytale / Columnar (Rutina 1):** Se probaron anchos de matriz de 2 a 50. No se detectaron secuencias de palabras legibles.
2.  **Boustrophedon Visual (Rutina 2):** Se aplicó inversión de líneas basada en las longitudes rúnicas de la imagen original [23, 21, 21, 24, 21, 22, 21, 23, 22, 22, 23, 20]. Sin éxito inmediato.
3.  **Anagramas (Rutina 3):** Se realizaron búsquedas de ventanas deslizantes para identificar palabras clave de Cicada.

## Hallazgos Técnicos
El hecho de que el IC sea alto (1.7) pero el texto ilegible sugiere que la transposición es **intra-bloque** o que la clave de 28 posiciones del Vigenère se aplicó sobre un texto ya transpuesto.

## Estado de las Herramientas
*   `transposition_solver.py`: Motor de búsqueda de patrones espaciales y Scytale.
*   `get_best_p20.py`: Extractor de la mejor hipótesis de sustitución.
