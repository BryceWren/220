def encode(message, key):
    user = str(message)
    key = (key)
    encoded_string = ""
    for character in user:
        code_character = (ord(character) + key)
        enc_let = (chr(code_character))
        encoded_string = encoded_string + enc_let
    return encoded_string

def encode_better(message, key):
    user = message
    key = key
    encoded_string = ""
    for number in range(len(user)):
        code_character = ord(user[number]) - 65
        index_key = (number % len(key))
        key_string = key[index_key]
        key_number = ord(key_string) - 65
        difference_value = (code_character + key_number) % 58
        value_letter = difference_value + 65
        encoded_string = encoded_string + chr(value_letter)
    return encoded_string