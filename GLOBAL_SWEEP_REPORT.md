# GLOBAL VULNERABILITY SWEEP REPORT (P17-P72)

## 1. Top 5 Vulnerable Pages (Highest IoC)
IoC values normalized to alphabet size 29. Values closer to 1.7-2.0 indicate lower entropy.

| Rank | Page | IoC | Probable Key Lengths (Kasiski) |
|---|---|---|---|
| 1 | 72 | 1.8186 |  |
| 2 | 70 | 1.0989 |  |
| 3 | 51 | 1.0437 | 7, 29 |
| 4 | 58 | 1.0437 | 3, 2, 5, 10 |
| 5 | 30 | 1.0435 | 3, 11 |

## 2. Technical Observations
- **Routine 1:** Identified potential weak links based on character distribution.
- **Routine 2:** Kasiski estimation reveals periodicity patterns in high-IoC candidates.
- **Routine 3:** Balanced N-Gram Fitness Function with Consonant Penalty has been registered for future decryption attempts.
