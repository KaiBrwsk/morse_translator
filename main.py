# Morse Dictionary
MORSE_CODE = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '0': '-----',
    ',': '--..--',
    '.': '.-.-.-',
    '?': '..--..',
    '/': '-..-.',
    '-': '-....-',
    '(': '-.--.',
    ')': '-.--.-',
    ' ': ' '
}


def morse_translation(word_to_translate):
    input_translated = ""
    message = ""

    # Translate each character and add to translated string
    for element in word_to_translate:
        if element in MORSE_CODE:
            element_morse = MORSE_CODE[element]
            input_translated += element_morse + " "
            message = f"{user_input} translated into morse code is {input_translated}\n"
        else:
            message = "Please don't use special characters. Only letters, numbers and normal characters of sentences are allowed.\n"

    return message


def user_continue():
    keep_asking = True
    while keep_asking:
        # Ask if user wants to continue
        user_decision = input("Would you like to continue? ").lower()
        if user_decision == "no":
            print("Thank you for using the translator.")
            return False
        elif user_decision == "yes":
            return True
        else:
            print("This is no valid input.\n")


running = True
while running:
    # Get user input to translate
    user_input = input("Please type in a word or sentence: ").upper()

    # Translate user input if any exists
    if user_input:
        # Display translation to user
        print(morse_translation(user_input))
    else:
        print("This is no valid input.")

    # Check if user wants to continue
    if not user_continue():
        running = False

