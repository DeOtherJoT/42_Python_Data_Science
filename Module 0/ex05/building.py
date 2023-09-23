import sys


def get_input() -> str:
    '''Returns the string to be broken down'''
    if (len(sys.argv) == 1):
        print("What is the text to count?")
        string = sys.stdin.readline()
    else:
        string = sys.argv[1]
    if ('\n' not in string):
        print('')
    return (string)


def breakdown(target: str):
    '''Counts and prints the components of the string'''
    total = len(target)
    upper = sum(1 for c in target if c.isupper())
    lower = sum(1 for c in target if c.islower())
    punc = sum(1 for c in target if c in "!\"#$%&'()*+,-./:;<=>?@][^\\_`{|}~")
    space = sum(1 for c in target if c.isspace())
    digit = sum(1 for c in target if c.isdigit())
    print("The text contains {} characters:".format(total))
    print("{} upper letters".format(upper))
    print("{} lower letters".format(lower))
    print("{} punctuation marks".format(punc))
    print("{} spaces".format(space))
    print("{} digits".format(digit))


def main():
    sys.tracebacklimit = 0

    assert (len(sys.argv) <= 2), "Program takes either one or no argumnets"

    try:
        target = get_input()
        breakdown(target)
    except KeyboardInterrupt:
        print("\nCtrl + C detected.")


if __name__ == "__main__":
    main()
