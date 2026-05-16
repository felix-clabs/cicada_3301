import os
import sys

# Add the tools directory to the path
sys.path.append(os.path.join(os.path.dirname(__file__)))

import gp_core
import ioc_scanner

def run_recon():
    markdown_dir = 'liber_primus/markdown/'
    files = sorted([f for f in os.listdir(markdown_dir) if f.endswith('.md') and f != 'README.md'])
    results = []
    for filename in files:
        filepath = os.path.join(markdown_dir, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        is_solved = "Plaintext" in content or "Translation:" in content or "Status: Decrypted" in content
        runes = gp_core.get_runes_from_text(content)
        indices = gp_core.runes_to_indices(runes)
        if not is_solved and len(indices) > 20:
            ioc = ioc_scanner.calculate_ioc(indices)
            kasiski = ioc_scanner.kasiski_examination(indices)
            results.append({
                'page': filename.replace('.md', ''),
                'ioc': ioc,
                'length': len(indices),
                'kasiski': kasiski
            })
    results.sort(key=lambda x: x['ioc'], reverse=True)
    print("Top 5 Most Vulnerable Pages (Highest IoC):")
    print("| Page | IoC (Base 29) | Length | Top Kasiski Factors |")
    print("|------|----------------|--------|---------------------|")
    for r in results[:5]:
        kasiski_str = ", ".join(map(str, r['kasiski']))
        print(f"| {r['page']} | {r['ioc']:.4f} | {r['length']} | {kasiski_str} |")

    solved_pages = []
    for filename in files:
        filepath = os.path.join(markdown_dir, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        if "Plaintext" in content or "Translation:" in content or "Status: Decrypted" in content:
            solved_pages.append(filename.replace('.md', ''))
    print(f"\nSolved pages detected: {', '.join(solved_pages)}")

if __name__ == "__main__":
    run_recon()
