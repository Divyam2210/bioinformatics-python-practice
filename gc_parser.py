def gc_content_parser(dna):

    dna = dna.upper().strip()

    if not dna:
        raise ValueError("Input DNA sequence is empty.")

    base_set = {'A', 'T', 'C', 'G'}
    for i in dna:
        if i not in base_set:
            raise ValueError(f"Invalid character '{i}' found in DNA sequence. Only A, T, C, G are allowed.")
    gc_count = dna.count('G') + dna.count('C')
    return round((gc_count / len(dna)) * 100, 2)



def main():
    while True:
        try:
            user_input = input("Enter a DNA sequence: ")
            gc_con = gc_content_parser(user_input)

        except ValueError as e:
            print(f"Error: {e}")
        else:
            print(f"GC content: {gc_con:.2f}%")
            break

main()