def main():

    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        # print(file_contents)
        words = file_contents.split()
        # number_of_words = len(words)
        word_count = count_words(file_contents)
        print(word_count)


def count_words(all_words):
    count_dict = {}
    for s in all_words:
        lower_s = s.lower()
        if lower_s in count_dict:
            count_dict[lower_s] = count_dict[lower_s] + 1
        else:
            count_dict[lower_s] = 1
    return count_dict


main()
