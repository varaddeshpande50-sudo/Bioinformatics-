# BioSeq Toolkit

A lightweight, beginner-friendly Python command-line tool for basic DNA sequence analysis. It reads multi-record FASTA files and exports reproducible CSV summaries for students learning computational biology.

## Features
- DNA length and nucleotide composition (A, C, G, T, N).
- GC percentage among known bases (N excluded; blank if all bases are unknown).
- Reverse complement and DNA-to-RNA letter conversion (coding-strand convention).
- Input validation and multi-line FASTA support.
- No third-party dependencies.

## Quick start
Requires Python 3.8 or newer.

```bash
python bioseq.py sample.fasta -o results.csv
python -m unittest -v
```

## Example results
| Record | Length | GC % |
| --- | ---: | ---: |
| synthetic_balanced | 8 | 50 |
| synthetic_gc_rich | 8 | 75 |
| synthetic_ambiguous | 6 | 50 |

The included sequences are synthetic educational examples, not clinical or experimental data. The full results are in `results.csv`.

## Reach and intended impact
This early-stage educational project aims to lower the barrier to FASTA analysis for biotechnology students and novice bioinformatics learners. It complements established packages such as Biopython by providing a transparent, dependency-free example, rather than replacing them. Adoption and download metrics have not been established.

## Limitations and roadmap
Supports A/C/G/T/N only; not a clinical tool or a gene prediction pipeline. Future work: support additional IUPAC ambiguity codes, sequence visualization, and documented examples using public reference sequences.

## Files
- `bioseq.py`: analysis and CLI
- `sample.fasta`: synthetic demo data
- `results.csv`: generated output
- `test_bioseq.py`: unit tests
- `LICENSE`: MIT license
