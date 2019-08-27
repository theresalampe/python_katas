import python_katas.morse_decoder.main.Morsecode as Morsecode

morse_alphabet = Morsecode.morseAlphabet


def encode_value(letter):
    for key, value in morse_alphabet.items():
        if value == letter:
            return key


def encode_word(word):
    output = ""
    letters = word.split(" ")
    for letter in letters:
        output += encode_value(letter)
    return output


def encode_sentence(sentence):
    output = []
    words = sentence.split("   ")
    for word in words:
        output.append(encode_word(word))
    return " ".join(output)
