def square(x: int | float) -> int | float:
    '''
    Returns the square of the argument
    '''
    return (x * x)


def pow(x: int | float) -> int | float:
    '''
    Returns the exponentiation of itself, that is x^x.
    '''
    return (x ** x)


def outer(x: int | float, function) -> object:
    '''
    Closer Function
    Returns an object that when called, returns the result
    of the argument's calculation
    '''
    count = 0

    def inner() -> float:
        '''
        Closure part of the closer function
        '''
        nonlocal count
        if (count == 0):
            count = x
        count = function(count)
        return (count)
    return inner
