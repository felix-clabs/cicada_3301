# Informe de Progreso - Fase 15: Nulos Intercalados y Transposición Doble en P20

## Poda Inteligente de Nulos (Smart Null Stripping)
Se han desarrollado técnicas para reducir las 263 runas de la P20 a una matriz simétrica de 256, buscando desalineamientos internos:
1.  **Filtro de Final de Línea:** Eliminación de la última runa de las primeras 7 líneas de la P20.
    *   *Resultado:* IC cae a 0.99 (desalinea la sustitución).
2.  **Filtro Fibonacci:** Eliminación de runas en posiciones correspondientes a la secuencia de Fibonacci.
    *   *Resultado:* IC se mantiene en **1.7192**, confirmando que la sustitución base es robusta a este tipo de poda puntual.

## Transposición Doble (Audio-Keyed)
Se implementó un motor de transposición doble que opera sobre la matriz 16x16:
*   **Clave de Columnas:** Derivada de los Delta Times del archivo MIDI.
*   **Clave de Filas:** Derivada de los valores de las Notas (Rank Order) del archivo MIDI.
*   **Observación:** La transposición doble aplicada sobre la poda Fibonacci mantiene la integridad estadística (IC 1.7), pero el texto semántico sigue oculto tras el reordenamiento.

## Estado de la Investigación
La Page 20 resiste la transposición lineal y doble basada en metadatos MIDI. El hecho de que la poda Fibonacci mantenga un IC alto sugiere que los caracteres "nulos" podrían estar siguiendo una progresión matemática, pero su eliminación no basta para alinear el texto horizontalmente.

## Herramientas Consolidadas
*   `matrix_preprocessor.py`: Ahora incluye filtros de poda selectiva (Fibonacci, Líneas).
*   `double_transposition_solver.py`: Motor de reordenamiento matricial por filas y columnas independientes.
