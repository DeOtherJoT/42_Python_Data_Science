def get_args(args) -> list[float]:
    '''
    Takes in the variable arguments and confirms each element is a number, and
    returns a sorted list.
    '''
    ret_lst = []

    for arg in args:
        if (isinstance(arg, (int, float)) is False):
            raise AssertionError("Variable *args must be of type int or float")
        ret_lst.append(float(arg))
    ret_lst.sort()
    return ret_lst


def mean(arr: list[float]) -> float:
    '''
    Returns the average value of the elements in the list.
    '''
    return (sum(x for x in arr) / len(arr))


def median(arr: list[float]) -> float:
    '''
    Returns the middle value of the sorted list.
    '''
    mid_val = len(arr) // 2
    if (len(arr) % 2 == 0):
        return ((arr[mid_val] + arr[mid_val + 1]) / 2)


def quartile(arr: list[float]) -> tuple[float, float]:
    '''
    Returns the 25% and 75% percentile of the sorted list.

    Q1:
    If len(arr) * 0.25 is an integer, then the first quartile is the mean
    of the numbers at positions len(arr) * 0.25 and [len(arr) * 0.25] + 1.
    Else, if len(arr) * 0.25 is a float, then round it up. The number at
    this position in the set (not the index yet) is the first quartile.

    Q3:
    If len(arr) * 0.75 is an integer, then the first quartile is the mean
    of the numbers at positions len(arr) * 0.75 and [len(arr) * 0.75] + 1.
    Else, if len(arr) * 0.75 is a float, then round it up. The number at
    this position in the set (not the index yet) is the third quartile.
    '''
    length = len(arr)
    pos_q1 = length * 0.25
    if (round(pos_q1) == pos_q1):
        pos_q1 = int(pos_q1) - 1
        val_q1 = (arr[pos_q1] + arr[pos_q1 + 1]) / 2
    else:
        pos_q1 = (int(pos_q1) + bool(pos_q1 % 1)) - 1
        val_q1 = arr[pos_q1]
    pos_q3 = length * 0.75
    if (round(pos_q3) == pos_q3):
        pos_q3 = int(pos_q3) - 1
        val_q3 = (arr[pos_q3] + arr[pos_q3 + 1]) / 2
    else:
        pos_q3 = (int(pos_q3) + bool(pos_q3 % 1)) - 1
        val_q3 = arr[pos_q3]
    return val_q1, val_q3


def var(arr: list[float]) -> float:
    '''
    Returns the variance of a dataset.
    '''
    if (len(arr) == 0):
        return (0)
    avrg = mean(arr)
    sum_data = sum((x - avrg) ** 2 for x in arr)
    return sum_data / len(arr)


def std(arr: list[float]) -> float:
    '''
    Returns the standard deviation of a dataset.
    '''
    return var(arr) ** 0.5


def ft_statistics(*args, **kwargs) -> None:
    '''
    Takes in an unknown list of numbers and prints out statistical values
    based on the keyword arguments dictionary passed.
    '''
    try:
        sorted_num = get_args(args)
        for key, item in kwargs.items():
            if len(sorted_num) == 0:
                print("ERROR")
            elif item == "mean":
                print(f"mean : {mean(sorted_num)}")
            elif item == "median":
                print(f"median : {median(sorted_num)}")
            elif item == "quartile":
                q1, q3 = quartile(sorted_num)
                print(f"quartile : [{q1}, {q3}]")
            elif item == "std":
                print(f"std : {std(sorted_num)}")
            elif item == "var":
                print(f"var : {var(sorted_num)}")
            else:
                continue
    except Exception as e:
        print(f"{type(e).__name__}: {e}")


ft_statistics()
