# Informe de Progreso - Fase 8: Transposición con Clave en P20

## Análisis de Transposición Columnar
*   **Método:** Se utilizó la clave de 28 posiciones obtenida del solver genético como clave de transposición.
*   **Resultados:**
    *   La reordenación de columnas basada en el rango de los valores de la clave (Keyed Columnar Transposition) no reveló texto legible en lecturas horizontales ni verticales.
    *   Se probaron variantes de extracción (Lectura por filas vs. Lectura por columnas reordenadas).

## Hipótesis de Transposición Intra-Bloque (Fase 8)
*   Se dividió el texto con IC 1.7 en bloques exactos de 28 caracteres.
*   **Observación:** El bloque 0 ("J E T F A L F IA/IO G I E I H AE R EO I E AE E J E M A E S/Z E N") contiene una alta densidad de vocales y letras comunes, pero no se ha encontrado una permutación local que forme palabras clave.

## Desafíos de la Página 20
Aunque la sustitución polialfabética de ciclo 28 ha sido resuelta estadísticamente (IC 1.7), el texto sigue desordenado. Esto indica que:
1.  La transposición es independiente de la clave de sustitución.
2.  La clave de 28 caracteres se deriva de un sistema dinámico (posiblemente audio o una página matemática como la 57) que aún no hemos mapeado correctamente a la rejilla espacial.

## Herramientas Consolidadas
*   `transposition_solver.py`: Implementación de transposición columnar con clave y análisis de chunks.
*   `capture_p20_key.py`: Extractor de claves óptimas por Hill Climbing.
