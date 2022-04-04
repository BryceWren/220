from random import randint


def make_hidden_secret(secret_word, guesses):
    empty_string = ""
    for letter in secret_word:
        if letter in guesses:
            empty_string += letter
        else:
            empty_string += " _ "
    print(empty_string)


make_hidden_secret("reverse", ['e', 'i'])