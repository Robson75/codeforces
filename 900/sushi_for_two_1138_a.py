class SushiForTwo:

    pass


if __name__ == "__main__":
    n = int(input())
    types = list(map(int, input().split()))
    seq_tuna = 0
    seq_eel = 0
    max_seq = 0
    seq = ""
    start_second = False
    for t in types:
        if seq == "":
            if t == 1:
                seq = "tuna"
                seq_tuna += 1
            else:
                seq = "eel"
                seq_eel += 1
        else:
            if t == 1 and seq == "tuna":
                seq_tuna += 1
            elif t == 2 and seq == "eel":
                seq_eel += 1
            elif t == 1 and seq == "eel":
                seq = "tuna"
                current_seq = 2 * min(seq_tuna, seq_eel)
                max_seq = max(current_seq, max_seq)
                seq_tuna = 1
            elif t == 2 and seq == "tuna":
                seq = "eel"
                current_seq = 2 * min(seq_tuna, seq_eel)
                max_seq = max(current_seq, max_seq)
                seq_eel = 1
    current_seq = 2 * min(seq_tuna, seq_eel)
    max_seq = max(current_seq, max_seq)
    print(max_seq)


