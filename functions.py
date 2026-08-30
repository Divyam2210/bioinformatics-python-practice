def clean_dna(dna):
    x = dna.strip().upper()

    return x

def get_length(dna):
    return len(dna)

def calculate_ratio(dna):
    for i in dna:
        if i in "GC":
            y = dna.count("G") + dna.count("C")
            z = dna.count("A") + dna.count("T")
            if z == 0:
                return 0.0
            ratio = round(y/z, 2)

    return ratio
def get_gc_percentage(dna):
    gc_count = dna.count("G") + dna.count("C")
    total_count = len(dna)
    if total_count == 0:
        return 0.0
    gc_percentage = (gc_count / total_count) * 100
    return round(gc_percentage, 2)

def generate_report(sequence_name, dna):
    cleaned_dna = clean_dna(dna)
    length = get_length(cleaned_dna)
    gc_percentage = get_gc_percentage(cleaned_dna)
    ratio = calculate_ratio(cleaned_dna)

    report = f"Report for {sequence_name}:\n"
    report += f"Length: {length}\n"
    report += f"GC Percentage: {gc_percentage}%\n"
    report += f"GC Ratio: {ratio}\n"

    return report

print(generate_report("Sample Sequence", "ACGTACGTGCGTACGTA"))