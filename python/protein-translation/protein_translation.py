TRANSLATION = {
    'AUG': 'Methionine',
    'UUU': 'Phenylalanine',
    'UUC': 'Phenylalanine',
    'UUA': 'Leucine',
    'UUG': 'Leucine',
    'UCU': 'Serine',
    'UCC': 'Serine',
    'UCA': 'Serine',
    'UCG': 'Serine',
    'UAU': 'Tyrosine',
    'UAC': 'Tyrosine',
    'UGU': 'Cysteine',
    'UGC': 'Cysteine',
    'UGG': 'Tryptophan',
    'UAA': 'INVALID',
    'UAG': 'INVALID',
    'UGA': 'INVALID',
}


def proteins(strand):
    acids = []
    for i in range(0, len(strand), 3):
        acid = TRANSLATION.get(strand[i:i + 3])
        if acid == 'INVALID':
            break
        acids.append(acid)

    return acids
