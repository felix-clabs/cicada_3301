# Informe Técnico: Análisis de la Página 20 con Clave de 28 Runas

## 1. Validación de la Clave
La clave extraída de los 28 puntos rojos (10-9-9) en P20 es:
Latin: S/Z D EA M C/K W L I Y TH D EA F S/Z O J AE U G T M NG/ING T TH NG/ING R G G

## 2. Análisis Estadístico (IC)
- IC Base (P20 Completa): 1.0303
- IC Periódico (Periodo 28): 1.7180
El alto IC periódico confirma matemáticamente que la Página 20 utiliza un ciclo de 28 caracteres.

## 3. Resultados de Rutinas
### Routine 1: Vigenère Attack
Se aplicó la clave como desplazamiento cíclico (Suma/Resta).
- Resultado: IC ~1.02. No se detectó alineación léxica inmediata.
### Routine 2: Columnar Transposition
Se usó la clave para reordenar 28 columnas de la matriz 8x28.
- Lectura Horizontal: Genera secuencias rúnicas con IC ~1.02.
- Lectura Vertical: Genera secuencias rúnicas con IC ~1.02.

## 4. Conclusión Técnica
Aunque la clave de 28 runas es el periodo exacto del cifrado (confirmado por IC 1.71), su aplicación directa mediante Vigenère o Transposición simple no ha revelado el texto en claro. Esto sugiere que la clave de 28 runas podría ser:
1. Una clave de autotransposición (Autokey).
2. Un índice para un diccionario externo.
3. Una clave que requiere un desplazamiento adicional (G-Shift) basado en otra página (ej. P71 o P0).
