# Informe de Progreso - Fase 9: Análisis de Bloques y Permutaciones en P20

## Análisis del Bloque 0 (Página 20)
*   **Inventario de Caracteres:** El primer bloque de 28 runas (tras la sustitución con IC 1.7) presenta una composición rica en vocales:
    *   **Inventario de Vocales:** {'ᛁ': 2, 'ᛇ': 1, 'ᛖ': 9, 'ᚪ': 2, 'ᛡ': 1, 'ᛠ': 1}.
    *   Total vocales: 16 de 28 caracteres.
*   **Ataque de Esqueleto:** Se verificó la posibilidad de formar palabras clave del léxico Cicada:
    *   El Bloque 0 contiene los caracteres necesarios para formar la palabra **PILGRIM** y conectores como **THE** o **AND**.
    *   La alta densidad de la runa 'ᛖ' (E) sugiere una estructura gramaticalmente correcta pero desordenada localmente.

## Capa de Permutación Dinámica
*   Se ha implementado la función `dynamic_block_permutation` en `transposition_solver.py`.
*   Esta función permite reordenar los bloques de 28 caracteres basándose en secuencias externas (ej. derivadas de la amplitud o frecuencia del audio).

## Estado de la Investigación
La Página 20 se comporta como un cifrado de **Transposición de Bloques Fijos (28 caracteres)** sobre una sustitución polialfabética ya resuelta. La clave de la transposición es la pieza final.

## Herramientas Actualizadas
*   `transposition_solver.py`: Incluye análisis de esqueleto de palabras y ganchos para permutación dinámica por array.
