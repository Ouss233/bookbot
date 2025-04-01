def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    number_char = {}
    for char in text:
        if char.lower() not in number_char:
            count = 0
            for x in text:
                if x.lower() == char.lower():
                    count += 1
            number_char[char.lower()] = count
    return number_char


