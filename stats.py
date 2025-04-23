def get_num_words(book):
    words = book.split()
    number_of_words = len(words)
    return number_of_words


def print_report(character_count, word_count):
    report = "--- Begin report of books/frankenstein.txt ---\n"
    report += f"Found {word_count} total words\n"
    result = [{key: value} for key, value in character_count.items()]
    filtered_sorted_data = sorted(
        (d for d in result if list(d.keys())[0].isalpha()),
        key=lambda d: list(d.values())[0],
        reverse=True,
    )

    for character_count in filtered_sorted_data:
        (key,) = character_count.keys()
        report += f"\n{key}: {character_count[key]}"
    report += "\n--- End report ---"
    return report
