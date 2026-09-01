def evalute_primer(primer):
    primer = primer.upper().strip()
    if 10 > len(primer) or len(primer)> 30:
        return "Invalid Primer Length"

    gc_count = primer.count("G") + primer.count("C")
    at_count = primer.count("A") + primer.count("T")

        
    tm = (gc_count * 4) + (at_count * 2)
        
    if tm >65:
        return "High Tm"
    elif 55 <= tm <= 65:
        return "Optimal Tm"
    else:
        return "Low Tm"


print(evalute_primer("ATGC"))                      # Output: Invalid Length
print(evalute_primer("ATGCGATCGATCGATCGATC"))
