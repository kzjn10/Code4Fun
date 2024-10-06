def find_kth_character(k: int) -> str:
    word = "a"

    # Shift current charactor to next charactor, if z -> a
    def shift_to_char(c: str) -> str:
        new_index = (ord(c) - ord('a') + 1) % 26 + ord('a')
        return chr(new_index)

    while len(word) < k:
        new_string = ''.join(shift_to_char(c) for c in word)
        word += new_string
    return word[k - 1]


# Test cases
print(find_kth_character(5))  # Output: "b"
print(find_kth_character(10))  # Output: "c"
