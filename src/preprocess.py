def remove_whitespace(string):
    return ''.join(string.split())

def parse_first_cabin_letter(cabin):
    for letter in cabin:
        if letter.isalpha():
            return letter
    else: 
        return false

def parse_alphabetic_characters(ticket):
    if isinstance(ticket, str):
        alphas = [character for character in ticket if character.isalpha()]
    else:
        alphas = []
    return ''.join(alphas)
