import sys


def ft_isint(arg: str) -> bool:
    try:
        int(arg)
    except ValueError:
        return (False)
    else:
        return (True)


def main():
    sys.tracebacklimit = 0

    if (len(sys.argv) == 1):
        return
    assert (len(sys.argv) == 2), "more than one argument is provided"
    assert (ft_isint(sys.argv[1])), "argument is not an integer"

    target = int(sys.argv[1])
    if (target % 2 == 0):
        print("I'm Even.")
    else:
        print("I'm Odd.")


if __name__ == "__main__":
    main()
