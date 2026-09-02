
#A "CpG site" is where a Cytosine is immediately followed by a Guanine along the 5' $\rightarrow$ 3' direction ("CG").

def count_dinucleotide(dna, dinucleotide):
    dna =  dna.upper().replace(" ", "")
    dinucleotide = dinucleotide.upper().replace(" ", "")

    for i in range(len(dna) - 1):
        if dna[i:i + 2] == dinucleotide:
            return dna.count(dinucleotide)


print(count_dinucleotide("ACGCGATCG", "CG"))  # Example usage

def longest_homopolymer(dna):
    dna = dna.upper().replace(" ", "")
    base = ""
    max_length = 1
    current_length = 1

    for i in range(1, len(dna)):
        if dna[i] == dna[i - 1]:
            current_length += 1
            
            if current_length > max_length:
                max_length = current_length
                base = dna[i]

        else:
            current_length = 1
            
    return base, max_length


print(longest_homopolymer("AAACCCGGGTTTAAA"))  # Example usage              



def sliding_window_gc_content(dna, window_size):
    dna = dna.upper().replace(" ", "")
    gc_contents = []

    for i in range(len(dna) - window_size + 1):
        window = dna[i:i + window_size]
        gc_content = (window.count('G') + window.count('C')) / window_size * 100
        gc_contents.append(gc_content)
    return gc_contents

print(sliding_window_gc_content("GCATGC", 4))
