def filter_sequence(dna):
    fdna = dna.upper().replace(" ", "")
    
    for base in fdna:
        if base not in "ACGT":
            return "Invalid characters present"


    if len(fdna) < 15:
        return "Sequence is too short"
    gc_p = (fdna.count('G') + fdna.count('C')) / len(fdna) * 100

    if 40 > gc_p or gc_p > 60:
        return "GC content is not in the range of 40-60%"


    if fdna.count('A')/len(fdna) > 0.5:
        return "Adenine content is too high"
    elif fdna.count('T')/len(fdna) >0.5:
        return "Thymine content is too high"    
    elif fdna.count('C')/len(fdna) > 0.5:      
        return "Cytosine content is too high"
    elif fdna.count('G')/len(fdna) > 0.5:
        return "Guanine content is too high"

    else:
        return "Sequence is valid"
print(filter_sequence("AAAAACCCCGGGGTTTTT"))  # Example usage