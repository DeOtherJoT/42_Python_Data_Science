def ft_verify(target: list) -> bool:
    '''Verifies if the elements of the list are either an int or a flot'''
    for x in target:
        elem_type = type(x)
        if elem_type not in (int, float) or x <= 0:
            return (False)
    return (True)


def give_bmi(height: list[int | float], weight: list[int | float])\
      -> list[int | float]:
    '''Returns a list of BMI values based on the heights and weights given'''

    assert (len(height) == len(weight)), "The list sizes are not equal"
    assert (ft_verify(height) and ft_verify(weight)), "The values aren't valid"

    ret = []
    for h, w in zip(height, weight):
        ret.append(w / (h * h))
    return (ret)


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    '''Returns True if bmi[x] > limit, False otherwise'''

    assert (ft_verify(bmi)), "The BMI has bad values"

    ret = [True if x > limit else False for x in bmi]
    return (ret)
