from stats import count_words
from stats import count_characters
from stats import list_sorted
import sys

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents


def main():
    if (len(sys.argv) !=2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print("============ BOOKBOT ============\nAnalyzing book found at books/frankenstein.txt...\n----------- Word Count ----------")
    print("Found",count_words(get_book_text(sys.argv[1])), "total words")
    #print(count_characters(get_book_text('./books/frankenstein.txt')))
    print("----------- Character Count -----------")
    report = list_sorted(count_characters(get_book_text(sys.argv[1])))
    for element in report:
        if element[0].isalpha() == True:
            print(f"{element[0]}:",element[1])
main()