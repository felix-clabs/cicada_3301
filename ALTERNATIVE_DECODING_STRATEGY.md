# Estrategia Alternativa de Desencriptación - Liber Primus (Cicada 3301)

Este documento detalla un enfoque alternativo para abordar las páginas no resueltas del Liber Primus (17-72), centrándose en vectores de ataque no convencionales y pistas poco explotadas.

## 1. Análisis de Audio (Vectores No Estándar)

A diferencia de la esteganografía clásica (Steghide, Mp3Stego), este plan propone tratar los archivos de audio como fuentes de datos puros.

### A. Mapeo de Frecuencias a Runas
- **Hipótesis:** Las frecuencias dominantes en ciertos intervalos de tiempo corresponden a índices en la tabla Gematria Primus.
- **Acción:** Desarrollar herramientas para extraer frecuencias (FFT) y normalizarlas al rango 0-28 (o al conjunto de números primos asociados a las runas).
- **Archivos Objetivo:** `interconnected.mp3`, `mp3stego.mp3`.

### B. Análisis de Intervalos y Ritmo
- **Hipótesis:** La duración de las notas o los silencios codifica información (similar al Código Morse pero usando la base rúnica).
- **Acción:** Analizar los archivos MIDI y convertirlos a secuencias numéricas para ataques de fuerza bruta Vigenere.

## 2. Análisis Estadístico y Lingüístico de Runas

### A. Análisis de Distribución de Frecuencia (FQA)
- **Hipótesis:** Aunque el cifrado sea polialfabético (como Vigenere), el uso de un lenguaje específico (Inglés/Léxico Cicada) deja huellas.
- **Acción:** Comparar el Índice de Coincidencia (IC) de las páginas no resueltas con las resueltas (0-16). Si el IC es similar, el desplazamiento es simple o la clave es corta.

### B. Diccionarios de Cicada
- **Hipótesis:** Las claves de las páginas restantes están ocultas en las páginas ya resueltas o en la estructura del libro (pág. 0, 57, etc.).
- **Acción:** Crear una herramienta que genere wordlists dinámicas basadas en el texto resuelto del Liber Primus para usarlas como claves en ataques Vigenere.

## 3. Búsqueda de Claves Dinámicas y Prime-Gematria

### A. Rotaciones basadas en Números Primos
- **Hipótesis:** El desplazamiento (Shift) de cada runa no es constante ni depende de una palabra clave, sino de la secuencia de números primos.
- **Acción:** Implementar un descifrador que use la secuencia de primos (2, 3, 5, 7...) como clave de desplazamiento sobre la tabla Gematria Primus.

### B. Cruce de Información (Cross-referencing)
- **Hipótesis:** Los números encontrados en páginas de "resumen" (como la 16 o la 5) son parámetros para algoritmos de audio o de generación de claves.
- **Acción:** Utilizar los números 434, 1311, 312, etc., como semillas para generadores de números pseudoaleatorios (PRNG) que podrían haber sido usados para el cifrado.

## 4. Hoja de Ruta de Implementación

1. **Fase 1:** Implementación de herramientas de análisis de frecuencia de runas en `tool/`.
2. **Fase 2:** Script de extracción de datos de audio (frecuencias/amplitud) a formato rúnico.
3. **Fase 3:** Ejecución de pruebas de fuerza bruta cruzadas entre páginas usando el léxico extraído.
