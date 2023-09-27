import numpy as np


def verify_list(family: list) -> bool:
    try:
        temp = np.array(family)
        print(temp.ndim)
        if (temp.ndim == 2):
            return (True)
        else:
            return (False)
    except ValueError:
        return (False)


def slice_me(family: list, start: int, end: int) -> list:
    '''Prints the shape of the list before and after slicing, and
    returns a truncated copy of the array based on the provided
    arguments.'''

    assert (type(family) == list), \
        "Argument 1 needs to be a list"
    assert (type(start) == int and type(end) == int), \
        "Argument 2 & 3 needs to be an int"
    assert (verify_list(family) == True), \
        "Argument 1 is not a valid 2D array"

    print("here")


test = [
 [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
 [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
 [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
 ]


slice_me(test, 5, 31)