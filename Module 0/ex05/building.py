import sys


def main():
    sys.tracebacklimit = 0

    assert (len(sys.argv) <= 2), "Program takes either one or no argumnets"

    if (len(sys.argv) == 1):
        print("What is the text to count?")
        string = sys.stdin.readline()
    else:
        string = sys.argv[1]
    total = len(string)
    upper = sum(1 for c in string if c.isupper())
    lower = sum(1 for c in string if c.islower())
    punc = sum(1 for c in string if c in "!\"#$%&'()*+,-./:;<=>?@][^\\_`{|}~")
    space = sum(1 for c in string if c.isspace())
    digit = sum(1 for c in string if c.isdigit())
    print("The text contains {} characters:".format(total))
    print("{} upper letters".format(upper))
    print("{} lower letters".format(lower))
    print("{} punctuation marks".format(punc))
    print("{} spaces".format(space))
    print("{} digits".format(digit))


if __name__ == "__main__":
    main()
