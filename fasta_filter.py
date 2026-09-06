valid_nucleotide = set('ATCG')


def validate_sequence(seq, header):
    if not seq:
        raise ValueError("The string is empty")
    for base in seq:
        if base not in valid_nucleotide:
            raise ValueError(f"Invalid Nucleotide found {base}")

def parse_seq(filepath: str) -> dict[str, str]:

    file_has_content = False
    current_header = None
    fasta = {}
    sequence_parts = []
    with open(filepath, 'r') as f:
        for line in f:

            if not line:
                continue

            file_has_content = True

            if line.startswith(">"):

                if current_header:
                    nucleotides = ''.join(sequence_parts).upper()
                    validate_sequence(nucleotides, current_header)
                    fasta[current_header] = nucleotides
                    sequence_parts = []
                current_header = line[1:].strip()

            else:
                if current_header is None:
                    raise ValueError("Invalid FASTA format: missing header line starting with '>'")
                sequence_parts.append(line.strip())


        if not file_has_content:
            raise ValueError("Invalid FASTA format: file is empty")

        if current_header:
            x = "".join(sequence_parts).upper()
            validate_sequence(x, current_header)
            fasta[current_header] = x   

    return fasta 


if __name__ == "__main__":
    result = parse_seq('example.fasta')
    print(result)
