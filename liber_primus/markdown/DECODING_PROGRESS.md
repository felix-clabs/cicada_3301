# Informe de Progreso - Análisis Criptográfico LP2

## Página 71: RESUELTA
*   **Método:** Prime Shift (sustracción) con un offset constante de 28.
*   **Texto:** "AN END WITHIN THE DEEP WEB THERE EXISTS A PAGE THAT HAS TO IT IS THE DUTY OF..."
*   **Significado:** Valida el uso de desplazamientos matemáticos dinámicos y el número 28 como constante clave.

## Página 20: ALTA PRIORIDAD
*   **Anomalía:** Señal de IC masiva en longitud **28** (IC 1.5363).
*   **Estado:** El análisis columnar (Chi-Square) eleva el IC a 1.4368. Se ha verificado que no es un Prime Shift simple.
*   **Hipótesis:** Cifrado polialfabético con ciclo de 28 posiciones. Dada la coincidencia con el offset de la P71, la clave de 28 podría estar relacionada con la estructura del alfabeto (29 runas - 1).

## Página 17: Cifrado Modulo 18
*   **Estado:** Longitud de clave 18 (IC 1.4451).
*   **Pruebas Realizadas:**
    *   Autoclave (Texto claro y Cifrado): Sin resultados.
    *   Análisis Columnar: IC mejorado a 1.2971.
    *   Ataque de Diccionario: Las palabras clave de Cicada no producen texto legible.
*   **Conclusión:** Requiere una clave numérica de 18 dígitos no derivada del léxico estándar.

## Distribución de Frecuencias Refinada
Se han generado perfiles de frecuencia para tres estilos detectados:
1.  **Filosofía:** Basado en páginas 0-13.
2.  **Koans:** Basado en páginas 14-15.
3.  **Parábolas:** Basado en la página 72.
Estos perfiles están integrados en las herramientas de `tool/python/`.

## Herramientas Actualizadas
*   `phase3_attack_p17.py`: Ahora incluye rutinas de Chi-Square y Prime-Shift cíclico.
*   `vigenere_brute.py`: Analizador universal de longitud de clave e IC.
