def count_vowels(text: str) -> int:
    """Return the number of vowels in the given text."""
    num_vowels = 0

    for letter in text:
        if letter == 'a' or letter == 'A':
            num_vowels += 1
        elif letter == 'e' or letter == 'E':
            num_vowels += 1
        elif letter == 'i' or letter == 'I':
            num_vowels += 1
        elif letter == 'o' or letter == 'O':
            num_vowels += 1
        elif letter == 'u' or letter == 'U':
            num_vowels += 1

    return num_vowels


if __name__ == "__main__":
    word = input("Enter a word or sentence: ")
    total = count_vowels(word)
    print(f'The word "{word}" contains {total} vowels')