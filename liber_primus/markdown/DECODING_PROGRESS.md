# Informe de Progreso - Fase 11: Análisis Profundo de Audio y Regex en P20

## Extracción de Metadatos de Audio
Se han implementado extractores para capas más profundas de esteganografía rítmica:
1.  **MIDI Delta Times:** Genera un array de permutación basado en los intervalos de ticks entre eventos Note-on.
    *   Array: [0, 18, 1, 19, 26, 2, 9, 10, 25, 27, 11, 24, 3, 4, 20, 7, 12, 21, 13, 22, 5, 16, 23, 17, 6, 8, 14, 15]
2.  **Audio Byte Rank (WAV):** Basado en el orden de rango de los primeros 28 bytes de datos de `steghide.wav`.
    *   Array: [0, 1, 2, 3, 27, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]

## Resultados de Ruteo Dinámico
*   La aplicación de los nuevos arrays de audio al Bloque 0 de la Página 20 altera significativamente la disposición de las 9 vocales 'E', pero no ha generado por sí sola la palabra **EMERGENCE** en posiciones lineales.
*   **Observación:** La falta de ciertos caracteres (ej. 'U' en el Bloque 0) sugiere que algunas palabras clave pueden estar divididas entre bloques o que la sustitución base requiere un ajuste fino.

## Motor de Anclaje Regex
Se ha preparado la infraestructura para búsquedas guiadas por patrones. El Bloque 0 posee la runa G (ᚷ) y abundantes E's, lo que mantiene viva la hipótesis de la palabra clave oculta.

## Herramientas Consolidadas
*   `csv_rank_extractor.py`: Ahora soporta análisis de Delta Times.
*   `lsb_array_extractor.py`: Extracción de secuencias binarias de audio.
*   `regex_anchor_attack.py`: Validador de patrones de esqueleto.
