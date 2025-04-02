from stats import count_words
from stats import count_characters
from stats import list_sorted

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents


def main():
    print(count_words(get_book_text('./books/frankenstein.txt')), "words found in the document")
    #print(count_characters(get_book_text('./books/frankenstein.txt')))
    report = list_sorted(count_characters(get_book_text('./books/frankenstein.txt')))
    for element in report:
        if element[0].isalpha() == True:
            print(element[0],":", element[1])
main()