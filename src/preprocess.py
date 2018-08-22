def remove_whitespace(string):
    return ''.join(string.split())

def parse_first_cabin_letter(cabin):
    for letter in cabin:
        if letter.isalpha():
            return letter
    else: 
        return false

    