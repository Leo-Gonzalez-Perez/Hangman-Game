from random import choice

#crear lista
def choice_word():
    words = ['saturno', 'colegio', 'vertebrado', 'silencio', 'majestad']
    the_word_choiced = choice(words)
    return the_word_choiced

def generate_hidden_word(the_word):
    word_len = len(the_word)
    hidden_word = "_" * word_len
    return hidden_word

def ask_and_verif_letter():
    letter = input("Ingresa una letra: ")
    letter = letter.lower()
    if len(letter) == 1 and letter.isalpha():
        return letter
    else:
        ask_and_verif_letter()

def is_letter_in_word(the_word, letter):
    position = []
    for index, char in enumerate(the_word):
        if char == letter:
            position.append(index)
    if len(position) == 0:
        print("La letra no esta en la palabra.")
    else:
        print("Bien!!! La letra esta en la palabra.")
    return position

def  add_letter_to_hidden_word(hidden_word, letter, positions):
    list_hidden_word = list(hidden_word)
    for position in positions:
            if 0 <= position < len(list_hidden_word):
                list_hidden_word[position] = letter

    modified_string = ''.join(list_hidden_word)
    return modified_string

def how_many_letters(the_word):
    letters_in_word = len(set(the_word))
    return letters_in_word


lives = 6
letters_OK = []
letters_KO = []
letter_discovered = 0
you_win = False
all_letters = []

print("Hola, bienvenido al juego del ahorcado.")
name = input("Ingresa tu nombre para comenzar: ")
print(f"Esta es tu palabra: ")
the_word = choice_word()
letters_in_word = how_many_letters(the_word)
hidden_word = generate_hidden_word(the_word)
print(hidden_word)
while lives > 0:
    letter = ask_and_verif_letter()
    if letter in all_letters:
        print("Letra repetida")
        continue
    else:
        all_letters.append(letter)
    positions = is_letter_in_word(the_word, letter)
    if len(positions) != 0:
        letter_discovered += 1
        hidden_word = add_letter_to_hidden_word(hidden_word, letter, positions)
        print(hidden_word)
        if letter_discovered == letters_in_word:
            you_win = True
            print(f"Ganaste!!!!!")
            break
    else:
        lives -= 1
if not you_win:
    print(f"Perdiste {name}, la palabra era: \"{the_word}\"")