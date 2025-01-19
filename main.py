def main():

    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        # print(file_contents)
        words = file_contents.split()
        number_of_words = len(words)
        character_count = count_characters(file_contents)
        # print(character_count)
        final_report = print_report(character_count, number_of_words)
        print(final_report)


def count_characters(all_words):
    count_dict = {}
    for s in all_words:
        lower_s = s.lower()
        if lower_s in count_dict:
            count_dict[lower_s] = count_dict[lower_s] + 1
        else:
            count_dict[lower_s] = 1
    return count_dict


def sort_on(dict):
    return dict["num"]


def print_report(character_count, word_count):
    report = "--- Begin report of books/frankenstein.txt ---\n"
    report += f"{word_count} words found in the document\n"
    result = [{key: value} for key, value in character_count.items()]
    filtered_sorted_data = sorted(
        (d for d in result if list(d.keys())[0].isalpha()),
        key=lambda d: list(d.values())[0],
        reverse=True,
    )

    for character_count in filtered_sorted_data:
        (key,) = character_count.keys()
        report += f"\nThe '{key}' character was found {character_count[key]} times"
    report += "\n--- End report ---"
    return report


main()
