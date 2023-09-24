import sys


def translate(string: str):
    '''Takes a string and converts it to morse code'''

    MORSE = {
        " ": "/",
        "A": ".-",
        "B": "-...",
        "C": "-.-.",
        "D": "-..",
        "E": ".",
        "F": "..-.",
        "G": "--.",
        "H": "....",
        "I": "..",
        "J": ".---",
        "K": "-.-",
        "L": ".-..",
        "M": "--",
        "N": "-.",
        "O": "---",
        "P": ".--.",
        "Q": "--.-",
        "R": ".-.",
        "S": "...",
        "T": "-",
        "U": "..-",
        "V": "...-",
        "W": ".--",
        "X": "-..-",
        "Y": "-.--",
        "Z": "--..",
        "1": ".----",
        "2": "..---",
        "3": "...--",
        "4": "....-",
        "5": ".....",
        "6": "-....",
        "7": "--...",
        "8": "---..",
        "9": "----.",
        "0": "-----"
    }

    t_char = []

    for c in string:
        t_char.append(MORSE.get(c.upper()))

    print(" ".join(t_char))


def main():
    sys.tracebacklimit = 0

    assert (len(sys.argv) == 2), \
        "The program takes in one and only one argument"
    assert (len(sys.argv[1]) > 0), \
        "The program's argument cannot be empty"
    assert (sys.argv[1].replace(' ', '').isalnum()), \
        "The arguments are bad"

    translate(sys.argv[1])


if __name__ == "__main__":
    main()
