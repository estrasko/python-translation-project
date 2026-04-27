#!/usr/bin/env python3

import sys
from find_orf import find_first_orf
from translate import translate_sequence
from find_orf import parse_sequence_from_path

def main():
    genetic_code = {
        'GUC': 'V', 'ACC': 'T', 'GUA': 'V', 'GUG': 'V', 'ACU': 'T', 'AAC': 'N',
        'CCU': 'P', 'UGG': 'W', 'AGC': 'S', 'AUC': 'I', 'CAU': 'H', 'AAU': 'N',
        'AGU': 'S', 'GUU': 'V', 'CAC': 'H', 'ACG': 'T', 'CCG': 'P', 'CCA': 'P',
        'ACA': 'T', 'CCC': 'P', 'UGU': 'C', 'GGU': 'G', 'UCU': 'S', 'GCG': 'A',
        'UGC': 'C', 'CAG': 'Q', 'GAU': 'D', 'UAU': 'Y', 'CGG': 'R', 'UCG': 'S',
        'AGG': 'R', 'GGG': 'G', 'UCC': 'S', 'UCA': 'S', 'UAA': '*', 'GGA': 'G',
        'UAC': 'Y', 'GAC': 'D', 'UAG': '*', 'AUA': 'I', 'GCA': 'A', 'CUU': 'L',
        'GGC': 'G', 'AUG': 'M', 'CUG': 'L', 'GAG': 'E', 'CUC': 'L', 'AGA': 'R',
        'CUA': 'L', 'GCC': 'A', 'AAA': 'K', 'AAG': 'K', 'CAA': 'Q', 'UUU': 'F',
        'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'GCU': 'A', 'GAA': 'E', 'AUU': 'I',
        'UUG': 'L', 'UUA': 'L', 'UGA': '*', 'UUC': 'F'
    }

    sequence_path = sys.argv[1]

    rna_sequence = parse_sequence_from_path(sequence_path)
    orf_sequence = find_first_orf(rna_sequence)
    amino_acid_sequence = translate_sequence(
        rna_sequence=orf_sequence,
        genetic_code=genetic_code,
    )

    sys.stdout.write(amino_acid_sequence + "\n")


if __name__ == "__main__":
    main()
