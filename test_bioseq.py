import unittest
from pathlib import Path
from tempfile import TemporaryDirectory
from bioseq import analyse, read_fasta


class TestBioSeq(unittest.TestCase):
    def test_balanced(self):
        row = analyse('x', 'ATGC')
        self.assertEqual(row['gc_percent'], 50)
        self.assertEqual(row['reverse_complement'], 'GCAT')
        self.assertEqual(row['rna'], 'AUGC')

    def test_ambiguous(self):
        self.assertEqual(analyse('x', 'GCNN')['gc_percent'], 100)
        self.assertIsNone(analyse('x', 'NN')['gc_percent'])

    def test_invalid(self):
        for seq in ('', 'AX', 'AU'):
            with self.assertRaises(ValueError):
                analyse('x', seq)

    def test_multiline_fasta(self):
        with TemporaryDirectory() as d:
            path = Path(d) / 'demo.fa'
            path.write_text('>first\nat\ngc\n>second\nGG\n')
            self.assertEqual(list(read_fasta(path)), [('first', 'ATGC'), ('second', 'GG')])

    def test_missing_header(self):
        with TemporaryDirectory() as d:
            path = Path(d) / 'demo.fa'
            path.write_text('ATGC\n')
            with self.assertRaises(ValueError):
                list(read_fasta(path))

if __name__ == '__main__':
    unittest.main()
