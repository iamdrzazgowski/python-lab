def read_data(file_path):
    with open(file_path, 'r') as file:
        data = [line.strip().split(',') for line in file.readlines()]
    return data


def write_results(file_path, results):
    with open(file_path, 'w') as file:
        for result in results:
            file.write(f"{result['pair_num']}\t{result['max_score']}\t{result['shift']}\n")
            file.write(f"{result['seq1']}\n")
            file.write(f"{result['aligned']}\n")
            file.write(f"{result['seq2']}\n\n")


def score_alignment(seq1, seq2):
    return sum(1 for a, b in zip(seq1, seq2) if a == b)


def align_sequences(seq1, seq2):
    max_score = 0
    best_shift = 0
    best_aligned = ""

    # Try all possible shifts
    for shift in range(-len(seq2) + 1, len(seq1)):
        if shift < 0:
            aligned_seq2 = " " * abs(shift) + seq2
            aligned_seq1 = seq1
        else:
            aligned_seq1 = " " * shift + seq1
            aligned_seq2 = seq2

        # Align sequences to the same length for scoring
        if len(aligned_seq1) > len(aligned_seq2):
            aligned_seq2 += " " * (len(aligned_seq1) - len(aligned_seq2))
        else:
            aligned_seq1 += " " * (len(aligned_seq2) - len(aligned_seq1))

        current_score = score_alignment(aligned_seq1, aligned_seq2)

        if current_score > max_score:
            max_score = current_score
            best_shift = shift
            best_aligned = aligned_seq1.replace(' ', '-') + "\n" + "".join(
                "|" if a == b and a != ' ' else " " for a, b in
                zip(aligned_seq1, aligned_seq2)) + "\n" + aligned_seq2.replace(' ', '-')

    return max_score, best_shift, best_aligned


def main():
    input_file = 'data.txt'
    output_file = 'wynik.txt'

    data = read_data(input_file)
    results = []

    for i, (seq1, seq2) in enumerate(data):
        max_score, best_shift, best_aligned = align_sequences(seq1, seq2)
        result = {
            "pair_num": i + 1,
            "max_score": max_score,
            "shift": best_shift,
            "seq1": seq1,
            "aligned": best_aligned.split("\n")[1],
            "seq2": seq2
        }
        results.append(result)

    write_results(output_file, results)


if __name__ == "__main__":
    main()
