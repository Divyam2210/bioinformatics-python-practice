def check_cleavage_suitability(dna, site, position):
    dna= dna.upper().replace(" ", "")
    site= site.upper().replace(" ", "")
    if site not in dna :
        return "Restriction site not found in the DNA sequence."
    elif position <=3 or position >= len(dna)-3:
        return "Position is too close to the ends of the DNA sequence."
    if dna.count(site) > 1:
        return "Restriction site occurs multiple times in the DNA sequence."

    return "Cleavage site is suitable for restriction enzyme activity."

print(check_cleavage_suitability("ACGTACGTGCGTACGTA", "GCGT", 8))
