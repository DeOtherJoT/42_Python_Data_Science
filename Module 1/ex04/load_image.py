import numpy as np
import matplotlib.pylab as plt


def ft_load(path: str) -> np.ndarray:

    try:
        assert (isinstance(path, str)), "Argument must be a string."
    except AssertionError as e:
        print("AssertionError:", e)
        return

    try:
        image = plt.imread(path)
        return (image)
    except Exception as e:
        print("{}: {}".format(type(e).__name__, e))