import sys
from ft_filter import ft_filter


def check_str(string: str) -> bool:
    '''Function checks if the string has special characters.'''
    total = sum(1 for c in string if c in "!\"#$%&'()*+,-./:;<=>?@][^\\_`{|}~")
    return (total == 0)


def ft_isint(string: str) -> bool:
    '''Function determines if the string is an integer or not.'''
    try:
        int(string)
    except ValueError:
        return (False)
    else:
        return (True)



def filter_string(S: str, N: str):
    '''Returns a list of S words longer than N'''
    words = S.split()
    print([x for x in ft_filter(lambda x: len(x) > int(N), words)])


def main():
    sys.tracebacklimit = 0

    assert (len(sys.argv) == 3), "the arguments are bad"
    assert (check_str(sys.argv[1])), "the string has special characters"
    assert(ft_isint(sys.argv[2])), "the integer is not integer"

    filter_string(sys.argv[1], sys.argv[2])


if __name__ == "__main__":
    main()