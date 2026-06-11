from Bio.Seq import Seq
dna = Seq("GAGCTGTGACTGCGCCATGGGGCTCAGCGACGGGGAATGGCAGTTGGTGCTGAACGTCTGGGGGAAGGTG")
print("Reverse complement=",dna.reverse_complement())
