from graphics import *
def encode_better():
    user = input("enter a message:").upper().replace(" ", "")
    key = input("enter a key:").upper().replace(" ", "")
    encoded_string = ""
    for number in range(len(user)):
        code_character = ord(user[number]) - 65
        index_key = (number % len(key))
        key_string = key[index_key]
        key_number = ord(key_string) - 65
        difference_value = (code_character + key_number) % 26
        value_letter = difference_value + 65
        encoded_string = encoded_string + chr(value_letter)
    print(encoded_string)
#encode_better()

def vigenere_cipher():
    win = GraphWin("Encryption Machine", 700, 700)
    message_text = Text(Point(100, 100), 'Message to code')
    message_text.draw(win)
    message_entry = Entry(Point(400, 100), 50)
    message_entry.draw(win)
    keyword_text = Text(Point(100, 200), 'Enter Keyword')
    keyword_text.draw(win)
    keyword_entry = Entry(Point(400, 200), 50)
    keyword_entry.draw(win)
    encode_box = Rectangle(Point(250, 300), Point(450, 400))
    encode_text = Text(Point(350, 350), "encode")
    encode_box.draw(win)
    encode_text.draw(win)
    win.getMouse()
    text_keyword_entry = keyword_entry.getText()
    text_message_entry = message_entry.getText()
    encode_text.undraw()
    encode_box.undraw()
    user = text_message_entry.upper().replace(" ", "")
    key = text_keyword_entry.upper().replace(" ", "")
    encoded_string = ""
    for number in range(len(user)):
        code_character = ord(user[number]) - 65
        index_key = (number % len(key))
        key_string = key[index_key]
        key_number = ord(key_string) - 65
        difference_value = (code_character + key_number) % 26
        value_letter = difference_value + 65
        encoded_string = encoded_string + chr(value_letter)
    encoded_string_txt = Text(Point(350, 520), encoded_string)
    close_text = Text(Point(350, 500), "Click anywhere to close")
    close_text.draw(win)
    encoded_string_txt.draw(win)
    win.getMouse()
    win.close()

vigenere_cipher()