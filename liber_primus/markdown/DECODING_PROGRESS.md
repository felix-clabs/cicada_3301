# Informe de Progreso - Fase 3: Ataque Focalizado P17 (Modulo 18)

## Estado de la Página 17
*   **Longitud de Clave Identificada:** 18 (IC Promedio ~1.44).
*   **Análisis Columnar (Routine 1):**
    *   Se descompuso la página en 18 columnas y se aplicó análisis de Chi-cuadrado para cada una.
    *   La mejor clave encontrada eleva el IC global a **1.2971**, pero el texto aún no es legible.
    *   *Hipótesis:* La distribución del inglés en el Liber Primus varía significativamente entre secciones (Koans vs. Filosofía).

## Nuevas Rutinas Implementadas
1.  **Chi-Square Columnar:** Implementado en `phase3_attack_p17.py`.
2.  **Cyclic Prime-Shift (Len 18):** Se probaron los primeros 18 primos como clave cíclica (con y sin offset 28).
3.  **External Hook:** Función preparada para integrar flujos de datos externos (audio/PRNG).

## Validaciones y Hallazgos Secundarios
*   **Página 20:** Presenta una señal fortísima en **longitud 28** (IC 1.5363). Dado que el offset de la P71 fue 28, esta página es un candidato prioritario para un ataque Prime-shift similar.
*   **Página 71:** Confirmada como el "punto de anclaje" metodológico (Prime Shift + Offset 28).

## Próximos Pasos
*   Refinar la distribución de frecuencias para la Routine 1 usando sub-segmentos de texto (ej. solo el texto de 'The Loss of Divinity').
*   Ejecutar Routine 1 en la Página 20 usando longitud 28.
