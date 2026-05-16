# Liber Primus Decoding Progress

**Date:** 2025-05-23

## PHASE 1: TOOLCHAIN FORGE

### Status: COMPLETED

The core cryptographic toolchain has been established in `tool/python/`. All existing artifacts have been audited and replaced with mathematically pure implementations supporting GP 2013/2014 and Autokey.

### Core Tools Developed:
- **`gp_core.py`**: Handles Gematria Primus alphabet mapping. Supports **GP 2014 (Phonemic, Base 29)** and **GP 2013 (Forward, Base 26)**.
- **`vigenere_engine.py`**: Modular 29 Vigenere processing. Supports standard repeating keys and **Autokey** (Plaintext-as-key).
- **`ioc_scanner.py`**: Normalized IoC calculation (Base 29) and Kasiski examination (GCD-based).
- **`baseline_recon.py`**: Automation script for manuscript entropy analysis.

### Baseline Reconnaissance Results (Top 5 Most Vulnerable)

| Page | IoC (Base 29) | Length (Runes) | Top Kasiski Factors |
|------|----------------|----------------|---------------------|
| 60 | 2.8098 | 272 | 2, 3, 5, 7, 4 |
| 50 | 2.6319 | 207 | 2, 4, 3, 19, 38 |
| 69 | 2.5745 | 253 | 2, 3, 5, 6, 4 |
| 44 | 2.5652 | 228 | 5, 3, 2, 9, 25 |
| 53 | 2.5572 | 229 | 2, 4, 13, 8, 26 |

### Solved Pages Detected:
The following pages contain verified plaintexts/translations and have been indexed for lexical analysis:
01, 03, 04, 05, 06, 07, 08, 09, 10, 11, 12, 13, 14, 15, 16, 73, 74.

---
*Ready for Phase 2: Structural and Lexical Analysis.*
