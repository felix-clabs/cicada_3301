# Resultados del Plan Alternativo de Desencriptación

Se ha iniciado una estrategia alternativa centrada en el análisis estadístico y el uso de Python para mayor flexibilidad.

## Logros Iniciales
1.  **Transcripción Completa:** Se han extraído y organizado las transcripciones de las páginas 17 a 72 del Liber Primus, que antes no estaban disponibles en formato digital en este repositorio.
2.  **Herramientas de Investigación:** Se creó un conjunto de herramientas en `tool/python/` para:
    *   Cálculo del Índice de Coincidencia (IC).
    *   Análisis de frecuencia de runas.
    *   Búsqueda de "cribs" (palabras conocidas) con desplazamientos constantes.
    *   Desencriptación por secuencia de números primos y funciones totient de Euler.
3.  **Descubrimiento en la Página 71:**
    *   Se identificó que la Página 71 utiliza un cifrado de desplazamiento basado en números primos con un offset de 28.
    *   **Texto Parcialmente Descifrado:** "AN END WITHIN THE DEEP WEB THERE EXISTS A PAGE THAT HAS TO IT IS THE DUTY OF..."

## Análisis de la Página 17
*   La Página 17 presenta un IC bajo (~1.03), lo que indica un cifrado polialfabético o una doble encriptación.
*   Análisis de Kasiski/IC sugiere longitudes de clave probables de 16, 18 o 20 caracteres.

## Próximos Pasos Recomendados
*   Aplicar ataques de diccionario sobre la Página 17 usando las longitudes de clave identificadas.
*   Investigar si los números de la Página 16 (434, 1311, ...) actúan como una secuencia de saltos (offsets) para el Prime-shift.
*   Explorar la relación entre las páginas resueltas y el uso de Atbash antes de los desplazamientos.
