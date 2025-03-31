def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def count_words(text):
    words = text.split()
    return len(words)

def main():
    print({count_words(get_book_text('./books/frankenstein.txt'))}, "words found in the document")
    
main()