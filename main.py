from stats import count_words
from stats import count_characters
from stats import list_sorted

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents


def main():
    print("============ BOOKBOT ============\nAnalyzing book found at books/frankenstein.txt...\n----------- Word Count ----------")
    print("Found",count_words(get_book_text('./books/frankenstein.txt')), "total words")
    #print(count_characters(get_book_text('./books/frankenstein.txt')))
    print("----------- Character Count -----------")
    report = list_sorted(count_characters(get_book_text('./books/frankenstein.txt')))
    for element in report:
        if element[0].isalpha() == True:
            print(element[0],":", element[1])
main()