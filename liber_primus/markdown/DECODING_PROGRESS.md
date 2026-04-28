# Informe de Progreso - Fase 10: Ruteo de Audio a Transposición en P20

## Extracción de Claves de Audio
Se han desarrollado e implementado dos rutinas de extracción de datos binarios para generar el array de permutación de 28 posiciones:
1.  **Audio Transients (Time-Domain):** Basado en los intervalos entre los primeros 28 picos de amplitud de `steghide.wav`.
    *   Array: [27, 0, 12, 24, 1, 13, 5, 20, 2, 17, 23, 3, 18, 6, 25, 14, 10, 26, 15, 11, 21, 7, 16, 8, 22, 4, 19, 9]
2.  **MIDI Note Order (Event-Domain):** Basado en el rango de los valores de las primeras 28 notas del archivo `song.csv`.
    *   Array: [15, 9, 3, 0, 19, 20, 21, 7, 1, 22, 10, 26, 2, 16, 11, 27, 4, 23, 17, 12, 18, 8, 24, 5, 13, 14, 25, 6]

## Resultados de las Pruebas de Permutación
*   Se aplicaron los arrays resultantes al Bloque 0 de la Página 20.
*   **Observación:** Aunque las permutaciones alteran la estructura fonética, no se ha logrado la alineación inmediata de palabras clave como "EMERGENCE" o "PILGRIM".
*   **Conclusión:** La estructura de la transposición es intra-bloque (28), pero el array de control podría estar en una propiedad de audio diferente (ej. fase, frecuencias específicas FFT) o en un desplazamiento de bit específico de los archivos MP3.

## Herramientas de Integración
*   `audio_rank_extractor.py`: Analizador de formas de onda (.wav).
*   `csv_rank_extractor.py`: Analizador de eventos MIDI (.csv).
*   `audio_permutation_attack.py`: Orquestador de ataques de ruteo dinámico.
