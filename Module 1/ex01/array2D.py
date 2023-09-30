import numpy as np


def verify_list(family: list) -> bool:
    '''Verifies that the list passed is a 2D array that is transformable 
    by numpy'''
    try:
        temp = np.array(family)
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

    try:
        assert (type(family) == list), \
            "Argument 1 needs to be a list"
        assert (type(start) == int and type(end) == int), \
            "Argument 2 & 3 needs to be an int"
        assert (verify_list(family) == True), \
            "Argument 1 is not a valid 2D array"
    except AssertionError as e:
        print(e)
    
    conv = np.array(family)
    print("My shape is : {}".format(conv.shape))
    new = family[start:end]
    if (new == []):
        print("WARNING: The start / end arguments produces an empty list.")
    print("My new shape is : {}".format(np.array(new).shape))
    return(new)
