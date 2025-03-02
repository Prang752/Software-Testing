from itertools import combinations

def is_alternating(subs):
    return all(subs[i] != subs[i + 1] for i in range(len(subs) - 1))

def alternate(s):
    unique_chars = set(s)
    max_length = 0

    for c1, c2 in combinations(unique_chars, 2):
        filtered = [ch for ch in s if ch == c1 or ch == c2]

        if is_alternating(filtered):
            max_length = max(max_length, len(filtered))

    return max_length
