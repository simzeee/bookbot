import sys
from stats import get_num_words, print_report


def main():
    args = sys.argv
    if len(args) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    with open(args[1]) as f:
        file_contents = f.read()
        number_of_words = get_num_words(file_contents)
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


main()
