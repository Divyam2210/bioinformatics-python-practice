class IncompleteCodonCountError(Exception):
    pass

    
class UnknownCodonException(Exception):
    pass
def codon_check(dna):
        if len(dna) % 3 != 0:
            raise IncompleteCodonCountError("The codon sequence length is not a multiple of 3. Please provide a complete codon sequence.")
            
        
def  codon_in(dna):

        codons = {
            'AUG': 'Methionine',
            'UUU': 'Phenylalanine',
            'UAA': 'Stop',
            'UAG': 'Stop',
            'UGA': 'Stop',
            'UUC': 'Phenylalanine',
            'UUA': 'Leucine',
            'UUG': 'Leucine',
            'CUU': 'Leucine',
            'CUC': 'Leucine',
            'CUA': 'Leucine',
            'CUG': 'Leucine',
            'AUU': 'Isoleucine',
            'AUC': 'Isoleucine',
            'AUA': 'Isoleucine',
            'GUU': 'Valine',
            'GUC': 'Valine',
            'GUA': 'Valine',
            'GUG': 'Valine',
            'CCA': 'Proline',
            'CCG': 'Proline',
            'CCU': 'Proline',
            'CCC': 'Proline',
            'ACU': 'Threonine',
            'ACC': 'Threonine',
            'ACA': 'Threonine',
            'ACG': 'Threonine',

        }
        codon = dna.upper().strip()
        
        for i in range(0, len(codon)+1, 3):
            if codon[i:i + 3] not in codons and codon[i:i + 3] != '':
                raise UnknownCodonException(f"Unknown codon '{codon[i:i + 3]}' found in DNA sequence. Please provide a valid codon.")
            else:
                return f'the resulting peptide is {codons[codon[i:i + 3]]}'
        





def main():
    while True:
        try :
            user_inp =input("Enter a codon sequence: ")
            codon_check(user_inp)
            result = codon_in(user_inp)

        except (IncompleteCodonCountError, UnknownCodonException) as e:
            print(f"Error: {e}")
        else:
            print(result)
            break

main()