# Informe de Progreso - Fase 13: Desbloqueo de Transposición 2D en P20

## Análisis de Matriz Columnar
*   Se implementó el descifrador de transposición columnar 2D manejando correctamente las columnas "largas" y "cortas" para un ancho de 28.
*   **Rutina de Ruteo MIDI:** Se aplicó el array de Delta Times [0, 18, 1, 19...] bajo múltiples interpretaciones geométricas:
    1.  Carga Vertical -> Lectura Horizontal.
    2.  Carga Horizontal -> Lectura Vertical.
    3.  Uso del array como Mapa de Posición Original vs. Mapa de Destino.

## Resultados de la Fase 13
*   **Alineación Estadística:** Todas las variantes mantienen el IC ideal de 1.7.
*   **Análisis Léxico:** Ninguna de las combinaciones automáticas con los arrays de audio actuales ha revelado oraciones coherentes en inglés rúnico.
*   **Conclusión:** La transposición de la Página 20 no es una simple permutación de columnas de ancho 28 basada directamente en los Delta Times MIDI.

## Hipótesis Evolucionada
Dada la ausencia de resultados con permutaciones lineales, es probable que:
1.  La matriz de transposición sea **cuadrada** (ej. 16x16 o similar) y las 263 runas contengan caracteres nulos o de relleno.
2.  La clave de transposición sea una **Espiral** o un patrón de **Ruta de Caballo** sobre una rejilla de ancho 28.

## Herramientas Actualizadas
*   `p20_columnar_2d.py`: Motor de transposición bidimensional con soporte para arrays externos y variantes de carga/lectura.
