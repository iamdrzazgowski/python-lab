def are_complementary(base1, base2):
    complementary_pairs = {
        'a': 't',
        't': 'a',
        'c': 'g',
        'g': 'c'
    }
    return complementary_pairs.get(base1) == base2


def count_complementary(seq1, seq2, offset):
    matches = 0
    for i in range(len(seq1)):
        seq2_index = i + offset
        if 0 <= seq2_index < len(seq2):
            if are_complementary(seq1[i], seq2[seq2_index]):
                matches += 1
    return matches

def find_best(seq1, seq2):
    max_matches = 0
    for offset in range(-len(seq2) + 1, len(seq1)):
        matches = count_complementary(seq1, seq2, offset)
        if matches > max_matches:
            max_matches = matches
    return max_matches

seq1 = "aaaaaccccccccccttttt"
seq2 = "cccccccccccccccaaaaa"
best_matches = find_best(seq1, seq2)
print(f"best: {best_matches}")