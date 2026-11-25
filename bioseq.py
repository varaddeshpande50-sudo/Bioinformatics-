"""Educational DNA FASTA analysis using only the Python standard library."""
import argparse
import csv
from collections import Counter
from pathlib import Path


def read_fasta(path):
    name, parts = None, []
    with open(path, encoding='utf-8') as handle:
        for line in handle:
            line = line.strip()
            if not line:
                continue
            if line.startswith('>'):
                if name is not None:
                    yield name, ''.join(parts)
                name, parts = line[1:].strip(), []
                if not name:
                    raise ValueError('Empty FASTA header')
            else:
                if name is None:
                    raise ValueError('Missing FASTA header')
                parts.append(''.join(line.split()).upper())
    if name is None:
        raise ValueError('No FASTA records')
    yield name, ''.join(parts)


def analyse(name, seq):
    seq = seq.upper()
    if not seq or set(seq) - set('ACGTN'):
        raise ValueError(f'{name}: expected nonempty DNA using A, C, G, T or N')
    c = Counter(seq)
    known = len(seq) - c['N']
    return dict(record=name, length=len(seq), A=c['A'], C=c['C'], G=c['G'],
                T=c['T'], N=c['N'], gc_percent=round(100*(c['G']+c['C'])/known, 2) if known else None,
                reverse_complement=seq.translate(str.maketrans('ACGTN', 'TGCAN'))[::-1],
                rna=seq.replace('T', 'U'))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('fasta', type=Path)
    parser.add_argument('-o', '--output', type=Path, default=Path('results.csv'))
    args = parser.parse_args()
    try:
        rows = [analyse(name, seq) for name, seq in read_fasta(args.fasta)]
        with args.output.open('w', newline='', encoding='utf-8') as handle:
            writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
            writer.writeheader()
            writer.writerows(rows)
    except (OSError, ValueError) as exc:
        parser.exit(1, f'Error: {exc}\n')
    print(f'Analysed {len(rows)} records; saved {args.output}')


if __name__ == '__main__':
    main()
