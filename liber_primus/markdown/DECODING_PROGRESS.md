# Informe de Progreso - Fase 18: Ataque KPA y Autokey en P20

## Resumen del Descubrimiento de la Clave
Se ha confirmado que la Página 20 posee un periodo rúnico de **28**, con un IC periódico de **1.7180**. La secuencia de 28 runas obtenida mediante el mapeo de puntos rojos y el descifrado con la P71 ("S D EA M C W L I Y...") ha sido identificada como una pieza fundamental del rompecabezas.

## Rutina 1: Ataque de Texto en Claro Conocido (KPA)
Se ha procedido a realizar ingeniería inversa de la clave matemática asumiendo que la secuencia extraída ($P$) es el texto en claro del primer bloque de 28 runas negras ($C$).
- **Clave Derivada (C - P):** `[20, 0, 8, 5, 13, 8, 15, 11, 3, 12, 0, 15, 11, 13, 5, 28, 6, 12, 8, 10, 8, 20, 7, 10, 0, 8, 15, 12]`
- **Análisis:** La aplicación de esta clave sobre el resto de la página no produjo un IC significativamente alto (~1.04), lo que sugiere que el crib no corresponde a la posición inicial o que el cifrado no es Vigenere puro.

## Rutina 2: Pruebas de Autoclave (Autokey)
Se evaluaron dos variantes de Autokey utilizando la secuencia de 28 runas como "Primer":
1.  **Plaintext Autokey:** La clave para cada bloque es el texto en claro del bloque anterior. (IC: 1.0455)
2.  **Ciphertext Autokey:** La clave para cada bloque es el texto cifrado del bloque anterior. (IC: 0.9980)

## Rutina 3: Desplazamiento Primario Dinámico (Prime G-Shift)
Se utilizó la secuencia de 28 runas convertida a sus valores primos como clave de desplazamiento.
- **Resultado:** IC 1.0526. Aunque bajo, es ligeramente superior al IC base, lo que justifica seguir explorando transformaciones basadas en primos.

## Próximos Pasos
- Explorar desplazamientos de la secuencia crib ($P$) a lo largo de las 240 runas negras para encontrar su posición correcta.
- Investigar si la clave verdadera $K$ es a su vez una secuencia de la Gematria Primus con significado léxico.
