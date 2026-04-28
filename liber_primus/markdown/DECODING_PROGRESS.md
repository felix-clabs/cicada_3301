# Informe de Progreso - Fase 3: Ataque sobre la Página 17

## Análisis Estadístico de la Página 17
*   **IC Base:** 1.0330 (Cifrado polialfabético confirmado).
*   **Análisis de Kasiski / Friedman:**
    *   Longitud 18: IC Promedio **1.4451** (Señal más fuerte)
    *   Longitud 16: IC Promedio 1.3435
    *   Longitud 20: IC Promedio 1.3299

## Resultados de las Rutinas de Ataque
1.  **Ataque de Diccionario:** No se detectaron coincidencias legibles usando combinaciones de palabras clave de Cicada (DIVINITY, PILGRIM, etc.) para longitudes 16, 18 y 20.
2.  **Ataque PRNG:** Las semillas de la página 16 (434, 1311...) no produjeron texto en claro mediante generadores LCG o MT estándar.

## Validaciones Exitosas
*   **Página 71:** Confirmada y descifrada usando **Prime Shift (offset 28)**.
*   **Página 72:** Confirmada como texto en claro (The Parable).

## Herramientas en `tool/python/`
*   `rune_tools.py`: Librería base para Gematria Primus e IC.
*   `vigenere_brute.py`: Analizador de longitud de clave.
*   `phase3_attack_p17.py`: Script de ataque automatizado para la página 17.
