def callLimit(limit: int):
    '''
    Decorator that limits how many times a function that is wrapped by it
    can be called.
    '''
    count = 0

    def callLimiter(function):
        '''
        Takes the function to be wrapped as an argument.
        '''
        def limit_function(*args, **kwds):
            '''
            Does the work of making sure the function is not called above the
            limit.
            '''
            nonlocal count
            if (count < limit):
                count += 1
                return (function(*args, **kwds))
            else:
                print(f"Error: {function} call too many times")

        return limit_function

    return callLimiter
