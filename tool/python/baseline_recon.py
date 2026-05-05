import os
import gp_core
import ioc_scanner

def get_unsolved_pages(directory):
    unsolved = []
    for filename in sorted(os.listdir(directory)):
        if filename.endswith(".md") and filename != "README.md":
            filepath = os.path.join(directory, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                if "**Status:** Not yet decrypted" in content:
                    unsolved.append((filename, content))
    return unsolved

def main():
    md_dir = "liber_primus/markdown/"
    unsolved = get_unsolved_pages(md_dir)

    results = []
    for filename, content in unsolved:
        runes = gp_core.get_runes_from_text(content)
        indices = [gp_core.rune_to_index(r) for r in runes]

        if not indices:
            continue

        ioc = ioc_scanner.calculate_ioc(indices)
        kasiski = ioc_scanner.kasiski_examination(indices)

        results.append({
            'page': filename.replace('.md', ''),
            'ioc': ioc,
            'kasiski': kasiski,
            'length': len(indices)
        })

    # Sort by IoC descending
    results.sort(key=lambda x: x['ioc'], reverse=True)

    print("| Page | IoC (Base 29) | Length | Top Kasiski Factors |")
    print("|------|----------------|--------|---------------------|")
    for r in results[:10]:
        k_str = ", ".join([str(f[0]) for f in r['kasiski']])
        print(f"| {r['page']} | {r['ioc']:.4f} | {r['length']} | {k_str} |")

if __name__ == "__main__":
    main()
